"""
Test per il modulo scoring.py (versione base lineare).

La firma attesa della funzione è:

    def apply_answer(score: int, is_correct: bool) -> int:
        ...

Comportamento richiesto per la versione base:
- risposta corretta: score viene incrementato di 10
- risposta errata: score resta uguale OPPURE viene decrementato di 5
  (potete scegliere, ma dovete essere coerenti)

I test accettano entrambe le policy per la risposta errata: verificano
solo che il punteggio sia uguale o inferiore, e mai superiore, a quello
precedente.

Per lanciarli: pytest tests/test_scoring_base.py
"""

import pytest

try:
    from scoring import apply_answer
except ImportError:
    apply_answer = None


def test_structure_check():
    """Verifica che scoring.py esista e contenga apply_answer."""
    assert apply_answer is not None, (
        "Non trovo 'apply_answer' in 'scoring.py'. "
        "Controlla che il file si chiami esattamente 'scoring.py' "
        "e contenga una funzione 'apply_answer(score, is_correct)'."
    )


def test_correct_answer_increases_score_by_10():
    """Una risposta corretta deve aggiungere esattamente 10 al punteggio."""
    assert apply_answer(0, True) == 10
    assert apply_answer(50, True) == 60
    assert apply_answer(123, True) == 133

def test_wrong_answer_does_not_increase_score():
    """Una risposta errata non deve MAI aumentare il punteggio."""
    assert apply_answer(100, False) <= 100
    assert apply_answer(0, False) <= 0
    assert apply_answer(50, False) <= 50

def test_wrong_answer_consistent_policy():
    """
    La policy per risposte errate deve essere coerente:
    o sempre 0 (score invariato), o sempre -5 (decremento fisso).
    """
    delta_1 = 50 - apply_answer(50, False)
    delta_2 = 200 - apply_answer(200, False)
    assert delta_1 == delta_2, (
        f"La policy per la risposta errata non è coerente: "
        f"da 50 hai tolto {delta_1}, da 200 hai tolto {delta_2}. "
        "Scegli una regola e applicala sempre."
    )

def test_correct_answer_from_negative_score():
    """Il meccanismo deve funzionare anche partendo da punteggio negativo."""
    assert apply_answer(-5, True) == 5

def test_apply_answer_is_pure():
    """
    apply_answer deve essere una funzione pura: chiamarla due volte con
    gli stessi argomenti deve restituire lo stesso risultato.
    """
    assert apply_answer(100, True) == apply_answer(100, True)
    assert apply_answer(100, False) == apply_answer(100, False)

def test_sequence_of_answers():
    """
    Una sequenza di 5 corrette partendo da 0 deve dare 50.
    (Versione base: nessun moltiplicatore, ogni corretta vale sempre 10.)
    """
    score = 0
    for _ in range(5):
        score = apply_answer(score, True)
    assert score == 50, (
        f"5 risposte corrette da 0 dovrebbero dare 50, hai ottenuto {score}. "
        "Nella versione base dello scoring NON ci deve essere moltiplicatore: "
        "il moltiplicatore è un obiettivo avanzato, su una funzione separata."
    )

def test_return_type_is_int():
    """apply_answer deve restituire un int, non un float o una stringa."""
    result = apply_answer(10, True)
    assert isinstance(result, int), (
        f"apply_answer deve restituire int, non {type(result).__name__}"
    )
