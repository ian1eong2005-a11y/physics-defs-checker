"""Formula and unit checker. No algebra engine: an answer is accepted when, after normalisation, it equals one of the
template's accepted forms (either way round the equals sign). Normalisation makes 'F = m × a', 'f=m*a', 'F = m a' and
'F=ma' identical, reads ², ½, ρ, λ, θ, Δ and subscripts, and ignores spaces and multiplication signs."""
import re
import unicodedata
from dataclasses import dataclass
from typing import Dict, List, Optional

_SUB = str.maketrans("₀₁₂₃₄₅₆₇₈₉", "0123456789")
_GREEK = {"ρ": "rho", "λ": "lambda", "θ": "theta", "δ": "delta", "ω": "omega", "μ": "u", "π": "pi",
          "°": "deg", "º": "deg", "ε": "e", "η": "eff"}
_WORDS = [  # spoken forms students type -> symbols (applied after lower-casing, before spaces are removed)
    (r"\bsquared\b", "^2"), (r"\bcubed\b", "^3"), (r"\bdivided by\b", "/"), (r"\bover\b", "/"), (r"\bper\b", "/"),
    (r"\btimes\b", "*"), (r"\bmultiplied by\b", "*"), (r"\bequals\b", "="), (r"\bis equal to\b", "="),
    (r"\bhalf\b", "1/2"), (r"\bchange in\b", "delta"), (r"\bsine\b", "sin"), (r"\bsin\s*\(\s*([a-z0-9]+)\s*\)", r"sin\1"),
    (r"\bwavelength\b", "lambda"), (r"\bdensity\b", "rho"), (r"\bohms?\b", "ohm"), (r"\bdegrees?\b", "deg"),
    (r"\bcelsius\b", "c"), (r"\bkelvin\b", "k"), (r"\bsec(ond)?s?\b", "s"), (r"\bmetres?\b", "m"), (r"\bmeters?\b", "m"),
    (r"\bkilograms?\b", "kg"), (r"\bnewtons?\b", "n"), (r"\bjoules?\b", "j"), (r"\bwatts?\b", "w"),
    (r"\bpascals?\b", "pa"), (r"\bhertz\b", "hz"), (r"\bcoulombs?\b", "c"), (r"\bvolts?\b", "v"), (r"\bamperes?\b", "a"),
    (r"\bamps?\b", "a"), (r"\bbecquerels?\b", "bq"), (r"\bmoles?\b", "mol"), (r"\bkilowatt[- ]hours?\b", "kwh"),
]


def normalise(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").strip().lower()
    s = s.translate(_SUB)
    for k, v in _GREEK.items():
        s = s.replace(k.lower(), v)
    s = (s.replace("×", "*").replace("·", "*").replace("⋅", "*").replace("∙", "*").replace("÷", "/")
          .replace("−", "-").replace("–", "-").replace("—", "-").replace("²", "^2").replace("³", "^3")
          .replace("½", "1/2").replace("¼", "1/4").replace("⁄", "/").replace("√", "sqrt"))
    for pat, rep in _WORDS:
        s = re.sub(pat, rep, s)
    s = re.sub(r"(?<=\s)x(?=\s)", "*", s)          # 'm x a' -> multiplication; 'x' glued to letters stays a symbol
    s = re.sub(r"(?<=\d)x(?=\d)", "*", s)          # 10x3
    s = re.sub(r"\s+", "", s)
    s = s.replace("*", "").replace("^", "")        # implicit multiplication; v^2 == v2 == v²
    s = s.replace("0.5", "1/2")
    s = s.replace("(", "").replace(")", "")        # F/(A) == F/A for the simple forms in this syllabus
    s = s.strip(".;,")
    s = re.sub(r"^(formula|answer|unit)[:=]", "", s)
    return s


def _sides(n: str) -> List[str]:
    if "=" in n:
        parts = n.split("=")
        if len(parts) == 2:
            return [n, f"{parts[1]}={parts[0]}"]
    return [n]


@dataclass
class FormResult:
    passed: bool
    message: Optional[str] = None   # specific message for a known wrong form


def check(answer: str, forms: List[str], wrongs: Optional[Dict[str, str]] = None) -> FormResult:
    n = normalise(answer)
    cands = _sides(n)
    if any(c in forms for c in cands):
        return FormResult(True)
    wrongs = wrongs or {}
    for c in cands:
        if c in wrongs:
            return FormResult(False, wrongs[c])
    if "=" not in n:   # a bare right-hand side, e.g. 'ma' for F = ma
        rhs = {f.split("=", 1)[1] for f in forms if "=" in f}
        if n in rhs:
            return FormResult(False, "That is the right-hand side only. Write the whole equation, with the quantity you are asked for on the left and an equals sign.")
    return FormResult(False, None)
