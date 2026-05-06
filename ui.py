import pygame 
def draw_card(surface,trial,config):
    card_whidth, card_height = 100,140
    x=(surface.get_whidt() // 2 - card_whidth // 2)
    y=(surface.get_height()//2 - card_height // 2)
    if trial.position == "TOP"
        y=100
    else:
        y=350 


    card_rect = pygame.Rect(x, y, card_whidth, card_height)
    
    pygame.draw.rect(surface, (255, 255, 255), card_rect)
    pygame.draw.rect(surface, (0, 0, 0), card_rect, 2)
