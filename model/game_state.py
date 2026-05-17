import time
from model.trial import Trial, generate_trial


class GameState:
    def __init__(self, rng):
        self.rng = rng
        self.score = 0
        self.count = 0
        self.attempts = 0
        self.multiplier = 1
        self.meter = 0
        self.hint_level = 0
        self.state = "INTRO"
        self.running = True
        self.start_time = 0
        self.pause_start = 0
        self.feedback_until = 0
        self.trial_until = 0
        self.feedback_color = None
        self.current_trial: Trial = generate_trial(rng)

    def reset(self):
        self.score = 0
        self.count = 0
        self.attempts = 0
        self.multiplier = 1
        self.meter = 0
        self.hint_level = 0
        self.state = "INTRO"
        self.start_time = 0
        self.pause_start = 0
        self.feedback_until = 0
        self.trial_until = 0
        self.feedback_color = None
        self.current_trial = generate_trial(self.rng)
