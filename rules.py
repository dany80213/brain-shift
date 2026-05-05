def is_even(number: int) -> bool:
    if number % 2 == 0:
        return True
    else:
        return False
def is_vowel(letter: str) -> bool:
    vowels = ["A", "E", "I", "O", "U"]
    if letter in vowels:
        return True
    else:
        return False

def compute_expected_answer(position: str, letter: str, number: int) -> bool:
    if position == "TOP":
        return is_even(number)
    elif position == "BOTTOM":
        return is_vowel(letter)
    
    return False # Caso di emergenza se la posizione è sbagliata
