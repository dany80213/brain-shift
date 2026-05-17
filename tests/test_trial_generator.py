"""
Test per TrialGenerator (model/trial.py).

Verifica due proprietà del generatore migliorato:

1. Nessuna streak di position superiore a MAX_STREAK.
   Come si verifica: si generano N trial e si controlla che non esista
   mai una finestra di MAX_STREAK+1 posizioni consecutive tutte uguali.

2. Bilanciamento YES/NO sul medio periodo (finestra BALANCE_WINDOW).
   Come si verifica: su ogni finestra scorrevole di BALANCE_WINDOW trial
   la percentuale di YES deve restare tra il 20% e l'80%.
   La soglia di intervento è 35%/65%, quindi il campo reale ammesso è
   leggermente più ampio.

Per lanciare solo questi test: pytest tests/test_trial_generator.py
"""

import random
import pytest
from model.trial import TrialGenerator, MAX_STREAK, BALANCE_WINDOW


def make_gen(seed=0):
    return TrialGenerator(random.Random(seed))


def test_no_position_streak_exceeds_max():
    gen = make_gen(42)
    trials = [gen.generate() for _ in range(200)]
    positions = [t.position for t in trials]
    for i in range(MAX_STREAK, len(positions)):
        window = positions[i - MAX_STREAK: i + 1]
        assert len(set(window)) > 1, (
            f"Streak di {MAX_STREAK + 1} posizioni identiche a partire dall'indice {i - MAX_STREAK}"
        )


def test_answer_balance_over_medium_term():
    gen = make_gen(42)
    trials = [gen.generate() for _ in range(200)]
    answers = [t.expected_answer for t in trials]
    for i in range(BALANCE_WINDOW, len(answers)):
        window = answers[i - BALANCE_WINDOW: i]
        yes_ratio = sum(window) / BALANCE_WINDOW
        assert 0.20 <= yes_ratio <= 0.80, (
            f"Squilibrio eccessivo nella finestra [{i - BALANCE_WINDOW}:{i}]: {yes_ratio:.0%} YES"
        )


def test_holds_across_multiple_seeds():
    for seed in range(20):
        gen = make_gen(seed)
        trials = [gen.generate() for _ in range(150)]
        positions = [t.position for t in trials]
        for i in range(MAX_STREAK, len(positions)):
            window = positions[i - MAX_STREAK: i + 1]
            assert len(set(window)) > 1, f"seed={seed}: streak a indice {i - MAX_STREAK}"
