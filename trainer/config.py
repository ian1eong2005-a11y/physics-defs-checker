"""Constants for the Physics definitions and formulae checker. Change class lists and rules here only."""

APP_TITLE = "Physics Definitions & Formulae Checker"
SCHOOL = "Queenstown Secondary School"

# Login dropdown, grouped by level. ADD OR REMOVE CLASSES ON THE NEXT TWO LINES ONLY.
CLASSES = {
    "Sec 4": ["4SG1", "4SG2", "4SG3", "4SG4", "4SG5", "4SG6", "4SG7", "4SG8"],
    "Sec 3": ["3SG2", "3SG3", "3SG4", "3SG8"],
}
CLASS_LIST = [c for group in CLASSES.values() for c in group]

# Students pick one of these at login. Every question is tagged with the syllabuses it belongs to.
SYLLABI = {
    "6091": "Pure Physics (6091)",
    "5086": "Science (Physics) (5086)",
}

# Fine-grained topic keys -> chapter number in each syllabus (None = not in that syllabus).
# A topic is the unit every question is tagged with; the chapter lists below are built from this table.
TOPICS = {
    "meas":         (1, 1),
    "kin":          (2, 2),
    "mwg":          (3, 3),     # types of forces, mass, weight, gravitational field
    "newton":       (3, 4),     # Newton's laws, F = ma, friction, inertia, terminal velocity
    "moments":      (4, 5),
    "pressure":     (5, 3),     # pressure, density, hydraulic press, liquid column
    "energy":       (6, 6),
    "kpm":          (7, 7),
    "thermal_proc": (8, 8),
    "internal":     (9, 7),     # internal energy, melting / boiling at constant temperature
    "thermal_props": (9, None),  # heat capacity, specific heat capacity, latent heat (6091 only)
    "waves":        (10, 9),
    "em":           (11, 10),
    "light":        (12, 11),
    "static":       (13, 12),
    "current":      (14, 12),
    "dc":           (15, 13),
    "practical":    (16, 14),
    "magnetism":    (17, 15),
    "electromag":   (18, 15),
    "emi":          (19, None),
    "radio":        (20, 16),
}
_SYL_INDEX = {"6091": 0, "5086": 1}

CHAPTERS = {
    "6091": {
        1: "Physical Quantities, Units and Measurement", 2: "Kinematics", 3: "Dynamics", 4: "Turning Effects of Forces",
        5: "Pressure", 6: "Energy", 7: "Kinetic Particle Model of Matter", 8: "Thermal Processes",
        9: "Thermal Properties of Matter", 10: "General Properties of Waves", 11: "Electromagnetic Spectrum", 12: "Light",
        13: "Static Electricity", 14: "Current of Electricity", 15: "D.C. Circuits", 16: "Practical Electricity",
        17: "Magnetism", 18: "Electromagnetism", 19: "Electromagnetic Induction", 20: "Radioactivity",
    },
    "5086": {
        1: "Physical Quantities, Units and Measurement", 2: "Kinematics", 3: "Force and Pressure", 4: "Dynamics",
        5: "Turning Effects of Forces", 6: "Energy", 7: "Kinetic Particle Model of Matter", 8: "Thermal Processes",
        9: "General Properties of Waves", 10: "Electromagnetic Spectrum", 11: "Light",
        12: "Electric Charge and Current of Electricity", 13: "D.C. Circuits", 14: "Practical Electricity",
        15: "Magnetism and Electromagnetism", 16: "Radioactivity",
    },
}


def chapter_of(topic: str, syllabus: str):
    return TOPICS[topic][_SYL_INDEX[syllabus]]


def topics_in(chapter: int, syllabus: str):
    return [t for t, chs in TOPICS.items() if chs[_SYL_INDEX[syllabus]] == chapter]


CATEGORIES = {
    "defs": "Definitions",
    "formula": "Formulae",
    "units": "Units & prefixes",
}

LEVEL_NAMES = {
    "defs": {
        1: "L1 - the core quantities (speed, density, pressure, moment, work, power ...)",
        2: "L2 - other defined terms and 'state that' facts",
        3: "L3 - laws, principles and conditions",
        4: "L4 - the ones examiners say students fumble",
        5: "L5 - distinguish between two terms",
    },
    "formula": {
        1: "L1 - the core formulae",
        2: "L2 - the rest of the syllabus formulae",
        3: "L3 - rearranged: make another quantity the subject",
        4: "L4 - combined and derived formulae",
    },
    "units": {
        1: "L1 - base units and common derived units",
        2: "L2 - compound units and alternatives",
        3: "L3 - prefixes",
        4: "L4 - unit equivalences",
    },
}

# Adaptive rules (same as the G3 Physics trainer, confirmed by the teacher)
UP_STREAK = 5          # correct in a row at a level -> level + 1
DOWN_STREAK = 3        # wrong in a row at a level -> level - 1
MIN_LEVEL, MAX_LEVEL = 1, 5
START_LEVEL = 1
HISTORY_LEN = 1000

ONLINE_SECONDS = 120
DASHBOARD_REFRESH_S = 5

DEFAULT_TEACHER_PASSWORD = "physics"   # used only when no TEACHER_PASSWORD secret / env var is set
