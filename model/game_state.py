import time
from model.trial import Trial, TrialGenerator


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
        self.max_multiplier = 1
        self.best_streak = 0
        self.current_streak = 0
        self.response_times = []
        self.trial_start_time = 0
        self.final_bonus = 0
        self.generator = TrialGenerator(rng)
        self.current_trial: Trial = self.generator.generate()

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
        self.max_multiplier = 1
        self.best_streak = 0
        self.current_streak = 0
        self.response_times = []
        self.trial_start_time = 0
        self.final_bonus = 0
        self.generator = TrialGenerator(self.rng)
        self.current_trial = self.generator.generate()
