"""Rule-based marker for short written answers. No LLM: meaning is recognised through marking points, each with
several alternative phrasings; words are matched after light stemming with spelling tolerance, and the words of a phrase may
appear in any order within a short window. Pitfalls (common wrong ideas) are matched in order within a tight window.

    points = [Point("direction: hot to cold", ["hot to cold", "higher temperature to lower temperature", "hotter to colder"])]
    result = mark("Energy goes from the hoter object to the colder one", points)
    result.passed, result.hit, result.missed
"""
import re
from dataclasses import dataclass, field
from difflib import SequenceMatcher
from typing import List, Optional, Sequence

STOP = set("the a an of to and is are in on at by it its this that as be from with for than so which who what there their "
           "they them then will would can could has have had was were been being do does did also very "
           "you your my his her our".split())
# 'more', 'less', 'not', 'no' are deliberately NOT stop words: comparatives and negations carry physics meaning.

NEGATIONS = {"not", "never", "no", "cannot", "without", "isn", "aren", "doesn", "don", "wasn", "weren", "won", "nor", "neither"}

SUPERSCRIPTS = str.maketrans("⁰¹²³⁴⁵⁶⁷⁸⁹⁻₀₁₂₃₄₅₆₇₈₉", "0123456789-0123456789")   # also subscripts: R₁ -> r1

WINDOW = 9          # max token span for the words of one phrase (order-free)
PITFALL_WINDOW = 4  # tight, ordered


@dataclass
class Point:
    label: str                       # shown to the student when hit / missed, e.g. "says energy goes from hot to cold"
    any_of: Sequence[str]            # alternative phrasings; one matching phrase scores the point
    required: bool = True
    ordered: bool = False            # True: phrase words must appear in order (for "P is microwaves"-type pairings)
    window: Optional[int] = None     # max token span for a phrase (default WINDOW)


@dataclass
class Pitfall:
    phrases: Sequence[str]           # ordered phrases, e.g. "cold to hot"
    message: str


@dataclass
class MarkResult:
    hit: List[str]
    missed: List[str]
    pitfalls: List[str]
    needed: int
    passed: bool
    too_short: bool = False

    @property
    def score(self) -> str:
        return f"{len(self.hit)} / {len(self.hit) + len(self.missed)}"


# ------------------------------------------------------------------ text normalisation
def _stem(w: str) -> str:
    if len(w) <= 3:
        return w
    for suf in ("ingly", "ing", "edly", "ed", "ies", "es", "ly", "s"):
        if w.endswith(suf) and len(w) - len(suf) >= 3:
            if suf == "es" and not (w[-3] in "sxz" or w.endswith(("ches", "shes"))):
                continue                      # 'bones', 'waves' -> strip only the 's'
            w = w[: -len(suf)]
            break
    if w.endswith("e") and len(w) > 4:
        w = w[:-1]
    return w


def tokens(text: str) -> List[str]:
    """Lower-case word tokens. Superscripts become digits ('m/s²' -> 'm/s2'), arithmetic operators become their own tokens
    ('÷' and a digit-digit '/' -> '/', '×' and 'x' between numbers -> '*', '−' -> '-'), so 'm/s' and 'm/s²' differ and
    '12 × 4' does not match '12 ÷ 4'."""
    text = text.lower().replace("'", " ").replace("’", " ")
    text = text.translate(SUPERSCRIPTS).replace("^", "")   # m/s^2 -> m/s2, 10⁷ and 10^7 -> 107, 10⁻³ -> 10-3
    text = re.sub(r"\b(c\.\s?g\.?|cg|c of g)(?![a-z])", " centre of gravity ", text)   # common abbreviation
    text = re.sub(r"\bp\.\s?d\.?(?![a-z])", " pd ", text)                                 # p.d. -> pd
    text = re.sub(r"\be\.\s?m\.\s?f\.?(?![a-z])", " emf ", text)                        # e.m.f. -> emf
    text = re.sub(r"\b([ad])\.c\.?(?![a-z])", r" \1c ", text)                               # a.c. / d.c.
    text = re.sub(r"\bcent(er|re)s?\b", "centre", text)
    text = text.replace("÷", " / ").replace("×", " * ").replace("−", " - ").replace("=", " = ")
    text = re.sub(r"(?<=\d)\s*/\s*(?=\d)", " / ", text)          # 12/4 -> 12 / 4   (m/s stays one token)
    text = re.sub(r"(?<=\d)\s*x\s*(?=\d)", " * ", text)          # 12x4, 12 x 4 -> 12 * 4
    text = text.replace("λ", " lambda ")                         # wavelength symbol
    text = text.replace("ohms", "ω").replace("ohm", "ω")        # '2 ohm' and '2 Ω' read the same, and differ from '2 A'
    text = re.sub(r"[;,:!?]", " ¦ ", text)                       # clause boundaries
    text = re.sub(r"\.(?=\s|$)", " ¦ ", text)                    # full stops (not decimal points)
    text = re.sub(r"(?<=[a-z])(?<!non)-(?=[a-z])", " ", text)  # "high-resistance" reads as "high resistance"; "non-contact" stays one word
    text = re.sub(r"[^a-z0-9°/\-*=.ω¦]+", " ", text)
    out = []
    for t in text.split():
        t = t.strip(".")
        if t:
            out.append(t)
    return out


