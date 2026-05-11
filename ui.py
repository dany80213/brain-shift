import pygame

def draw_card(surface, trial):

    card_width, card_height = 100, 140

    x = (surface.get_width() // 2 - card_width // 2)
    y = (surface.get_height() // 2 - card_height // 2)

    if trial.position == "TOP":
        y = 100
    else:
        y = 350

    card_rect = pygame.Rect(x, y, card_width, card_height)


    pygame.draw.rect(surface, (255, 255, 255), card_rect, border_radius=10)
    pygame.draw.rect(surface, (0, 0, 0), card_rect, 2, border_radius=10)


    letter_font = pygame.font.SysFont("arial", 42, bold=True)
    number_font = pygame.font.SysFont("arial", 32)


    letter_text = letter_font.render(
        str(trial.letter),
        True,
        (0, 0, 0)
    )

    number_text = number_font.render(
        str(trial.number),
        True,
        (0, 0, 0)
    )


    letter_x = x + card_width // 2 - letter_text.get_width() // 2
    letter_y = y + 20

    number_x = x + card_width // 2 - number_text.get_width() // 2
    number_y = y + 80


    surface.blit(letter_text, (letter_x, letter_y))
    surface.blit(number_text, (number_x, number_y))