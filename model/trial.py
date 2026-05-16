import string
from dataclasses import dataclass
from model.rules import compute_expected_answer


@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool


def generate_trial(rng) -> Trial:
    position = rng.choice(["TOP", "BOTTOM"])
    letter = rng.choice(string.ascii_uppercase)
    number = rng.randint(1, 9)
    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=compute_expected_answer(position, letter, number),
    )