def _edits(a: str, b: str) -> int:
    """Levenshtein distance (words are short, so the plain DP is fine)."""
    if a == b:
        return 0
    prev = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        cur = [i]
        for j, cb in enumerate(b, 1):
            cur.append(min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + (ca != cb)))
        prev = cur
    return prev[-1]


def _word_match(a: str, b: str, exact: bool = False) -> bool:
    """a: answer token, b: phrase word (both raw). Exact, stem-equal, or (unless exact) one spelling slip.
    One edit keeps 'hoter'/'hotter' and 'radiaton'/'radiation' but separates 'conduction'/'convection' and 'dense'/'denser'."""
    if a == b:
        return True
    sa, sb = _stem(a), _stem(b)
    if sa == sb or sa == b or a == sb:        # 'sunbeds' -> 'sunbed' matches the phrase word 'sunbed' even though it stems to 'sunb'
        return True
    if exact or len(sa) < 5 or len(sb) < 5:
        return False
    if sa[0] != sb[0]:
        return False
    return _edits(sa, sb) <= 1 or (min(len(sa), len(sb)) >= 11 and _edits(sa, sb) <= 2)


def _positions(ans: List[str], word: str, exact: bool = False) -> List[int]:
    return [i for i, t in enumerate(ans) if _word_match(t, word, exact)]


def phrase_match(ans: List[str], phrase: str, ordered: bool = False, window: int = WINDOW, exact: bool = False) -> bool:
    words = tokens(phrase) if exact else [w for w in tokens(phrase) if w not in STOP]   # pitfalls keep every word ('more dense')
    if not words:
        return False
    if exact:
        window = max(window, len(words))           # a long pitfall phrase may span its own length (one extra word allowed), in order
    negated_phrase = any(w in NEGATIONS for w in words)
    if negated_phrase and not ordered:
        ordered, window = True, min(window, 6)        # 'not accurate', 'cannot be formed on a screen': in order, close together
    pos = [_positions(ans, w, exact) for w in words]
    if any(not p for p in pos):
        return False

    def negated_before(i):
        # a positive phrase does not count when the answer negates it: 'not precise', 'is never destroyed'
        # (a negation in an earlier clause does not count: '...does not change; potential energy rises')
        if negated_phrase:
            return False
        before = ans[max(0, i - 2): i]
        if "¦" in before:
            before = before[before.index("¦") + 1:] if before[-1] != "¦" else []
        return any(t in NEGATIONS for t in before)

    if len(words) == 1:
        return any(not negated_before(i) for i in pos[0])
    for start in pos[0]:
        if negated_before(start):
            continue
        if ordered:
            cur = start
            ok = True
            for p in pos[1:]:
                nxt = [i for i in p if cur < i <= start + window]
                if not nxt:
                    ok = False
                    break
                cur = min(nxt)
            if ok:
                # a positive phrase that the answer negates ("energy is NOT destroyed") does not count;
                # a phrase that is itself negative ("no net transfer") is matched as written
                span = ans[max(0, start - 2): cur + 1]
                if "¦" in span[:2]:
                    span = span[span.index("¦") + 1:]
                if negated_phrase or not any(t in NEGATIONS for t in span):
                    return True
        else:
            if all(any(abs(i - start) <= window for i in p) for p in pos[1:]):
                return True
    return False


# ------------------------------------------------------------------ marking
def mark(answer: str, points: Sequence[Point], pitfalls: Sequence[Pitfall] = (), min_points: Optional[int] = None) -> MarkResult:
    ans = tokens(answer)
    hit, missed = [], []
    for p in points:
        ok = any(phrase_match(ans, ph, ordered=p.ordered, window=p.window or WINDOW) for ph in p.any_of)
        (hit if ok else missed).append(p.label)
    found = [pf.message for pf in pitfalls if any(phrase_match(ans, ph, ordered=True, window=PITFALL_WINDOW, exact=True) for ph in pf.phrases)]
    needed = len(points) if min_points is None else min(min_points, len(points))
    too_short = len(ans) == 0 or (len(ans) < 3 and needed > 1)   # a one-word answer is fine for a 'name the process' question
    passed = (not too_short) and len(hit) >= needed and not found
    return MarkResult(hit=hit, missed=missed, pitfalls=found, needed=needed, passed=passed, too_short=too_short)
