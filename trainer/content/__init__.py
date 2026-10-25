"""Question content registry. Importing the modules registers their templates."""
import importlib
import pkgutil

for _name in sorted(m.name for m in pkgutil.iter_modules(__path__)):
    if _name != "base":
        importlib.import_module(f"{__name__}.{_name}")
from .base import TEMPLATES, Question, Template  # noqa: E402


def for_syllabus(syllabus: str):
    return [t for t in TEMPLATES if syllabus in t.syllabi]


def topics_with_content(category: str, syllabus: str):
    return {t.topic for t in TEMPLATES if t.category == category and syllabus in t.syllabi}


def inventory(syllabus=None):
    """{(category, topic): {level: count}}"""
    out = {}
    for t in TEMPLATES:
        if syllabus and syllabus not in t.syllabi:
            continue
        out.setdefault((t.category, t.topic), {}).setdefault(t.level, 0)
        out[(t.category, t.topic)][t.level] += 1
    return out


__all__ = ["TEMPLATES", "Question", "Template", "for_syllabus", "topics_with_content", "inventory"]
