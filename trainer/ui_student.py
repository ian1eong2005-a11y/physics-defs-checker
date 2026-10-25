"""Student view: one definition / formula / unit at a time, scripted tutor after a wrong answer, level banners."""
import random
import time

import streamlit as st

from .config import CATEGORIES, CHAPTERS, DOWN_STREAK, LEVEL_NAMES, SYLLABI, UP_STREAK, chapter_of, topics_in
from .content import TEMPLATES, for_syllabus, topics_with_content
from .engine import apply_first_attempt, levels_available, repeat_until_correct, select_template
from .formula import check as check_formula
from .marker import mark
from .store import Attempt

_rng = random.Random()


def _qs():
    return st.session_state.setdefault("qs", {})


def _templates(rec):
    return for_syllabus(rec.syllabus)


def _serve(store, rec, cat, topics, mixed):
    state = rec.states[cat]
    tpl = select_template(_templates(rec), cat, None if mixed else state.level, topics, rec.recent[cat], _rng)
    q = tpl.make(_rng.randrange(1_000_000_000))
    rec.recent[cat].append(tpl.id)
    rec.current[cat] = q
    st.session_state["qs"] = dict(
        cat=cat, question=q, level=state.level, phase="answer", hints_shown=0, hints_used=0,
        formula_shown=False, chat=[], event=None, retry_correct=False, serial=_rng.randrange(1 << 30), served_at=time.time(),
    )
    store.touch(rec.key)
    return st.session_state["qs"]


def _written_feedback(result, first=True):
    lead = "Not quite yet." if first else "Still not there."
    parts = [f"{lead} You have **{result.score}** marking points so far."]
    if result.too_short:
        parts.append("Write the full definition in a sentence; a word or two is not enough.")
    if result.hit:
        parts.append("✔ " + "; ".join(result.hit) + ".")
    if result.missed:
        n = len(result.missed)
        parts.append(f"✘ {n} marking point{'s' if n > 1 else ''} still missing. Ask for a hint or the key words.")
    for msg in result.pitfalls:
        parts.append("⚠ " + msg)
    return " ".join(parts)


def _formula_feedback(result, first=True):
    lead = "Not quite." if first else "Still not it."
    if result.message:
        return f"{lead} {result.message}"
    return f"{lead} That is not the form on the syllabus. Check which quantities appear and which is divided by which; ask for a hint if you are stuck."


def _answer(store, rec, response):
    qs = _qs()
    q, cat = qs["question"], qs["cat"]
    state = rec.states[cat]
    if q.kind == "written":
        result = mark(response, q.points, q.pitfalls, q.min_points)
        correct = result.passed
    else:
        result = check_formula(response, q.forms, q.wrongs)
        correct = result.passed
    qs["mark"], qs["last_answer"] = result, response
    chosen = response.strip()[:80]
    first = qs["phase"] == "answer"
    if first:                                                   # first attempt: the only one that counts
        qs["event"] = apply_first_attempt(state, correct)
        store.log_attempt(rec.key, Attempt(time.time(), cat, q.template_id, q.topic, qs["level"], chosen, q.model_answer or "", correct, False, 0))
    else:                                                       # retry: no streak credit
        store.log_attempt(rec.key, Attempt(time.time(), cat, q.template_id, q.topic, qs["level"], chosen, q.model_answer or "", correct, True, qs["hints_used"]))
    if correct:
        qs["phase"] = "solved"
        qs["retry_correct"] = not first
    else:
        msg = _written_feedback(result, first) if q.kind == "written" else _formula_feedback(result, first)
        if first or repeat_until_correct(cat, qs["level"]):
            qs["phase"] = "hints"
            qs["chat"].append(("tutor", msg))
        else:
            qs["phase"] = "revealed"
    store.touch(rec.key)


def _box(colour):
    return f'<span style="display:inline-block;width:16px;height:16px;border-radius:3px;margin:0 2px;vertical-align:middle;background:{colour}"></span>'


