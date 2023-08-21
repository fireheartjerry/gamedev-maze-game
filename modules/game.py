from modules.info import GameState, WHITE, BLACK
from modules.ui_element import UIElement
from pygame.sprite import RenderUpdates
import pygame

def title_screen(screen):
    """Title Screen Function - The main title screen of the game.

    Args:
        `screen` - The screen which we use to draw sprites on.\n

    Returns:
        A render of the `_game_loop()` internal function.
    """
    start_btn = UIElement(
        center_position=(500, 150),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )

    quit_btn = UIElement(
        center_position=(500, 300),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    creds_btn = UIElement(
        center_position=(500, 450),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Credits",
        action=GameState.QUIT,
    )

    buttons = RenderUpdates(start_btn, quit_btn, creds_btn)

    return _game_loop(screen, buttons)

def play_level(screen, player):
    """Play Level Function - Renders the maze level background with the gameplay and some buttons.

    Args:
        `screen` - The screen which we use to draw sprites on.\n
        `player` - The player object (which is just a rectangle with stats).\n

    Returns:
        A render of the `_game_loop()` internal function.
    """
    return_btn = UIElement(
        center_position=(80, 575),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Go Back",
        action=GameState.TITLE,
    )

    reset_pos_btn = UIElement(
        center_position=(875, 575),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text=f"Reset Player",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, reset_pos_btn)

    return _game_loop(screen, buttons)

def _game_loop(screen, buttons):
    """Handles game loop until an action is return by a button in the buttons sprite renderer.

    Args:
        `screen` - The screen which we use to draw sprites on.\n
        `player` - The player object (which is just a rectangle with stats).\n
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