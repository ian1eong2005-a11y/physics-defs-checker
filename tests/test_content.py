"""Every question: model answer passes its own marking, sample answers pass / fail as declared, three hints, no cloze hints,
and both syllabuses have content in every chapter."""
from collections import Counter

import pytest

from trainer.config import CHAPTERS, SYLLABI, TOPICS, chapter_of, topics_in
from trainer.content import TEMPLATES, for_syllabus
from trainer.formula import check, normalise
from trainer.marker import mark

DEFS = [t for t in TEMPLATES if t.category == "defs"]
FORMS = [t for t in TEMPLATES if t.category in ("formula", "units")]


def test_inventory():
    assert len(DEFS) >= 100, len(DEFS)
    assert len([t for t in TEMPLATES if t.category == "formula"]) >= 45
    assert len([t for t in TEMPLATES if t.category == "units"]) >= 40
    ids = [t.id for t in TEMPLATES]
    assert len(ids) == len(set(ids))
    for t in TEMPLATES:
        assert t.topic in TOPICS, t.id
        assert t.syllabi and t.syllabi <= set(SYLLABI), t.id
        for syl in t.syllabi:
            assert chapter_of(t.topic, syl) is not None, f"{t.id}: topic {t.topic} is not in syllabus {syl}"


@pytest.mark.parametrize("syl", list(SYLLABI))
def test_every_chapter_has_definitions_and_most_have_formulae(syl):
    tpls = for_syllabus(syl)
    for ch in CHAPTERS[syl]:
        topics = set(topics_in(ch, syl))
        n_defs = sum(1 for t in tpls if t.category == "defs" and t.topic in topics)
        assert n_defs >= 2, f"{syl} chapter {ch}: only {n_defs} definitions"
    n_form_chapters = sum(1 for ch in CHAPTERS[syl] if any(t.category == "formula" and t.topic in topics_in(ch, syl) for t in tpls))
    assert n_form_chapters >= 9, f"{syl}: formulae in only {n_form_chapters} chapters"
    levels = Counter(t.level for t in tpls if t.category == "defs")
    assert set(levels) == {1, 2, 3, 4, 5}, levels


@pytest.mark.parametrize("tpl", TEMPLATES, ids=lambda t: t.id)
def test_well_formed(tpl):
    q = tpl.make(0)
    assert q.template_id == tpl.id and q.level == tpl.level and q.topic == tpl.topic and q.category == tpl.category
    assert q.stem.strip() and len(q.hints) == 3 and all(h.strip() for h in q.hints)
    assert q.working and q.formula
    for h in q.hints:
        assert "___" not in h, f"{tpl.id}: cloze hint {h!r}"
    passes, fails = q.samples
    assert passes and fails, f"{tpl.id}: give sample answers"


@pytest.mark.parametrize("tpl", DEFS, ids=lambda t: t.id)
def test_definition_marking(tpl):
    q = tpl.make(0)
    assert q.kind == "written" and q.points and q.model_answer
    r = mark(q.model_answer, q.points, q.pitfalls, q.min_points)
    assert r.passed, f"{tpl.id}: model answer fails its own marking: missed {r.missed}, pitfalls {r.pitfalls}"
    assert not mark("", q.points, q.pitfalls, q.min_points).passed
    passes, fails = q.samples
    for a in passes:
        r = mark(a, q.points, q.pitfalls, q.min_points)
        assert r.passed, f"{tpl.id}: should PASS: {a!r} -> missed {r.missed}, pitfalls {r.pitfalls}"
    for a in fails:
        r = mark(a, q.points, q.pitfalls, q.min_points)
        assert not r.passed, f"{tpl.id}: should FAIL: {a!r} -> hit {r.hit}"
    for h in q.hints:
        assert h.strip().lower() != q.model_answer.strip().lower()


@pytest.mark.parametrize("tpl", FORMS, ids=lambda t: t.id)
def test_formula_checking(tpl):
    q = tpl.make(0)
    assert q.kind == "formula" and q.forms
    assert all(f == normalise(f) for f in q.forms), f"{tpl.id}: forms must be normalised"
    passes, fails = q.samples
    for a in passes:
        assert check(a, q.forms, q.wrongs).passed, f"{tpl.id}: should PASS: {a!r} -> {normalise(a)!r} not in {q.forms}"
    for a in fails:
        assert not check(a, q.forms, q.wrongs).passed, f"{tpl.id}: should FAIL: {a!r}"
    for w, msg in q.wrongs.items():
        assert w not in q.forms, f"{tpl.id}: wrong form {w!r} is also an accepted form"
        assert msg.strip()
    assert not check("", q.forms, q.wrongs).passed
