import json

# Il file viene cercato nella cartella da cui si lancia il gioco 
_FILE = "leaderboard.json"
_MAX = 5


def load() -> list:
    try:
        with open(_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def save_score(score: int) -> list:
    entries = load()
    entries.append(score)
    entries.sort(reverse=True)
    entries = entries[:_MAX]
    with open(_FILE, "w") as f:
        json.dump(entries, f)
    return entries
