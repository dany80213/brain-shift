import time
import random
import pygame
import config
from model.game_state import GameState
from model.scoring import apply_correct, apply_wrong, apply_bonus
from model.leaderboard import save_score
from view.ui import BUTTON_NO_RECT, BUTTON_YES_RECT


class GameController:
    def __init__(self, state: GameState, sounds: dict = None):
        self.state = state
        # Dizionario dei suoni caricati (nome → oggetto Sound); vuoto se il suono non è disponibile
        self._sounds = sounds or {}

    def _play(self, name: str):
        # Riproduce un suono se esiste, altrimenti lo ignora silenziosamente
        s = self._sounds.get(name)
        if s:
            s.play()

    def handle_events(self, events):
        # Smista ogni evento pygame verso il gestore dello stato corrente
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
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if self.state.state == "PLAYING":
                    self._handle_mouse_click(event.pos)

    def update(self):
        # Viene chiamato ogni frame; gestisce solo lo stato PLAYING
        if self.state.state != "PLAYING":
            return
        current_time = time.time()

        # Fase 1: il feedback visivo è scaduto → spegnilo e avvia l'inter-trial interval
        if self.state.feedback_color is not None and current_time >= self.state.feedback_until:
            self.state.feedback_color = None
            iti = random.uniform(config.ITI_MIN, config.ITI_MAX)
            self.state.trial_until = current_time + iti

        # Fase 2: l'inter-trial interval è scaduto → genera il prossimo trial
        if self.state.feedback_color is None and self.state.trial_until > 0 and current_time >= self.state.trial_until:
            self.state.current_trial = self.state.generator.generate()
            self.state.trial_start_time = current_time
            self.state.trial_until = 0

        # Fase 3: il tempo della sessione è finito → calcola bonus e vai ai risultati
        if current_time - self.state.start_time >= config.SESSION_DURATION:
            self.state.final_bonus = 250 * self.state.multiplier
            self.state.score = apply_bonus(self.state.score, self.state.multiplier)
            self.state.leaderboard = save_score(self.state.score)
            self.state.state = "RESULTS"

    def _handle_intro_key(self, key):
        # SPAZIO o INVIO avviano la partita
        if key in (pygame.K_SPACE, pygame.K_RETURN):
            self.state.start_time = time.time()
            self.state.trial_start_time = time.time()
            self.state.state = "PLAYING"

    def _handle_playing_key(self, key):
        if key == pygame.K_p:
            # P mette in pausa: salva il timestamp per calcolare la durata della pausa
            self.state.pause_start = time.time()
            self.state.state = "PAUSED"
            return
        # Freccia sinistra = NO, freccia destra = YES
        if key == pygame.K_LEFT:
            self._process_answer(False)
        elif key == pygame.K_RIGHT:
            self._process_answer(True)

    def _handle_mouse_click(self, pos):
        # Controlla se il click cade dentro uno dei due pulsanti
        if BUTTON_NO_RECT.collidepoint(pos):
            self._process_answer(False)
        elif BUTTON_YES_RECT.collidepoint(pos):
            self._process_answer(True)

    def _process_answer(self, is_yes: bool):
        current_time = time.time()
        # Ignora input durante il feedback o l'inter-trial interval
        if current_time < self.state.feedback_until or self.state.trial_until > 0:
            return

        # Registra il tempo di risposta per le statistiche finali
        if self.state.trial_start_time > 0:
            self.state.response_times.append(current_time - self.state.trial_start_time)
            self.state.trial_start_time = 0

        is_correct = is_yes == self.state.current_trial.expected_answer
        self.state.attempts += 1

        if is_correct:
            self.state.count += 1
            # Aumenta l'hint level: più risposte corrette → istruzioni sempre più sbiadite
            self.state.hint_level = min(self.state.hint_level + 1, 20)
            prev_multiplier = self.state.multiplier
            self.state.score, self.state.multiplier, self.state.meter = apply_correct(
                self.state.score, self.state.multiplier, self.state.meter
            )
            self.state.current_streak += 1
            self.state.best_streak = max(self.state.best_streak, self.state.current_streak)
            self.state.max_multiplier = max(self.state.max_multiplier, self.state.multiplier)
            # Suono diverso se si è appena saliti di moltiplicatore
            if self.state.multiplier > prev_multiplier:
                self._play("level_up")
            else:
                self._play("correct")
        else:
            # Errore: abbassa l'hint level e azzera lo streak
            self.state.hint_level = max(self.state.hint_level - 1, 0)
            self.state.multiplier, self.state.meter = apply_wrong(
                self.state.multiplier, self.state.meter
            )
            self.state.current_streak = 0
            self._play("wrong")

        # Mostra il colore di feedback sulla card per FEEDBACK_DURATION secondi
        self.state.feedback_color = (50, 200, 90) if is_correct else (210, 55, 55)
        self.state.feedback_until = current_time + config.FEEDBACK_DURATION

    def _handle_paused_key(self, key):
        if key == pygame.K_p:
            # Riprende: sposta in avanti tutti i timestamp della durata della pausa
            # così i timer non contano il tempo in pausa
            current_time = time.time()
            pause_duration = current_time - self.state.pause_start
            self.state.start_time += pause_duration
            if self.state.feedback_until > 0:
                self.state.feedback_until += pause_duration
            if self.state.trial_until > 0:
                self.state.trial_until += pause_duration
            if self.state.trial_start_time > 0:
                self.state.trial_start_time += pause_duration
            self.state.state = "PLAYING"

    def _handle_results_key(self, key):
        # R riavvia la partita da zero
        if key == pygame.K_r:
            self.state.reset()
