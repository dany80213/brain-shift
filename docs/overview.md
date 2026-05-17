# Panoramica

Brain Shift è un gioco di commutazione cognitiva rapida sviluppato con Python e Pygame. I giocatori classificano carte usando regole diverse in base alla posizione della carta sullo schermo — allenando attenzione, flessibilità mentale e velocità di reazione.

## Stati

| Stato | Descrizione |
|-------|-------------|
| `INTRO` | Schermata iniziale con regole e controlli. La sessione parte con SPAZIO |
| `PLAYING` | Sessione attiva, conto alla rovescia di 60 secondi |
| `PAUSED` | Timer bloccato. Premi P per riprendere |
| `RESULTS` | Statistiche di fine sessione. Premi R per rigiocare |

## Come si gioca

Una carta appare in alto o in basso sullo schermo con una lettera e un numero.

| Posizione | Regola |
|-----------|--------|
| ALTO | Numero pari → freccia destra · Numero dispari → freccia sinistra |
| BASSO | Vocale → freccia destra · Consonante → freccia sinistra |

Si può rispondere sia con le frecce della tastiera sia cliccando i pulsanti YES/NO sullo schermo.

## Controlli

| Tasto | Azione |
|-------|--------|
| `←` `→` | Rispondi |
| `P` | Pausa / riprendi |
| `SPAZIO` | Inizia la sessione (da INTRO) |
| `R` | Rigioca (da RESULTS) |

## Punteggio

- **+50 × moltiplicatore** per ogni risposta corretta
- Il meter si riempie con le risposte corrette — ogni 4 il moltiplicatore aumenta (max ×10)
- Una risposta sbagliata azzera il meter; se il meter è già vuoto, il moltiplicatore scende di 1
- **+250 × moltiplicatore** bonus di fine sessione

## Installazione

```bash
git clone https://github.com/dany80213/brain-shift.git
cd brain-shift
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install pygame
python main.py
```

## Test

```bash
pip install pytest
pytest tests/
```