def _streak_strip(state):
    boxes = _box("#2e9e5b") * state.correct_streak + _box("#dcdfe4") * max(0, UP_STREAK - state.correct_streak)
    wrong = _box("#d64545") * state.wrong_streak + _box("#dcdfe4") * max(0, DOWN_STREAK - state.wrong_streak)
    return f"Correct in a row: {boxes}&nbsp;&nbsp;&nbsp; Wrong in a row: {wrong}"


def _chapter_label(syl, ch):
    return f"Ch {ch} {CHAPTERS[syl][ch]}"


def render_student(store, rec):
    store.touch(rec.key)
    ss = st.session_state
    syl = rec.syllabus

    with st.sidebar:
        st.markdown(f"### {rec.name}\n{rec.cls} · {SYLLABI[syl]}")
        for cat, label in CATEGORIES.items():
            s = rec.states[cat]
            acc = "–" if s.accuracy is None else f"{round(100 * s.accuracy)}%"
            st.markdown(f"**{label}**: L{s.level} · {s.attempted} done · {acc} correct")
        if st.button("Log out", width="stretch"):
            for k in ("student_key", "qs", "category", "chapters", "mixed"):
                ss.pop(k, None)
            st.rerun()

    # ---- practice settings
    cat = st.radio("Practise", list(CATEGORIES), format_func=CATEGORIES.get, horizontal=True,
                   index=list(CATEGORIES).index(ss.get("category", "defs")), key="category_radio")
    if cat != ss.get("category"):
        ss["category"] = cat
        ss.pop("qs", None)
    have_topics = topics_with_content(cat, syl)
    available = [ch for ch in CHAPTERS[syl] if any(t in have_topics for t in topics_in(ch, syl))]
    with st.expander("Chapters and mode", expanded=False):
        default = [c for c in ss.get("chapters", available) if c in available] or available
        chapters = st.multiselect("Practise these chapters", available, default=default,
                                  format_func=lambda c: _chapter_label(syl, c), key=f"chapters_ms_{cat}_{syl}")
        missing = [c for c in CHAPTERS[syl] if c not in available]
        if missing:
            st.caption("No " + CATEGORIES[cat].lower() + " questions for: " + ", ".join(f"Ch {c}" for c in missing) + ".")
        mixed = st.toggle("Mix all levels (run through the whole chapter)", value=ss.get("mixed", False), key=f"mixed_{cat}",
                          help="Off: adaptive, you get questions at your current level and move up after 5 in a row. On: every level of the chosen chapters, unseen questions first.")
    if not chapters:
        chapters = available
    if chapters != ss.get("chapters"):
        ss["chapters"] = chapters
        ss.pop("qs", None)
    if mixed != ss.get("mixed"):
        ss["mixed"] = mixed
        ss.pop("qs", None)
    topics = {t for ch in chapters for t in topics_in(ch, syl)}

    state = rec.states[cat]
    names = LEVEL_NAMES[cat]
    pool = [t for t in _templates(rec) if t.category == cat and t.topic in topics]
    seen = len({tid for tid in rec.recent[cat] if tid in {t.id for t in pool}})
    st.markdown(f"#### {CATEGORIES[cat]} · Level {state.level}" + (" · mixed" if mixed else ""))
    st.caption(names.get(state.level, f"L{state.level}") + f" · seen {seen} of {len(pool)} in the chosen chapters")
    st.markdown(_streak_strip(state), unsafe_allow_html=True)

    top = max(levels_available(_templates(rec), cat))
    if state.level > top and not mixed:
        st.info(f"You have cleared all the {CATEGORIES[cat].lower()} levels (up to L{top}). Keep practising at L{top}, or switch on 'Mix all levels'.")

    qs = ss.get("qs")
    if not qs or qs.get("cat") != cat:
        qs = _serve(store, rec, cat, topics, mixed)
    q = qs["question"]

    # ---- the question
    st.divider()
    ch = chapter_of(q.topic, syl)
    st.caption(f"{_chapter_label(syl, ch)} · L{q.level}")
    st.markdown(q.stem)

    phase = qs["phase"]
    answering = phase in ("answer", "retry")
    if answering:
        prefill = qs.get("last_answer", "") if phase == "retry" else ""
        if q.kind == "written":
            text = st.text_area("Your answer", value=prefill, height=110, key=f"ans_{qs['serial']}",
                                placeholder="Type the definition in a full sentence, in your own words.")
        else:
            text = st.text_input("Your answer", value=prefill, key=f"ans_{qs['serial']}", placeholder="e.g. F = ma   or   N/m^2")
            st.caption("Type ^2 or ² for squared, / for divided by, × or * for times (or just write the symbols together, e.g. mgh). "
                       "Greek letters can be typed as rho, lambda, theta, delta.")
        if st.button("Check my answer", type="primary", width="stretch", key=f"submit_{qs['serial']}"):
            if text.strip():
                _answer(store, rec, text)
                st.rerun()
            else:
                st.warning("Type an answer first.")
    else:
        st.markdown("**Your answer:** " + (qs.get("last_answer") or "").replace("\n", " "))
        res = qs.get("mark")
        if q.kind == "written" and res is not None:
            st.caption(f"Marking points: {res.score}" + (" · " + "; ".join(res.hit) if res.hit else ""))

    # ---- banners
    if qs["event"] == "up":
        st.success(f"Level up! You are now on **L{state.level}**: {names.get(state.level, '')}")
    elif qs["event"] == "down":
        st.warning(f"Back to **L{state.level}** to consolidate. You will move up again after {UP_STREAK} correct in a row.")

    # ---- outcome panels
    if phase in ("solved", "revealed"):
        if phase == "solved":
            if qs["retry_correct"]:
                st.info("Correct on the second try. Retries do not count towards your streak, so keep going.")
            else:
                st.success("Correct!" + (f" {qs['mark'].score} marking points." if q.kind == "written" else ""))
        else:
            st.error("Not this time. Compare your answer with the model answer below, then move on.")
        st.markdown("**Model answer**")
        for line in q.working:
            st.markdown(f"- {line}")
        if st.button("Next question ➜", type="primary", width="stretch", key=f"next_{qs['serial']}"):
            _serve(store, rec, cat, topics, mixed)
            st.rerun()

    elif phase == "hints":
        _tutor_panel(store, rec, qs, q)

    elif phase == "retry":
        verb = "Edit your answer and check again."
        st.info(verb if not repeat_until_correct(cat, qs["level"]) else verb + " This question comes back until you get it right.")
        with st.expander("Tutor chat"):
            for role, text in qs["chat"]:
                with st.chat_message("assistant" if role == "tutor" else "user"):
                    st.markdown(text)


