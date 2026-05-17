import time
import pygame
import config
from model.game_state import GameState
from model.trial import generate_trial
from model.scoring import apply_correct, apply_wrong, apply_bonus


class GameController:
    def __init__(self, state: GameState):
        self.state = state

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.QUIT:
                self.state.running = False
            elif event.type == pygame.KEYDOWN:
                if self.state.state == "PLAYING":
                    self._handle_playing_key(event.key)
                elif self.state.state == "RESULTS":
                    self._handle_results_key(event.key)

    def update(self):
        if self.state.state != "PLAYING":
            return
        current_time = time.time()
        if self.state.feedback_color is not None and current_time >= self.state.feedback_until:
            self.state.current_trial = generate_trial(self.state.rng)
            self.state.feedback_color = None
        if current_time - self.state.start_time >= config.SESSION_DURATION:
            self.state.score = apply_bonus(self.state.score, self.state.multiplier)
            self.state.state = "RESULTS"

    def _handle_playing_key(self, key):
        current_time = time.time()
        if current_time < self.state.feedback_until:
            return
        if key not in (pygame.K_LEFT, pygame.K_RIGHT):
            return
        user_answer = key == pygame.K_RIGHT
        is_correct = user_answer == self.state.current_trial.expected_answer
        self.state.attempts += 1
        if is_correct:
            self.state.count += 1
            self.state.score, self.state.multiplier, self.state.meter = apply_correct(
                self.state.score, self.state.multiplier, self.state.meter
            )
        else:
            self.state.multiplier, self.state.meter = apply_wrong(
                self.state.multiplier, self.state.meter
            )
        self.state.feedback_color = (50, 200, 90) if is_correct else (210, 55, 55)
        self.state.feedback_until = current_time + config.FEEDBACK_DURATION

    def _handle_results_key(self, key):
        if key == pygame.K_r:
            self.state.reset()
