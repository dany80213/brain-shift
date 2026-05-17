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
        self.state = "PLAYING"
        self.running = True
        self.start_time = time.time()
        self.feedback_until = 0
        self.feedback_color = None
        self.current_trial: Trial = generate_trial(rng)

    def reset(self):
        self.score = 0
        self.count = 0
        self.attempts = 0
        self.multiplier = 1
        self.meter = 0
        self.state = "PLAYING"
        self.start_time = time.time()
        self.feedback_until = 0
        self.feedback_color = None
        self.current_trial = generate_trial(self.rng)
