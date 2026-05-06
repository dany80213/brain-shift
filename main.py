import random
import pygame
from generator import generate_trial
rng = random.Random(42)
trial_di_test = generate_trial(rng)
print(trial_di_test)
pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
runnig = True 
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((0, 0, 0))
    pygame.display.flip()
pygame.quit()