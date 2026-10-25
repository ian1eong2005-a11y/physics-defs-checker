"""Shared building blocks for question templates: definitions (marked by meaning), formulae and units (checked by form)."""
from dataclasses import dataclass
from typing import Callable, Dict, FrozenSet, List, Optional

from ..formula import normalise

BOTH = frozenset({"6091", "5086"})
PURE = frozenset({"6091"})
COMBINED = frozenset({"5086"})


@dataclass
class Question:
    template_id: str
    category: str              # defs | formula | units
    topic: str                 # key in config.TOPICS
    level: int
    seed: int
    stem: str                  # markdown
    working: List[str]         # model answer lines shown after the attempt
    hints: List[str]           # three hints, never the answer
    formula: Optional[str]     # 'key words' shown on request by the tutor
    lo: str = ""
    kind: str = "written"      # written | formula
    syllabi: FrozenSet[str] = BOTH
    # written (definitions)
    points: Optional[list] = None
    pitfalls: Optional[list] = None
    model_answer: Optional[str] = None
    min_points: Optional[int] = None
    # formula / units
    forms: Optional[List[str]] = None            # accepted answers, normalised
    wrongs: Optional[Dict[str, str]] = None      # normalised wrong answer -> message
    samples: Optional[tuple] = None              # (answers that must pass, answers that must fail) for the tests
    key: str = ""

    @property
    def chapter(self):
        return self.topic


@dataclass
class Template:
    id: str
    category: str
    topic: str
    level: int
    lo: str
    syllabi: FrozenSet[str]
    make: Callable[[int], Question]

    @property
    def chapter(self):
        return self.topic


TEMPLATES: List[Template] = []
_IDS = set()


def _register(t: Template):
    if t.id in _IDS:
        raise ValueError(f"duplicate template id {t.id}")
    _IDS.add(t.id)
    TEMPLATES.append(t)


def definition(id: str, topic: str, level: int, lo: str, stem: str, points, model_answer: str, hints, keywords: str,
               pitfalls=(), min_points: Optional[int] = None, syllabi: FrozenSet[str] = BOTH,
               sample_pass=(), sample_fail=()):
    """Register a definition / statement question (fixed text; marked by trainer.marker)."""
    hints = list(hints)
    assert len(hints) == 3, id

    def make(seed: int) -> Question:
        return Question(template_id=id, category="defs", topic=topic, level=level, seed=seed, lo=lo, stem=stem,
                        working=[f"**Model answer:** {model_answer}"], hints=hints, formula=keywords, kind="written",
                        syllabi=syllabi, points=list(points), pitfalls=list(pitfalls), model_answer=model_answer,
                        min_points=min_points, samples=(list(sample_pass), list(sample_fail)))
    _register(Template(id=id, category="defs", topic=topic, level=level, lo=lo, syllabi=syllabi, make=make))
    return make


def formula(id: str, topic: str, level: int, lo: str, stem: str, forms, answer: str, symbols: str, hints, keywords: str,
            wrongs: Optional[Dict[str, str]] = None, syllabi: FrozenSet[str] = BOTH, category: str = "formula",
            sample_pass=(), sample_fail=()):
    """Register a formula or unit question. `forms`: accepted answers in any spelling (normalised on registration).
    `answer`: the model answer as shown; `symbols`: the non-obvious symbols explained, e.g. 'F is the resultant force'."""
    hints = list(hints)
    assert len(hints) == 3, id
    norm_forms = sorted({normalise(f) for f in forms})
    norm_wrongs = {normalise(k): v for k, v in (wrongs or {}).items()}
    working = [f"**{answer}**"] + ([symbols] if symbols else [])

    def make(seed: int) -> Question:
        return Question(template_id=id, category=category, topic=topic, level=level, seed=seed, lo=lo, stem=stem,
                        working=working, hints=hints, formula=keywords, kind="formula", syllabi=syllabi,
                        forms=norm_forms, wrongs=norm_wrongs, model_answer=answer,
                        samples=(list(sample_pass), list(sample_fail)))
    _register(Template(id=id, category=category, topic=topic, level=level, lo=lo, syllabi=syllabi, make=make))
    return make


def unit(id: str, topic: str, level: int, lo: str, stem: str, forms, answer: str, hints, keywords: str,
         wrongs=None, syllabi: FrozenSet[str] = BOTH, sample_pass=(), sample_fail=(), symbols: str = ""):
    return formula(id, topic, level, lo, stem, forms, answer, symbols, hints, keywords, wrongs=wrongs, syllabi=syllabi,
                   category="units", sample_pass=sample_pass, sample_fail=sample_fail)
