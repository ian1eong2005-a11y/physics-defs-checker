# Physics Definitions & Formulae Checker

Self-check quiz for the **definitions, formulae, units and prefixes** in the O-Level Physics syllabuses
**6091 (Pure Physics)** and **5086 (Science (Physics))**. Built for last-week revision before the national exams.
Streamlit app, no database, no LLM.

## What it does

- Students log in with **name + class** and pick **Pure Physics (6091)** or **Science (Physics) (5086)**. Only questions on
  that syllabus are served, and chapters are numbered and named as in that syllabus document.
- Three categories, chosen with a radio button:
  - **Definitions** – the student types the definition / statement / law in a sentence. It is **marked by meaning**
    (`trainer/marker.py`): marking points with many alternative phrasings, light stemming, one spelling slip allowed,
    words of a phrase in any order within a short window, and *pitfalls* (common wrong ideas from SEAB examiner reports,
    e.g. "force on an area", "rate of change of displacement per unit time", "time for a nucleus to halve") that block a pass
    with a one-sentence message.
  - **Formulae** – the student types the formula, e.g. `F = ma`, `p = F/A`, `1/R = 1/R1 + 1/R2`. The checker
    (`trainer/formula.py`) normalises spacing, ×, ·, ², ½, Greek letters (ρ, λ, θ, Δ) and subscripts, accepts listed
    rearrangements and either side of the `=` first, and recognises known wrong forms ("Rt = 1/R1 + 1/R2", "Ek = mv²",
    "n = v/c") with a specific message. The model answer gives the formula and explains only the non-obvious symbols,
    e.g. *F = ma — F is the resultant force*.
  - **Units & prefixes** – SI units of every quantity in the syllabus "Summary of key quantities", prefixes nano…tera as
    powers of ten, and unit equivalences (1 N = 1 kg m/s², 1 V = 1 J/C, 1 kWh = 3.6 MJ …).
- **Adaptive levels**: everyone starts at L1; **5 correct in a row → level up, 3 wrong in a row → level down**; only the first
  attempt at a question counts. A **"Mix all levels"** toggle instead runs through every question in the chosen chapters,
  unseen ones first (for a final sweep).
- Wrong answer → scripted **tutor**: feedback on what was hit / missed / the pitfall, up to 3 hints, the key words on request,
  then one retry (a correct retry gives no streak credit). Level-1 questions come back until answered correctly.
- **Teacher dashboard** (sidebar → Teacher, or `?teacher=1`, password from `st.secrets["TEACHER_PASSWORD"]`): who is online,
  syllabus, level / streak / accuracy per category, last 20 attempts with the actual answer typed, reset / clear / CSV.
  Refreshes every 5 s. Live only; nothing is persisted (clears on redeploy).
- Phone-friendly single column. British English, MOE/SEAB syllabus wording.

## Content bank (251 questions for 6091, 198 for 5086; 251 distinct)

Counts are **L1/L2/L3/L4(/L5) = total**. Definitions: L1 core quantities, L2 other defined terms, L3 laws/principles/conditions,
L4 the ones examiner reports say students fumble, L5 distinguish-between pairs. Formulae: L1 core, L2 rest, L3 rearranged
subject, L4 combined/derived. Units: L1 base + common derived, L2 compound, L3 prefixes, L4 equivalences.

### Pure Physics (6091)

