# Architettura

Brain Shift segue una struttura MVC per separare la logica di gioco dal rendering.

## Struttura del progetto

```
brain-shift/
├── main.py                  # Entry point
├── config.py                # Costanti di gioco
├── model/
│   ├── game_state.py        # Stato mutabile (punteggio, moltiplicatore, meter, …)
│   ├── trial.py             # Dataclass Trial e generatore
│   ├── rules.py             # Logica di classificazione pura
│   ├── scoring.py           # Funzioni di scoring pure
│   └── leaderboard.py       # Persistenza top 5 punteggi (JSON)
├── controller/
│   └── game_controller.py   # Gestione input, temporizzazione, transizioni di stato
├── view/
│   ├── ui.py                # Tutto il rendering Pygame
│   └── sounds.py            # Generazione effetti sonori
└── tests/
    ├── test_rules.py
    ├── test_scoring_base.py
    ├── test_scoring_advanced.py
    ├── test_trial_generator.py
    └── conftest.py
```

## Model

Tutto lo stato di gioco è in `GameState`. Contiene solo dati, nessuna logica.

| Campo | Tipo | Descrizione |
|-------|------|-------------|
| `state` | str | `"INTRO"`, `"PLAYING"`, `"PAUSED"` o `"RESULTS"` |
| `score` | int | Punteggio corrente |
| `multiplier` | int | Moltiplicatore del punteggio (1–10) |
| `meter` | int | Contatore risposte corrette consecutive (0–3) |
| `hint_level` | int | Controlla l'opacità delle istruzioni a schermo |
| `start_time` | float | Timestamp di inizio sessione |
| `pause_start` | float | Timestamp quando è stato premuto P |
| `feedback_color` | tuple \| None | Colore della carta durante il feedback visivo |
| `feedback_until` | float | Timestamp di fine feedback |
| `trial_until` | float | Timestamp di fine inter-trial interval |
| `trial_start_time` | float | Timestamp di quando la carta corrente è diventata attiva |
| `max_multiplier` | int | Moltiplicatore massimo raggiunto nella sessione |
| `best_streak` | int | Miglior serie consecutiva di risposte corrette |
| `response_times` | list | Tempi di risposta registrati (in secondi) |
| `final_bonus` | int | Bonus applicato a fine sessione |
| `leaderboard` | list | Top 5 punteggi caricati a fine sessione |

Funzioni di scoring pure in `model/scoring.py`:

```python
apply_correct(score, multiplier, meter)  # restituisce (score, multiplier, meter)
apply_wrong(multiplier, meter)           # restituisce (multiplier, meter)
apply_bonus(score, multiplier)           # restituisce score
```

## Generatore dei trial

`TrialGenerator` in `model/trial.py` gestisce la generazione delle carte con due garanzie:

### 1. Limite alle streak di posizione

Il generatore tiene traccia delle ultime `MAX_STREAK` (default: 3) posizioni mostrate. Se sono tutte uguali, la prossima carta viene forzata nella posizione opposta. Questo evita lunghe serie dello stesso tipo che renderebbero il gioco monotono.

### 2. Bilanciamento YES/NO

Su una finestra mobile di `BALANCE_WINDOW` (default: 10) trial, il generatore monitora il rapporto tra risposte attese YES e NO. Se YES supera il 65%, la carta successiva viene generata in modo da richiedere una risposta NO (e viceversa sotto il 35%). Per le carte ALTO questo significa scegliere numeri pari o dispari; per le carte BASSO scegliere vocali o consonanti.

### Come si verifica

I test in `tests/test_trial_generator.py` verificano entrambe le proprietà su sequenze di 150–200 trial con seed diversi.

## Controller

Transizioni di stato:

```
INTRO ──(SPAZIO)──► PLAYING ──(60s)──► RESULTS ──(R)──► INTRO
                       │
                     (P) ↕
                    PAUSED
```

### Gestione della pausa

Quando si preme P viene registrato `pause_start`. Alla ripresa, tutti i campi temporali vengono traslati in avanti della durata della pausa:

```python
pause_duration = time.time() - state.pause_start
state.start_time       += pause_duration
state.feedback_until   += pause_duration  # se attivo
state.trial_until      += pause_duration  # se attivo
state.trial_start_time += pause_duration  # se attivo
```

### Inter-trial interval

Dopo ogni risposta il controller esegue due fasi:
1. Feedback (0.15 s) — la carta mostra verde o rosso
2. ITI (100–250 ms casuale) — la carta torna neutra prima del trial successivo

L'input è bloccato durante entrambe le fasi.

## View

`view/ui.py` contiene solo codice di rendering — nessuna logica, nessuna modifica allo stato.

| Funzione | Cosa mostra |
|----------|-------------|
| `draw_intro` | Schermata iniziale con regole e controlli |
| `draw_playing` | Schermata di gioco completa |
| `draw_paused` | Overlay semi-trasparente con testo PAUSA |
| `draw_results` | Pannello risultati di fine sessione |
| `draw_card` | Carta lettera/numero con eventuale colore di feedback |
| `draw_score_hud` | Box punteggio (in alto a sinistra) |
| `draw_timer_hud` | Timer conto alla rovescia (in alto a destra) |
| `draw_meter_hud` | Meter a 4 punti e moltiplicatore (in alto al centro) |
| `draw_instructions` | Istruzioni con dissolvenza progressiva |
| `draw_answer_buttons` | Pulsanti YES/NO cliccabili (in basso) |

## Config

```python
SEED = 48
SESSION_DURATION = 60
FEEDBACK_DURATION = 0.15
ITI_MIN = 0.10
ITI_MAX = 0.25
```
