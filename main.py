import random
import time
import pygame
from generator import generate_trial
from ui import draw_card
from scoring import apply_answer
rng = random.Random(48)
trial_di_test = generate_trial(rng)
start_time = time.time()
print(trial_di_test)
count = 0
score = 0
attempts = 0
pygame.init()
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True 
user_answer = False
state = "PLAYING"
feedback_until = 0
feedback_color = None

while running:
    if state == "PLAYING":
        current_time = time.time()
        
        if feedback_color is not None and current_time >= feedback_until:
            trial_di_test = generate_trial(rng)
            feedback_color = None

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            
            if event.type == pygame.KEYDOWN:
                if current_time < feedback_until:
                    continue

                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    attempts += 1
                    if event.key == pygame.K_LEFT:
                        user_answer = False
                    elif event.key == pygame.K_RIGHT:
                        user_answer = True
                        
                    is_correct = (user_answer == trial_di_test.expected_answer)
                    count += 1 if is_correct else 0
                    score = apply_answer(score,is_correct)
                    
                    feedback_color = (0, 255, 0) if is_correct else (255, 0, 0)
                    feedback_until = current_time + 0.15

        screen.fill((0, 0, 0))

        if count < 10:
            rule_font = pygame.font.SysFont("arial", 24)
            top_rule = rule_font.render("ALTO: Pari (Destra) o Dispari (Sinistra)", True, (150, 150, 150))
            bottom_rule = rule_font.render("BASSO: Vocale (Destra) o Consonante (Sinistra)", True, (150, 150, 150))
            screen.blit(top_rule, (WIDTH // 2 - top_rule.get_width() // 2, 40))
            screen.blit(bottom_rule, (WIDTH // 2 - bottom_rule.get_width() // 2, HEIGHT - 80))

        draw_card(screen, trial_di_test, feedback_color=feedback_color)

        # TIMER
        elapsed = time.time() - start_time

        remaining_time = max(0, 60 - int(elapsed))

        timer_font = pygame.font.SysFont("arial", 36, bold=True)

        timer_color = (255, 255, 255)

        if remaining_time <= 10:
            timer_color = (255, 0, 0)

        timer_text = timer_font.render(
            f"Time: {remaining_time}",
            True,
            timer_color
        )

        screen.blit(timer_text, (620, 20))

        if elapsed >= 60:
            state = "RESULTS"
            continue

        pygame.display.flip()

        clock.tick(60)
    elif state == "RESULTS":

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:

                    score = 0
                    count = 0
                    attempts = 0

                    start_time = time.time()

                    trial_di_test = generate_trial(rng)
                    feedback_until = 0
                    feedback_color = None

                    state = "PLAYING"

        screen.fill((25, 25, 35))

        # CALCOLI
        wrong = attempts - count

        accuracy = 0

        if attempts > 0:
            accuracy = int((count / attempts) * 100)

        # FONT
        title_font = pygame.font.SysFont("arial", 52, bold=True)
        text_font = pygame.font.SysFont("arial", 32)
        small_font = pygame.font.SysFont("arial", 24)

        # TESTI
        title = title_font.render("RESULTS", True, (255, 255, 255))

        score_text = text_font.render(
            f"Score: {score}",
            True,
            (0, 255, 100)
        )

        correct_text = text_font.render(
            f"Correct: {count}",
            True,
            (255, 255, 255)
        )

        wrong_text = text_font.render(
            f"Wrong: {wrong}",
            True,
            (255, 100, 100)
        )

        accuracy_text = text_font.render(
            f"Accuracy: {accuracy}%",
            True,
            (100, 200, 255)
        )

        replay_text = small_font.render(
            "Press R to replay",
            True,
            (200, 200, 200)
        )

        # DISEGNO
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 70))

        screen.blit(score_text, (260, 180))
        screen.blit(correct_text, (260, 240))
        screen.blit(wrong_text, (260, 300))
        screen.blit(accuracy_text, (260, 360))

        screen.blit(
            replay_text,
            (WIDTH // 2 - replay_text.get_width() // 2, 500)
        )

        pygame.display.flip()
            

pygame.quit()