def is_even(number: int) -> bool:
    return number % 2 == 0

def is_vowel(letter: str) -> bool:
    return letter in ("A", "E", "I", "O", "U")

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    if position == "TOP":
        return is_even(number)
    elif position == "BOTTOM":
        return is_vowel(letter)
    return False
