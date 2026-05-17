import string
from dataclasses import dataclass
from model.rules import compute_expected_answer


MAX_STREAK     = 3
BALANCE_WINDOW = 10

_EVENS     = [2, 4, 6, 8]
_ODDS      = [1, 3, 5, 7, 9]
_VOWELS    = list("AEIOU")
_CONSONANTS = [c for c in string.ascii_uppercase if c not in "AEIOU"]


@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool


class TrialGenerator:
    def __init__(self, rng):
        self.rng = rng
        self._positions = []
        self._answers   = []

    def generate(self) -> Trial:
        position = self._pick_position()
        want_yes = self._target_answer()
        letter, number = self._pick_card(position, want_yes)
        answer = compute_expected_answer(position, letter, number)
        self._positions.append(position)
        self._answers.append(answer)
        return Trial(position=position, letter=letter, number=number, expected_answer=answer)

    def _pick_position(self) -> str:
        if (len(self._positions) >= MAX_STREAK
                and len(set(self._positions[-MAX_STREAK:])) == 1):
            options = [p for p in ("TOP", "BOTTOM") if p != self._positions[-1]]
        else:
            options = ["TOP", "BOTTOM"]
        return self.rng.choice(options)

    def _target_answer(self):
        if len(self._answers) < BALANCE_WINDOW:
            return None
        yes_ratio = sum(self._answers[-BALANCE_WINDOW:]) / BALANCE_WINDOW
        if yes_ratio > 0.65:
            return False
        if yes_ratio < 0.35:
            return True
        return None

    def _pick_card(self, position: str, want_yes):
        if position == "TOP":
            if want_yes is True:
                number = self.rng.choice(_EVENS)
            elif want_yes is False:
                number = self.rng.choice(_ODDS)
            else:
                number = self.rng.randint(1, 9)
            letter = self.rng.choice(string.ascii_uppercase)
        else:
            if want_yes is True:
                letter = self.rng.choice(_VOWELS)
            elif want_yes is False:
                letter = self.rng.choice(_CONSONANTS)
            else:
                letter = self.rng.choice(string.ascii_uppercase)
            number = self.rng.randint(1, 9)
        return letter, number
