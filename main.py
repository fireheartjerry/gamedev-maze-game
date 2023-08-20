import pygame
from UIElement import UIElement
from GameState import GameState

# starting variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# special variables
FPS_clock = pygame.time.Clock()
width = 1000
height = 600

# main function
def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game!")
    screen.fill(BLACK)

    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=BLUE,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    running = True
    while running:
        for event in pygame.event.get():
            pass

        screen.fill(BLACK)
        quit_btn.update(pygame.mouse.get_pos())
        quit_btn.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()