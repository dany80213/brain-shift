# Uso dell'IA nel progetto

## Strumenti usati

- [x] **Claude (modello: Claude Sonnet 4.6)**
- [x] **Gemini (modello: Gemini 2.5 Pro)**
- [x] **ChatGPT (modello: GPT-5.5)**

---

## Cosa abbiamo chiesto e cosa ha risposto

### 1. Struttura iniziale del progetto

**Cosa abbiamo chiesto:** Non sapevamo da dove iniziare per organizzare il progetto. Avevamo tutto in mente ma non sapevamo in quanti file dividerlo e come chiamarli.

**Cosa ci ha suggerito:** Di partire definendo le regole e lo scoring come funzioni pure in file separati, senza toccare pygame, così da poterle testare subito. Ci ha spiegato perché è più semplice debuggare una funzione isolata rispetto a cercare un errore dentro il loop di gioco. Ci ha anche detto di mettere i parametri fissi (durata sessione, seed, tempi) in un file `config.py` a parte, così da trovarli tutti in un posto senza dover cercare nel codice.

**Cosa abbiamo fatto:**
- [x] Preso solo l'idea e riscritto

---

### 2. Come strutturare il `GameState`

**Cosa abbiamo chiesto:** Avevamo tante variabili di gioco (punteggio, moltiplicatore, meter, timer, streak…) sparse in `main.py` e stava diventando difficile tenere tutto sotto controllo. Abbiamo chiesto come organizzarle meglio.

**Cosa ci ha suggerito:** Di raccoglierle tutte in una classe `GameState` con un metodo `reset()` per azzerare lo stato tra una partita e l'altra, invece di reinizializzare ogni variabile singolarmente. Ci ha spiegato che in questo modo è più difficile dimenticarsi di resettare qualcosa quando si aggiunge un campo nuovo.

**Cosa abbiamo fatto:**
- [x] Modificato adattandolo al nostro codice

---

### 3. Come funziona l'aggiunta dell'audio con pygame

**Cosa abbiamo chiesto:** Volevamo aggiungere suoni ma non avevamo mai lavorato con l'audio in pygame e non volevamo usare file esterni. Abbiamo chiesto sia come funzionava che del codice da cui partire.

**Cosa ci ha suggerito:** Il codice per generare i suoni direttamente dal programma, usando `math.sin` e `struct.pack` per produrre un buffer di byte da passare a `pygame.mixer.Sound`. Ci ha spiegato che il buffer deve avere un formato preciso (stereo, 16 bit, signed) e che `pygame.mixer.pre_init()` va chiamato prima di `pygame.init()`, altrimenti il mixer si inizializza con parametri diversi e il suono esce distorto.

**Cosa abbiamo fatto:**
- [x] Modificato adattandolo al nostro codice

---

### 4. Miglioramenti sulla parte grafica

**Cosa abbiamo chiesto:** Avevamo la grafica funzionante ma molto grezza — rettangoli piatti, tutto allineato a occhio, nessun contrasto visivo tra gli elementi. Abbiamo chiesto pezzi di codice concreti per migliorarla senza usare immagini esterne.

**Cosa ci ha suggerito:** Blocchi di codice funzionanti per le parti principali: la carta con angoli arrotondati tramite `border_radius` e un rettangolo sfalsato per l'ombra, l'HUD con sfondo e bordo separati per staccarsi visivamente dal resto, i cerchi pieni e vuoti per rappresentare il meter, e il cambio colore del timer sotto una certa soglia. Non conoscevamo queste possibilità di pygame.

**Cosa abbiamo fatto:**
- [x] Modificato adattandolo al nostro codice

---

### 5. Creazione dei test aggiuntivi

**Cosa abbiamo chiesto:** Non avevamo mai usato pytest e non sapevamo come si scrivevano i test. Abbiamo chiesto aiuto per creare i test aggiuntivi oltre a quelli forniti dal docente.

**Cosa ci ha suggerito:** Il codice dei test, spiegandoci come funzionava ogni parte — come si usa `assert`, come si costruisce uno scenario di partenza con un seed fisso, e cosa aveva senso testare per le parti che avevamo scritto noi (saturazione del moltiplicatore, comportamento con il meter vuoto, invarianza del seed nel generatore).

**Cosa abbiamo fatto:**
- [x] Accettato integralmente

---

### 6. Linguaggio della documentazione

**Cosa abbiamo chiesto:** Non sapevamo bene come scrivere la documentazione allora gli abbiamo spiegato il progetto e fornito pezzi di codice e ci ha spiegato come scriverla fornendo dei pezzi e correggendo qualcosa  

**Cosa ci ha suggerito:** Come riformulare alcune parti per renderle più dirette e comprensibili, suggerendoci il tono e le parole giuste per spiegare le scelte tecniche senza essere troppo formali o troppo vaghi.

**Cosa abbiamo fatto:**
- [x] Modificato adattandolo al nostro codice
