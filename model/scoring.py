def apply_answer(score: int, is_correct: bool) -> int:
    return score + 10 if is_correct else score - 5
