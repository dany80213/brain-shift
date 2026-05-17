# DEVLOG — Brain Shift

---

## 23 aprile 2026

Ho (@dany80213) inizializzato il repo e creato la struttura base: `main.py`, cartelle `assets/` e `tests/`. Per ora non gira ancora niente, ma almeno la struttura c'è.

---

## 5 maggio 2026

Ho (@alessandro-guttadauro) scritto la parte che genera le carte e calcola se la risposta è giusta. Ho aggiunto anche i primi test per verificare che le regole funzionassero.

Ho (@MattePavons) messo insieme il gioco e il sistema di punteggio con @alessandro-guttadauro. Il gioco gira già, si risponde con le frecce e il punteggio sale.

---

## 6 maggio 2026

Io (@MattePavons) e @alessandro-guttadauro abbiamo sistemato alcune cose che non tornavano nel codice di ieri.

---

## 11 maggio 2026

Ho (@dany80213) aggiunto qualche funzionalità.

---

## 13 maggio 2026

Ho (@MattePavons) aggiunto il feedback visivo: quando rispondi la carta diventa verde o rossa per qualche istante.

---

## 15 maggio 2026

Ho (@MattePavons) fatto in modo che le istruzioni spariscano pian piano — all'inizio le vedi, poi scompaiono. Per ora scompaiono dopo un po' comunque, non dipende da quanto stai andando bene.

@dany80213 ha fatto il merge del branch dev in `main`.

---

## 16 maggio 2026

Ho (@dany80213) riscritto quasi tutto oggi prima di aggiungere roba nuova: separato il codice in MVC (`model/`, `controller/`, `view/`), introdotto `GameController`, spostato le costanti in `config.py`, ridisegnato tutta la grafica, rimosso i file inutili e aggiunto i test di scoring.

---

## 17 maggio 2026

Ho (@dany80213) aggiunto scoring con meter e moltiplicatore, fading delle istruzioni collegato all'`hint_level`, inter-trial interval e le schermate INTRO e PAUSA.

@alessandro-guttadauro ha aggiunto i pulsanti YES/NO cliccabili — adesso si può rispondere anche col mouse oltre che con la tastiera.

Il progetto si è concluso il 17 maggio 2026.
