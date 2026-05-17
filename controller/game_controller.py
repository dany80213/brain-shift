import time
import random
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
                if self.state.state == "INTRO":
                    self._handle_intro_key(event.key)
                elif self.state.state == "PLAYING":
                    self._handle_playing_key(event.key)
                elif self.state.state == "PAUSED":
                    self._handle_paused_key(event.key)
                elif self.state.state == "RESULTS":
                    self._handle_results_key(event.key)

    def update(self):
        if self.state.state != "PLAYING":
            return
        current_time = time.time()

        if self.state.feedback_color is not None and current_time >= self.state.feedback_until:
            self.state.feedback_color = None
            iti = random.uniform(config.ITI_MIN, config.ITI_MAX)
            self.state.trial_until = current_time + iti

        if self.state.feedback_color is None and self.state.trial_until > 0 and current_time >= self.state.trial_until:
            self.state.current_trial = generate_trial(self.state.rng)
            self.state.trial_until = 0

        if current_time - self.state.start_time >= config.SESSION_DURATION:
            self.state.score = apply_bonus(self.state.score, self.state.multiplier)
            self.state.state = "RESULTS"

    def _handle_intro_key(self, key):
        if key in (pygame.K_SPACE, pygame.K_RETURN):
            self.state.start_time = time.time()
            self.state.state = "PLAYING"

    def _handle_playing_key(self, key):
        current_time = time.time()

        if key == pygame.K_p:
            self.state.pause_start = current_time
            self.state.state = "PAUSED"
            return

        if current_time < self.state.feedback_until or self.state.trial_until > 0:
            return
        if key not in (pygame.K_LEFT, pygame.K_RIGHT):
            return

        user_answer = key == pygame.K_RIGHT
        is_correct = user_answer == self.state.current_trial.expected_answer
        self.state.attempts += 1
        if is_correct:
            self.state.count += 1
            self.state.hint_level = min(self.state.hint_level + 1, 20)
            self.state.score, self.state.multiplier, self.state.meter = apply_correct(
                self.state.score, self.state.multiplier, self.state.meter
            )
        else:
            self.state.hint_level = max(self.state.hint_level - 1, 0)
            self.state.multiplier, self.state.meter = apply_wrong(
                self.state.multiplier, self.state.meter
            )
        self.state.feedback_color = (50, 200, 90) if is_correct else (210, 55, 55)
        self.state.feedback_until = current_time + config.FEEDBACK_DURATION

    def _handle_paused_key(self, key):
        if key == pygame.K_p:
            current_time = time.time()
            pause_duration = current_time - self.state.pause_start
            self.state.start_time += pause_duration
            if self.state.feedback_until > 0:
                self.state.feedback_until += pause_duration
            if self.state.trial_until > 0:
                self.state.trial_until += pause_duration
            self.state.state = "PLAYING"

    def _handle_results_key(self, key):
        if key == pygame.K_r:
            self.state.reset()
