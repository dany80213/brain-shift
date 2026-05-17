import json
from pathlib import Path

_FILE = Path(__file__).resolve().parent.parent / "leaderboard.json"
_MAX = 5


def load() -> list:
    if not _FILE.exists():
        return []
    with _FILE.open() as f:
        return json.load(f)


def save_score(score: int) -> list:
    entries = load()
    entries.append(score)
    entries.sort(reverse=True)
    entries = entries[:_MAX]
    with _FILE.open("w") as f:
        json.dump(entries, f)
    return entries
