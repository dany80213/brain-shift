import random
import pygame
import config
from model.game_state import GameState
from controller.game_controller import GameController
from view.ui import draw_intro, draw_playing, draw_paused, draw_results
from view.sounds import load_sounds


def main():
    pygame.mixer.pre_init(44100, -16, 2, 512)
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Brain Shift")
    clock = pygame.time.Clock()

    sounds = load_sounds()
    rng = random.Random(config.SEED)
    state = GameState(rng=rng)
    controller = GameController(state, sounds)

    while state.running:
        events = pygame.event.get()
        controller.handle_events(events)
        controller.update()

        if state.state == "INTRO":
            draw_intro(screen)
        elif state.state == "PLAYING":
            draw_playing(screen, state)
        elif state.state == "PAUSED":
            draw_paused(screen, state)
        elif state.state == "RESULTS":
            draw_results(screen, state)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()
