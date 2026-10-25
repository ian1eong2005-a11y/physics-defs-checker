"""End-to-end through Streamlit's AppTest: login with syllabus, definition flow, formula flow, level up, dashboard."""
import pathlib

import pytest
from streamlit.testing.v1 import AppTest

APP = str(pathlib.Path(__file__).resolve().parents[1] / "app.py")


def login(at, name="Amy Tan", cls="Sec 4 · 4SG4", syl="6091"):
    at.text_input[0].input(name)
    at.selectbox[0].select(cls)
    at.radio[0].set_value(syl)
    next(b for b in at.button if b.label == "Start").click()
    at.run()
    assert at.session_state["student_key"] == (name.casefold(), cls.split(" · ")[1])


def submit(at, text):
    box = at.text_area[0] if at.text_area else at.text_input[0]
    box.input(text)
    at.run()
    next(b for b in at.button if b.key and b.key.startswith("submit_")).click()
    at.run()


def q(at):
    return at.session_state["qs"]["question"]


def good_answer(question):
    return question.model_answer if question.kind == "written" else question.samples[0][0]


@pytest.fixture
def at():
    app = AppTest.from_file(APP, default_timeout=60)
    app.run()
    assert not app.exception
    return app


def test_login_definition_flow_and_level_up(at):
    login(at)
    assert "qs" in at.session_state and q(at).kind == "written" and q(at).category == "defs"
    assert "6091" in q(at).syllabi
    for i in range(4):
        submit(at, good_answer(q(at)))
        assert at.session_state["qs"]["phase"] == "solved", i
        next(b for b in at.button if b.key and b.key.startswith("next_")).click(); at.run()
    submit(at, good_answer(q(at)))
    assert at.session_state["qs"]["event"] == "up"
    from trainer.store import get_store
    rec = get_store().get(at.session_state["student_key"])
    assert rec.states["defs"].level == 2 and rec.states["defs"].correct_streak == 0 and rec.syllabus == "6091"


def test_wrong_definition_opens_tutor_and_retry_gives_no_credit(at):
    login(at, name="Ben Lim", syl="5086")
    assert "5086" in q(at).syllabi
    submit(at, "something about physics")
    qs = at.session_state["qs"]
    assert qs["phase"] == "hints" and qs["chat"][0][0] == "tutor" and "marking points" in qs["chat"][0][1]
    next(b for b in at.button if b.key and b.key.startswith("hint_")).click(); at.run()
    assert at.session_state["qs"]["hints_shown"] == 1
    next(b for b in at.button if b.key and b.key.startswith("retry_")).click(); at.run()
    assert at.session_state["qs"]["phase"] == "retry"
    submit(at, good_answer(q(at)))
    assert at.session_state["qs"]["phase"] == "solved" and at.session_state["qs"]["retry_correct"]
    from trainer.store import get_store
    st_ = get_store().get(at.session_state["student_key"]).states["defs"]
    assert st_.correct_streak == 0 and st_.wrong_streak == 1 and st_.attempted == 1 and st_.correct == 0


def test_formula_flow_with_known_wrong_form(at):
    login(at, name="Cara Ng")
    at.radio[0].set_value("formula"); at.run()
    assert q(at).kind == "formula" and q(at).category == "formula" and q(at).level == 1
    wrong = next(iter(q(at).wrongs))
    submit(at, wrong)
    qs = at.session_state["qs"]
    assert qs["phase"] == "hints" and q(at).wrongs[wrong] in qs["chat"][0][1]
    next(b for b in at.button if b.key and b.key.startswith("retry_")).click(); at.run()
    submit(at, good_answer(q(at)))
    assert at.session_state["qs"]["phase"] == "solved"
    assert not at.exception


def test_units_and_mixed_mode(at):
    login(at, name="Dev Raj")
    at.radio[0].set_value("units"); at.run()
    assert q(at).category == "units"
    at.toggle[0].set_value(True); at.run()
    assert at.session_state["mixed"] is True
    assert q(at).category == "units"
    assert not at.exception


def test_teacher_dashboard_lists_students(at):
    login(at, name="Ella Goh")
    from trainer.store import get_store
    assert any(r["Name"] == "Ella Goh" and r["_online"] and r["Syllabus"] == "6091" for r in get_store().rows())
    at.session_state["view"] = "teacher"
    at.run()
    assert at.text_input[0].label == "Teacher password"
    at.text_input[0].input("physics")
    next(b for b in at.button if b.label == "Open dashboard").click(); at.run()
    assert at.session_state["teacher_ok"]
    assert not at.exception