| Ch | Chapter | Definitions | Formulae | Units | Total |
|---|---|---|---|---|---|
| 1 | Physical Quantities, Units and Measurement | 2/1/1/0/0 = 4 | 0 | 6/0/9/0 = 15 | 19 |
| 2 | Kinematics | 3/2/0/0/0 = 5 | 2/0/2/0 = 4 | 0/2/0/0 = 2 | 11 |
| 3 | Dynamics | 2/4/5/1/1 = 13 | 2/1/0/1 = 4 | 2/1/0/2 = 5 | 22 |
| 4 | Turning Effects of Forces | 1/1/2/1/0 = 5 | 1/0/1/0 = 2 | 1/0/0/0 = 1 | 8 |
| 5 | Pressure | 2/0/1/2/0 = 5 | 2/1/2/1 = 6 | 1/1/0/1 = 3 | 14 |
| 6 | Energy | 4/2/3/0/0 = 9 | 4/1/3/2 = 10 | 3/1/0/2 = 6 | 25 |
| 7 | Kinetic Particle Model of Matter | 0/4/2/0/0 = 6 | 0 | 0 | 6 |
| 8 | Thermal Processes | 1/2/3/0/0 = 6 | 0 | 0 | 6 |
| 9 | Thermal Properties of Matter | 0/4/2/1/1 = 8 | 0/3/1/0 = 4 | 0/4/0/0 = 4 | 16 |
| 10 | General Properties of Waves | 4/8/1/0/0 = 13 | 2/1/1/0 = 4 | 1/2/0/1 = 4 | 21 |
| 11 | Electromagnetic Spectrum | 0/2/1/0/0 = 3 | 0 | 0 | 3 |
| 12 | Light | 1/5/3/0/0 = 9 | 0/3/0/0 = 3 | 0/2/0/0 = 2 | 14 |
| 13 | Static Electricity | 1/3/0/1/0 = 5 | 0 | 0 | 5 |
| 14 | Current of Electricity | 2/4/2/1/0 = 9 | 2/1/1/0 = 4 | 4/0/0/3 = 7 | 20 |
| 15 | D.C. Circuits | 4/2/1/0/0 = 7 | 1/1/0/0 = 2 | 0 | 9 |
| 16 | Practical Electricity | 0/6/3/0/0 = 9 | 2/1/1/3 = 7 | 0/1/0/1 = 2 | 18 |
| 17 | Magnetism | 0/3/1/0/0 = 4 | 0 | 0 | 4 |
| 18 | Electromagnetism | 0/2/2/1/0 = 5 | 0 | 0 | 5 |
| 19 | Electromagnetic Induction | 0/1/3/2/0 = 6 | 0/2/0/0 = 2 | 0 | 8 |
| 20 | Radioactivity | 2/9/4/0/0 = 15 | 0 | 0/2/0/0 = 2 | 17 |
| | **Total** | **146** | **52** | **53** | **251** |

### Science (Physics) (5086)

| Ch | Chapter | Definitions | Formulae | Units | Total |
|---|---|---|---|---|---|
| 1 | Physical Quantities, Units and Measurement | 2/1/1/0/0 = 4 | 0 | 6/0/9/0 = 15 | 19 |
| 2 | Kinematics | 3/2/0/0/0 = 5 | 2/0/2/0 = 4 | 0/2/0/0 = 2 | 11 |
| 3 | Force and Pressure | 4/2/1/0/1 = 8 | 3/1/2/1 = 7 | 3/2/0/3 = 8 | 23 |
| 4 | Dynamics | 0/1/3/1/0 = 5 | 1/0/0/0 = 1 | 0 | 6 |
| 5 | Turning Effects of Forces | 1/1/2/0/0 = 4 | 1/0/1/0 = 2 | 1/0/0/0 = 1 | 7 |
| 6 | Energy | 4/1/2/0/0 = 7 | 4/0/3/2 = 9 | 3/0/0/2 = 5 | 21 |
| 7 | Kinetic Particle Model of Matter | 0/5/0/1/0 = 6 | 0 | 0 | 6 |
| 8 | Thermal Processes | 1/2/3/0/0 = 6 | 0 | 0 | 6 |
| 9 | General Properties of Waves | 4/7/1/0/0 = 12 | 2/1/1/0 = 4 | 1/2/0/1 = 4 | 20 |
| 10 | Electromagnetic Spectrum | 0/2/1/0/0 = 3 | 0 | 0 | 3 |
| 11 | Light | 1/5/1/0/0 = 7 | 0/2/0/0 = 2 | 0/2/0/0 = 2 | 11 |
| 12 | Electric Charge and Current of Electricity | 3/4/0/0/0 = 7 | 2/1/1/0 = 4 | 4/0/0/3 = 7 | 18 |
| 13 | D.C. Circuits | 4/0/0/0/0 = 4 | 1/1/0/0 = 2 | 0 | 6 |
| 14 | Practical Electricity | 0/6/3/0/0 = 9 | 2/1/1/3 = 7 | 0/1/0/1 = 2 | 18 |
| 15 | Magnetism and Electromagnetism | 0/5/3/0/0 = 8 | 0 | 0 | 8 |
| 16 | Radioactivity | 2/9/2/0/0 = 13 | 0 | 0/2/0/0 = 2 | 15 |
| | **Total** | **108** | **42** | **48** | **198** |

