def apply_answer(score: int, is_correct: bool) -> int:
    return score + 10 if is_correct else score - 5


def apply_correct(score: int, multiplier: int, meter: int):
    score += 50 * multiplier
    meter += 1
    if meter == 4:
        multiplier = min(multiplier + 1, 10)
        meter = 0
    return score, multiplier, meter


def apply_wrong(multiplier: int, meter: int):
    if meter > 0:
        meter = 0
    else:
        multiplier = max(multiplier - 1, 1)
    return multiplier, meter


def apply_bonus(score: int, multiplier: int) -> int:
    return score + 250 * multiplier
