import time
from model.trial import Trial, TrialGenerator


class GameState:
    def __init__(self, rng):
        self.rng = rng

        # Punteggio e contatori di risposta
        self.score = 0           # punteggio totale accumulato
        self.count = 0           # risposte corrette
        self.attempts = 0        # tentativi totali (corretti + errati)

        # Sistema moltiplicatore
        self.multiplier = 1      # moltiplicatore attivo (1x, 2x, 3x...)
        self.meter = 0           # barre riempite verso il prossimo moltiplicatore (0-4)
        self.max_multiplier = 1  # moltiplicatore più alto raggiunto nella sessione

        # Streak
        self.current_streak = 0  # risposte corrette consecutive in corso
        self.best_streak = 0     # streak massima della sessione

        # Stato della schermata corrente
        self.state = "INTRO"     # può essere: INTRO, PLAYING, PAUSED, RESULTS
        self.running = True      # False quando si chiude la finestra

        # Temporizzazione della sessione
        self.start_time = 0      # timestamp di quando è iniziata la partita
        self.pause_start = 0     # timestamp di quando è stata messa in pausa

        # Temporizzazione del feedback visivo e dell'inter-trial interval
        self.feedback_until = 0  # fino a quando mostrare il colore di feedback sulla card
        self.trial_until = 0     # fino a quando aspettare prima del prossimo trial (ITI)
        self.feedback_color = None  # colore attuale del feedback (verde/rosso o None)

        # Hint: le istruzioni a schermo si affievoliscono man mano che il giocatore impara
        self.hint_level = 0      # sale a ogni risposta; sopra 11 le istruzioni spariscono

        # Metriche finali
        self.response_times = []  # lista dei tempi di risposta (in secondi) per ogni trial
        self.trial_start_time = 0 # timestamp di quando è apparso il trial corrente
        self.final_bonus = 0      # bonus calcolato a fine partita in base alle performance

        # Classifica
        self.leaderboard = []    # top 5 punteggi letti dal file al termine della sessione

        # Generatore e trial corrente
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
        self.leaderboard = []
        self.generator = TrialGenerator(self.rng)
        self.current_trial = self.generator.generate()