Where a chapter has fewer than 3 questions at the student's level, the engine borrows from the adjacent levels, so every
chapter is always playable. 6091-only items (specific heat/latent heat, critical angle, electric field, e.m. induction,
transformers, efficiency, hydraulic press, fission/fusion …) are tagged `syllabi=PURE` and never shown to 5086 students.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

Default local teacher password is `physics`. Set `TEACHER_PASSWORD` as an environment variable or in `.streamlit/secrets.toml` to change it.

## Deploy on Streamlit Community Cloud

1. share.streamlit.io → **Create app** → repo `ian1eong2005-a11y/physics-defs-checker`, branch `main`, main file `app.py`.
2. Advanced settings → **Secrets**:
   ```toml
   TEACHER_PASSWORD = "choose-something"
   ```
3. Deploy. Share the `*.streamlit.app` URL (or a QR code) with students. Every push to `main` redeploys; live data is cleared.

## Tests

```bash
python -m pytest -q
```

`tests/test_content.py`: every definition's model answer passes its own marking, every declared sample passes / fails as
stated, every formula's accepted forms are normalised and its known wrong forms are not accepted, three hints each, both
syllabuses have content in every chapter. `tests/test_engine.py`: level rules, deck-style selection, mixed mode.
`tests/test_marker.py`: the meaning-based marker. `tests/test_app.py`: end-to-end through Streamlit's AppTest (login with
syllabus, definition flow, tutor, retry, level up, formula flow, units + mixed mode, dashboard).

## Adding a question (one question = one function call)

**Definition** – in `trainer/content/defs_*.py`:

```python
definition("d_kin_speed", "kin", 1, "2a",                      # id, topic key (config.TOPICS), level, syllabus LO
           stem="State what is meant by **speed**.",
           points=[P("distance travelled per unit time", ["distance travelled per unit time", "distance per unit time", "distance / time"])],
           pitfalls=[PF(["displacement per unit time"], "That is VELOCITY. Speed uses distance.")],
           model_answer="Speed is the distance travelled per unit time.",
           hints=["...", "...", "..."], keywords="distance travelled per unit time",
           syllabi=BOTH,                                           # or PURE for 6091-only
           sample_pass=["Distance travelled per unit time"], sample_fail=["How fast something is going"])
```

**Formula** – in `trainer/content/formulae.py` (`unit(...)` in `units.py` is the same shape):

```python
formula("f_newton2", "newton", 1, "4c", "Write the formula relating **resultant force**, mass and acceleration.",
        forms=["F = ma", "a = F/m"],                                  # accepted, any spelling; normalised automatically
        answer="F = ma", symbols="F is the resultant (net) force",      # shown as the model answer
        wrongs={"F = m/a": "Multiply: F = m × a."},                     # known slips -> message
        hints=["...", "...", "..."], keywords="mass, acceleration",
        sample_pass=["F = ma", "a = F/m"], sample_fail=["F = m/a"])
```

Run `python -m pytest -q` afterwards; the tests check the samples against the marker.

## Classes

Edit the two class lines at the top of `trainer/config.py` (`CLASSES = {"Sec 4": [...], "Sec 3": [...]}`).

## Layout

```
app.py                      entry point: login (name, class, syllabus), routing
trainer/config.py           classes, syllabi, topic -> chapter mapping, chapter names, level names, rules (5 up / 3 down)
trainer/engine.py           adaptive rules + deck-style selection (pure Python)
trainer/store.py            in-memory live store shared by all sessions
trainer/marker.py           meaning-based marker for definitions
trainer/formula.py          normaliser + checker for formulae and units
trainer/content/base.py     definition(), formula(), unit() registration helpers
trainer/content/defs_*.py   146 definitions by section
trainer/content/formulae.py 52 formulae (L1 core, L2 rest, L3 rearranged, L4 derived)
trainer/content/units.py    53 units, prefixes and equivalences
trainer/ui_student.py       student screen + tutor panel
trainer/ui_teacher.py       live dashboard
tests/                      pytest
```
