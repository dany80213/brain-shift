import string
from dataclasses import dataclass
from rules import compute_expected_answer

@dataclass
class Trial:
    position: str
    letter: str
    number: int
    expected_answer: bool

def generate_trial(rng) -> Trial:
    position = rng.choice(["TOP", "BOTTOM"])
    letter = rng.choice(string.ascii_uppercase)#alfabeto è ascii uppercase 
    number = rng.randint(1, 9)
    expected_answer = compute_expected_answer(position, letter, number)
    return Trial(
        position=position,
        letter=letter,
        number=number,
        expected_answer=expected_answer
    )
