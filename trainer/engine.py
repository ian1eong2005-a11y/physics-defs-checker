"""Adaptive rules. Pure Python, no Streamlit, fully covered by tests/test_engine.py.

Per student, per category (defs / formula / units):
  * 5 correct in a row at a level -> level + 1 (max 5); both streaks reset.
  * 3 wrong in a row at a level  -> level - 1 (min 1); both streaks reset.
  * A correct answer resets the wrong streak; a wrong answer resets the correct streak.
  * Only the FIRST attempt at a question counts. Retries never change streaks or accuracy.
  * Level 1 in every category: a wrong question is re-served until the student gets it right.
  * level=None in select_template mixes every level of the chosen chapters (the 'run through the chapter' mode).
"""
from dataclasses import dataclass, field
from typing import Iterable, Optional

from .config import DOWN_STREAK, MAX_LEVEL, MIN_LEVEL, START_LEVEL, UP_STREAK


@dataclass
class CatState:
    level: int = START_LEVEL
    correct_streak: int = 0
    wrong_streak: int = 0
    attempted: int = 0      # first attempts only
    correct: int = 0        # first attempts answered correctly
    best_level: int = START_LEVEL

    @property
    def accuracy(self) -> Optional[float]:
        return None if self.attempted == 0 else self.correct / self.attempted


def apply_first_attempt(state: CatState, correct: bool) -> Optional[str]:
    """Update streaks and level for a first attempt. Returns 'up', 'down' or None."""
    state.attempted += 1
    if correct:
        state.correct += 1
        state.correct_streak += 1
        state.wrong_streak = 0
        if state.correct_streak >= UP_STREAK and state.level < MAX_LEVEL:
            state.level += 1
            state.best_level = max(state.best_level, state.level)
            state.correct_streak = 0
            state.wrong_streak = 0
            return "up"
        return None
    state.wrong_streak += 1
    state.correct_streak = 0
    if state.wrong_streak >= DOWN_STREAK:
        state.wrong_streak = 0
        if state.level > MIN_LEVEL:
            state.level -= 1
            state.correct_streak = 0
            return "down"
    return None


def apply_retry(state: CatState, correct: bool) -> None:
    """A retry of the same question: never touches streaks, level or accuracy."""
    return None


def repeat_until_correct(category: str, level: int) -> bool:
    """Teacher rule: level-1 questions come back until answered correctly."""
    return level == 1


def levels_available(templates: Iterable, category: str) -> list:
    return sorted({t.level for t in templates if t.category == category})


def select_template(templates: Iterable, category: str, level: Optional[int], chapters: Iterable, recent_ids: Iterable[str], rng):
    """Pick a template at the student's level from the chosen chapters, like dealing from a shuffled deck:
    a question the student has not been served yet is always preferred, so nothing repeats until the whole pool has been seen.
    Once every question in the pool has been seen, pick at random from the least recently seen half (never the one just served).
    Fewer than 3 candidates at the level -> borrow from the adjacent levels. Nothing nearby -> nearest level that has content.
    `recent_ids` is the student's served-id history for this category, oldest first.
    `chapters` holds topic keys (strings); level=None pools every level."""
    chapters = set(chapters)
    last_seen = {tid: i for i, tid in enumerate(recent_ids)}      # later index = seen more recently
    pool_all = [t for t in templates if t.category == category and t.chapter in chapters]
    if not pool_all:
        pool_all = [t for t in templates if t.category == category]
    if not pool_all:
        raise ValueError(f"no templates for category {category!r}")

    def at(lv):
        return [t for t in pool_all if t.level == lv]

    if level is None:
        pool = list(pool_all)
    else:
        pool = at(level)
        if len(pool) < 3:
            pool = pool + at(level + 1) + at(level - 1)
        if not pool:
            nearest = sorted({t.level for t in pool_all}, key=lambda lv: (abs(lv - level), -lv))[0]
            pool = at(nearest)
    unseen = [t for t in pool if t.id not in last_seen]
    if unseen:
        return rng.choice(unseen)
    oldest_first = sorted(pool, key=lambda t: last_seen[t.id])
    return rng.choice(oldest_first[:max(1, len(oldest_first) // 2)])
