"""
Configurazione pytest per il laboratorio Brain Shift.

Aggiunge la radice del progetto al sys.path così i test possono importare
rules.py e scoring.py anche se si trovano in cartelle diverse.
"""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))
