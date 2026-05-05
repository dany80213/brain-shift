"""
Test per il modulo rules.py.

Questi test verificano che le tre funzioni pure del modulo rules
(is_even, is_vowel, compute_expected_answer) si comportino come la
specifica richiede.

Per lanciarli: pytest tests/test_rules.py
"""

import pytest

try:
    from rules import is_even, is_vowel, compute_expected_answer
except ImportError:
    is_even = None
    is_vowel = None
    compute_expected_answer = None


def test_structure_check():
    """Verifica che il file rules.py esista e contenga le funzioni attese."""
    assert is_even is not None, (
        "Non trovo 'is_even' in 'rules.py'. "
        "Controlla che il file si chiami esattamente 'rules.py' "
        "e contenga una funzione 'is_even'."
    )
    assert is_vowel is not None, "Manca la funzione 'is_vowel' in 'rules.py'."
    assert compute_expected_answer is not None, (
        "Manca la funzione 'compute_expected_answer' in 'rules.py'."
    )


# ---------- is_even ----------

def test_is_even_with_even_number():
    """Un numero pari deve dare True."""
    assert is_even(4) is True

def test_is_even_with_odd_number():
    """Un numero dispari deve dare False."""
    assert is_even(3) is False

def test_is_even_with_one():
    """1 è dispari."""
    assert is_even(1) is False

def test_is_even_with_nine():
    """9 è dispari (limite superiore del range di gioco)."""
    assert is_even(9) is False

def test_is_even_with_two():
    """2 è pari (limite inferiore dei pari nel range di gioco)."""
    assert is_even(2) is True


# ---------- is_vowel ----------

def test_is_vowel_with_vowel_A():
    """A è una vocale."""
    assert is_vowel("A") is True

def test_is_vowel_with_vowel_E():
    """E è una vocale."""
    assert is_vowel("E") is True

def test_is_vowel_with_vowel_U():
    """U è una vocale."""
    assert is_vowel("U") is True

def test_is_vowel_with_consonant_B():
    """B non è una vocale."""
    assert is_vowel("B") is False

def test_is_vowel_with_consonant_Z():
    """Z non è una vocale."""
    assert is_vowel("Z") is False

def test_is_vowel_all_vowels():
    """Tutte e cinque le vocali inglesi devono dare True."""
    for v in "AEIOU":
        assert is_vowel(v) is True, f"is_vowel('{v}') dovrebbe essere True"

def test_is_vowel_some_consonants():
    """Un campione di consonanti deve dare False."""
    for c in "BCDFGHJKLMNPQRSTVWXYZ":
        assert is_vowel(c) is False, f"is_vowel('{c}') dovrebbe essere False"


# ---------- compute_expected_answer ----------

def test_expected_top_even_number():
    """Carta TOP con numero pari: risposta attesa True."""
    assert compute_expected_answer("TOP", "B", 4) is True

def test_expected_top_odd_number():
    """Carta TOP con numero dispari: risposta attesa False."""
    assert compute_expected_answer("TOP", "A", 3) is False

def test_expected_bottom_vowel_letter():
    """Carta BOTTOM con lettera vocale: risposta attesa True."""
    assert compute_expected_answer("BOTTOM", "E", 7) is True

def test_expected_bottom_consonant_letter():
    """Carta BOTTOM con lettera consonante: risposta attesa False."""
    assert compute_expected_answer("BOTTOM", "K", 2) is False

def test_expected_top_ignores_letter():
    """Quando la carta è TOP, il calcolo dipende solo dal numero, non dalla lettera."""
    # A è vocale, ma con TOP conta solo il numero 3 (dispari)
    assert compute_expected_answer("TOP", "A", 3) is False
    # Z è consonante, ma con TOP conta solo il numero 6 (pari)
    assert compute_expected_answer("TOP", "Z", 6) is True

def test_expected_bottom_ignores_number():
    """Quando la carta è BOTTOM, il calcolo dipende solo dalla lettera, non dal numero."""
    # Numero pari, ma BOTTOM: conta la consonante B
    assert compute_expected_answer("BOTTOM", "B", 4) is False
    # Numero dispari, ma BOTTOM: conta la vocale I
    assert compute_expected_answer("BOTTOM", "I", 7) is True
