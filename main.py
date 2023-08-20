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

def title_screen(screen):
    start_btn = UIElement(
        center_position=(500, 400),
        font_size=30,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(500, 500),
        font_size=30,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = [start_btn, quit_btn]

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action
            button.draw(screen)

        pygame.display.flip()


def play_level(screen):
    return_btn = UIElement(
        center_position=(160, 570),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        ui_action = return_btn.update(pygame.mouse.get_pos(), mouse_up)
        if ui_action is not None:
            return ui_action
        return_btn.draw(screen)

        pygame.display.flip()

# main function
def main():
    pygame.init()

    screen = pygame.display.set_mode((1000, 600))
    game_state = GameState.TITLE

    while True:
        if game_state == GameState.TITLE:
            game_state = title_screen(screen)

        if game_state == GameState.NEWGAME:
            game_state = play_level(screen)

        if game_state == GameState.QUIT:
            pygame.quit()
            return

if __name__ == "__main__":
    main()