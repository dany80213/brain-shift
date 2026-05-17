import random
import pytest
from model.scoring import apply_correct, apply_wrong, apply_bonus
from model.trial import TrialGenerator


def test_multiplier_caps_at_10():
    score, multiplier, meter = apply_correct(0, 10, 3)
    assert multiplier == 10


def test_multiplier_decreases_when_meter_empty():
    multiplier, meter = apply_wrong(3, 0)
    assert multiplier == 2
    assert meter == 0


def test_same_seed_same_sequence():
    gen1 = TrialGenerator(random.Random(42))
    gen2 = TrialGenerator(random.Random(42))
    for _ in range(20):
        assert gen1.generate() == gen2.generate()
