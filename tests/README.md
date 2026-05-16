# Test forniti — istruzioni per gli studenti

Questa cartella contiene i **test pytest forniti dal docente** per il laboratorio Brain Shift. Sono parte integrante del progetto: per ottenere la sufficienza devono passare tutti.

## Cosa contiene

- `test_rules.py` — verifica che `is_even`, `is_vowel` e `compute_expected_answer` si comportino correttamente
- `test_scoring_base.py` — verifica che la versione lineare di `apply_answer` funzioni
- `conftest.py` — configurazione pytest per importare i vostri moduli

## Cosa dovete fare

1. Copiate **tutti i file di questa cartella** nella cartella `tests/` del vostro repository.
2. Installate pytest: `pip install pytest`.
3. Lanciate i test: `pytest tests/` dalla radice del repository.
4. All'inizio falliranno tutti (normale, non avete ancora scritto `rules.py` e `scoring.py`).
5. Man mano che completate le fasi 1 e 4 della guida operativa, i test inizieranno a diventare verdi.

## Firme attese delle vostre funzioni

I test si aspettano che abbiate scritto:

```python
# rules.py
def is_even(number: int) -> bool: ...
def is_vowel(letter: str) -> bool: ...
def compute_expected_answer(position: str, letter: str, number: int) -> bool: ...

# scoring.py
def apply_answer(score: int, is_correct: bool) -> int: ...
```

Se chiamate le funzioni con nomi diversi, i test non vi troveranno.

## Convenzioni importanti

- `position` è una stringa: `"TOP"` o `"BOTTOM"` (maiuscolo). Se usate altro (enum, costanti diverse), dovete adattare i test, e questo diventa un obiettivo avanzato.
- `is_vowel` accetta solo lettere maiuscole. Se volete gestire anche minuscole è un'estensione vostra.
- `apply_answer(score, is_correct)` restituisce il **nuovo punteggio**, non modifica nulla in place.

## Se un test fallisce

Pytest vi dice esattamente cosa non torna:

```
FAILED tests/test_rules.py::test_is_even_with_zero - AssertionError: assert False == True
```

Leggete il nome del test: vi dice cosa stava verificando. Leggete il messaggio di errore: vi dice cosa si aspettava e cosa ha trovato. Correggete il codice, rilanciate i test.

Non modificate i test forniti per farli passare: è barare e si vede dal diff.
