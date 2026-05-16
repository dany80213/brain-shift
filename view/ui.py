import time
import pygame
import config
from model.game_state import GameState
from model.trial import Trial


# ---------------------------------------------------------------------------
# Colors
# ---------------------------------------------------------------------------
BG_COLOR        = (18, 18, 30)
CARD_BG         = (240, 240, 250)
CARD_SHADOW     = (6, 6, 16)
CARD_BORDER     = (50, 50, 80)
TEXT_MAIN       = (220, 220, 235)
TEXT_DIM        = (115, 115, 140)
TEXT_ON_CARD    = (20, 20, 40)
TEXT_ON_COLORED = (255, 255, 255)
HUD_BG          = (26, 26, 44)
HUD_BORDER      = (58, 58, 88)
COLOR_CORRECT   = (50, 200, 90)
COLOR_WRONG     = (210, 55, 55)
COLOR_TIMER_OK  = (155, 205, 255)
COLOR_TIMER_LOW = (255, 75, 75)
COLOR_SCORE     = (85, 205, 145)
COLOR_ACCURACY  = (100, 175, 255)
SEPARATOR       = (42, 42, 68)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def draw_hud_box(surface, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, HUD_BG, rect, border_radius=8)
    pygame.draw.rect(surface, HUD_BORDER, rect, 1, border_radius=8)


def draw_panel(surface, x, y, w, h):
    rect = pygame.Rect(x, y, w, h)
    pygame.draw.rect(surface, (22, 22, 38), rect, border_radius=16)
    pygame.draw.rect(surface, (62, 62, 92), rect, 2, border_radius=16)


# ---------------------------------------------------------------------------
# Playing screen components
# ---------------------------------------------------------------------------

def draw_card(surface, trial: Trial, feedback_color=None):
    card_w = 120
    card_h = 160
    cx = surface.get_width() // 2
    card_x = cx - card_w // 2

    if trial.position == "TOP":
        card_y = 130
    else:
        card_y = 360

    card_rect = pygame.Rect(card_x, card_y, card_w, card_h)

    # Shadow (offset rect drawn first, behind the card)
    shadow_rect = pygame.Rect(card_x + 5, card_y + 5, card_w, card_h)
    pygame.draw.rect(surface, CARD_SHADOW, shadow_rect, border_radius=12)

    # Card body
    bg_color = feedback_color if feedback_color else CARD_BG
    pygame.draw.rect(surface, bg_color, card_rect, border_radius=12)
    pygame.draw.rect(surface, CARD_BORDER, card_rect, 2, border_radius=12)

    # Text: white on colored feedback, dark on white card
    text_color = TEXT_ON_COLORED if feedback_color else TEXT_ON_CARD

    letter_font = pygame.font.SysFont("arial", 52, bold=True)
    number_font = pygame.font.SysFont("arial", 38)

    letter_surf = letter_font.render(str(trial.letter), True, text_color)
    number_surf = number_font.render(str(trial.number), True, text_color)

    letter_x = card_x + card_w // 2 - letter_surf.get_width() // 2
    number_x = card_x + card_w // 2 - number_surf.get_width() // 2

    surface.blit(letter_surf, (letter_x, card_y + 22))
    surface.blit(number_surf, (number_x, card_y + 96))


