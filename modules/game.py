from modules.info import GameState, WHITE, BLACK
from modules.ui_element import UIElement
from pygame.sprite import RenderUpdates
import pygame


def title_screen(screen):
    start_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )
    quit_btn = UIElement(
        center_position=(400, 500),
        font_size=30,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn)

    return game_loop(screen, buttons)


def play_level(screen, player):
    return_btn = UIElement(
        center_position=(140, 570),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Return to main menu",
        action=GameState.TITLE,
    )

    nextlevel_btn = UIElement(
        center_position=(400, 400),
        font_size=30,
        bg_rgb=None,
        text_rgb=WHITE,
        text=f"Next level ({player.current_level + 1})",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, nextlevel_btn)

    return game_loop(screen, buttons)

def game_loop(screen, buttons):
    """ Handles game loop until an action is return by a button in the
        buttons sprite renderer.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()