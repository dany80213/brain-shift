# Brain Shift

A fast-paced cognitive switching game built with Python and Pygame. Players must quickly classify cards using different rules depending on where the card appears on screen — training attention, flexibility, and reaction speed.

## Gameplay

Each round lasts **60 seconds**. A card appears either at the top or bottom of the screen and shows a letter and a number.

| Position | Rule |
|----------|------|
| TOP | Even number → Right arrow · Odd number → Left arrow |
| BOTTOM | Vowel → Right arrow · Consonant → Left arrow |

The challenge is switching between the two rules as fast as possible without making mistakes.

## Controls

| Key | Action |
|-----|--------|
| `←` `→` | Answer |
| `P` | Pause / resume |
| `SPACE` | Start session |
| `R` | Replay (from results screen) |

## Scoring

- **+50 × multiplier** for each correct answer
- Meter fills up with correct answers — every 4 correct answers the multiplier increases (up to ×10)
- A wrong answer resets the meter; if the meter is already empty, the multiplier drops by 1
- **+250 × multiplier** bonus at the end of the session

## Features

- Opening screen with rules and controls — game starts only on SPACE
- 60-second timed sessions with live countdown
- Pause at any time with P — timer freezes correctly and resumes from where it left off
- Multiplier and meter system for scoring
- Visual feedback (green / red) after each answer
- Instructions fade out progressively as the player improves, reappear if accuracy drops
- Inter-trial interval (100–250 ms) between answers for rhythm and clarity
- Results screen with score, accuracy, and correct/wrong counts

## Installation

```bash
git clone https://github.com/dany80213/brain-shift.git
cd brain-shift
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
python main.py
```

## Running the tests

```bash
pip install pytest
pytest tests/
```

All 27 tests should pass.

## Project structure

```
brain-shift/
├── main.py                  # Entry point
├── config.py                # Game constants
├── model/                   # Pure logic, no Pygame
├── controller/              # Input handling and state transitions
├── view/                    # All rendering
├── docs/                    # Documentation
│   ├── overview.md
│   └── architecture.md
└── tests/
```

## Authors

- [@dany80213](https://github.com/dany80213)
- [@MattePavons](https://github.com/MattePavons)
- [@alessandro-guttadauro](https://github.com/alessandro-guttadauro)