def _tutor_panel(store, rec, qs, q):
    st.markdown("##### 🧑‍🏫 Tutor")
    for role, text in qs["chat"]:
        with st.chat_message("assistant" if role == "tutor" else "user"):
            st.markdown(text)
    n = qs["hints_shown"]
    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button(f"💡 Give me a hint ({min(n + 1, 3)}/3)", disabled=n >= 3, width="stretch", key=f"hint_{qs['serial']}_{n}"):
            qs["chat"].append(("student", "Give me a hint"))
            qs["chat"].append(("tutor", q.hints[n]))
            qs["hints_shown"] = n + 1
            qs["hints_used"] += 1
            store.touch(rec.key)
            st.rerun()
    with c2:
        is_written = q.kind == "written"
        label = "🔑 Show key words" if is_written else "🔑 What is involved?"
        if st.button(label, disabled=(not q.formula) or qs["formula_shown"], width="stretch", key=f"formula_{qs['serial']}"):
            qs["chat"].append(("student", "What should I include?" if is_written else "What quantities are involved?"))
            qs["chat"].append(("tutor", (f"Key ideas to include: **{q.formula}**. Put them into your own sentence." if is_written
                                         else f"It involves: **{q.formula}**. Now write the relationship between them.")))
            qs["formula_shown"] = True
            qs["hints_used"] += 1
            store.touch(rec.key)
            st.rerun()
    with c3:
        if st.button("🔁 Try again", type="primary", width="stretch", key=f"retry_{qs['serial']}"):
            qs["phase"] = "retry"
            qs["serial"] = _rng.randrange(1 << 30)
            store.touch(rec.key)
            st.rerun()
    if n == 0:
        st.caption("The tutor gives one hint at a time and never the answer. Ask for the key words if you are not sure what to include.")