def draw_score_hud(surface, score):
    draw_hud_box(surface, 20, 16, 90, 64)

    label_font = pygame.font.SysFont("arial", 17)
    value_font = pygame.font.SysFont("arial", 28, bold=True)

    label_surf = label_font.render("SCORE", True, TEXT_DIM)
    value_surf = value_font.render(str(score), True, COLOR_SCORE)

    cx = 20 + 45
    surface.blit(label_surf, (cx - label_surf.get_width() // 2, 22))
    surface.blit(value_surf, (cx - value_surf.get_width() // 2, 42))


def draw_timer_hud(surface, remaining):
    w = surface.get_width()
    box_x = w - 110
    draw_hud_box(surface, box_x, 16, 90, 64)

    label_font = pygame.font.SysFont("arial", 17)
    value_font = pygame.font.SysFont("arial", 28, bold=True)

    timer_color = COLOR_TIMER_LOW if remaining <= 10 else COLOR_TIMER_OK

    label_surf = label_font.render("TIME", True, TEXT_DIM)
    value_surf = value_font.render(str(remaining), True, timer_color)

    cx = box_x + 45
    surface.blit(label_surf, (cx - label_surf.get_width() // 2, 22))
    surface.blit(value_surf, (cx - value_surf.get_width() // 2, 42))


def draw_instructions(surface, count):
    if count >= config.INSTRUCTIONS_FADE_AFTER:
        return

    w, h = surface.get_width(), surface.get_height()
    font = pygame.font.SysFont("arial", 21)

    top_text    = "ALTO:   Pari → Destra   ·   Dispari → Sinistra"
    bottom_text = "BASSO:  Vocale → Destra   ·   Consonante → Sinistra"

    top_surf    = font.render(top_text, True, TEXT_DIM)
    bottom_surf = font.render(bottom_text, True, TEXT_DIM)

    # Top rule sits just below the HUD boxes (which end at y=80)
    surface.blit(top_surf,    (w // 2 - top_surf.get_width() // 2, 92))
    # Bottom rule sits near the bottom edge
    surface.blit(bottom_surf, (w // 2 - bottom_surf.get_width() // 2, h - 52))


def draw_playing(surface, state: GameState):
    surface.fill(BG_COLOR)

    elapsed        = time.time() - state.start_time
    remaining_time = max(0, config.SESSION_DURATION - int(elapsed))

    draw_score_hud(surface, state.score)
    draw_timer_hud(surface, remaining_time)
    draw_instructions(surface, state.count)
    draw_card(surface, state.current_trial, feedback_color=state.feedback_color)


# ---------------------------------------------------------------------------
# Results screen
# ---------------------------------------------------------------------------

def draw_results(surface, state: GameState):
    w, h = surface.get_width(), surface.get_height()
    surface.fill(BG_COLOR)

    wrong    = state.attempts - state.count
    accuracy = int((state.count / state.attempts) * 100) if state.attempts > 0 else 0

    panel_w = 420
    panel_h = 440
    panel_x = w // 2 - panel_w // 2
    panel_y = h // 2 - panel_h // 2
    draw_panel(surface, panel_x, panel_y, panel_w, panel_h)

    title_font = pygame.font.SysFont("arial", 44, bold=True)
    label_font = pygame.font.SysFont("arial", 20)
    value_font = pygame.font.SysFont("arial", 32, bold=True)
    hint_font  = pygame.font.SysFont("arial", 19)

    title_surf = title_font.render("RISULTATI", True, TEXT_MAIN)
    surface.blit(title_surf, (w // 2 - title_surf.get_width() // 2, panel_y + 22))

    rows = [
        ("Punteggio",   str(state.score), COLOR_SCORE),
        ("Corrette",    str(state.count), COLOR_CORRECT),
        ("Errate",      str(wrong),       COLOR_WRONG),
        ("Accuratezza", f"{accuracy}%",   COLOR_ACCURACY),
    ]

    row_start_y = panel_y + 108
    row_height  = 72

    for index, (label_text, value_text, color) in enumerate(rows):
        row_y = row_start_y + index * row_height

        if index > 0:
            sep_y = row_y - 10
            pygame.draw.line(
                surface, SEPARATOR,
                (panel_x + 20, sep_y),
                (panel_x + panel_w - 20, sep_y)
            )

        label_surf = label_font.render(label_text, True, TEXT_DIM)
        value_surf = value_font.render(value_text, True, color)

        surface.blit(label_surf, (panel_x + 30, row_y))
        surface.blit(value_surf, (panel_x + panel_w - 30 - value_surf.get_width(), row_y))

    hint_surf = hint_font.render("Premi  R  per rigiocare", True, TEXT_DIM)
    surface.blit(hint_surf, (w // 2 - hint_surf.get_width() // 2, panel_y + panel_h - 40))
