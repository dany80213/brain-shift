import math
import struct
import pygame

_RATE = 44100


def _tone_bytes(freq: float, duration: float, volume: float = 0.5) -> bytes:
    n = int(_RATE * duration)
    buf = bytearray()
    for i in range(n):
        val = int(volume * 32767 * math.sin(2 * math.pi * freq * i / _RATE))
        buf += struct.pack('<hh', val, val)
    return bytes(buf)


def load_sounds() -> dict:
    sounds = {}
    for name, raw in (
        ("correct",  _tone_bytes(880, 0.12)),
        ("wrong",    _tone_bytes(220, 0.18, 0.4)),
        ("level_up", _tone_bytes(660, 0.08) + _tone_bytes(990, 0.12)),
    ):
        sounds[name] = pygame.mixer.Sound(buffer=raw)
    return sounds
