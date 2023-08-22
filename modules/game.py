from modules.constants import GameState, WHITE, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT
from modules.ui_element import UIElement
from pygame.sprite import RenderUpdates
from datetime import datetime
import pygame

CENTERED_WIDTH = SCREEN_WIDTH/2

def title_screen(screen):
    """Title Screen Function - The main title screen of the game.

    Args:
        `screen` - The screen which we use to draw sprites on.\n

    Returns:
        `_game_loop()` function call, which in turn returns a gamestate.
    """
    start_btn = UIElement(
        center_position=(CENTERED_WIDTH, 150),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Start",
        action=GameState.NEWGAME,
    )

    quit_btn = UIElement(
        center_position=(CENTERED_WIDTH, 300),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Quit",
        action=GameState.QUIT,
    )

    creds_btn = UIElement(
        center_position=(CENTERED_WIDTH, 450),
        font_size=50,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Credits",
        action=GameState.CREDITS,
    )

    buttons = RenderUpdates(start_btn, quit_btn, creds_btn)

    return _game_loop(screen, buttons)

def play_level(screen, player):
    """Play Level Function - Renders the maze level background with the gameplay and some buttons.

    Args:
        `screen` - The screen which we use to draw sprites on.\n
        `player` - The player object (which is just a rectangle with stats).\n

    Returns:
        `_game_loop()` function call, which in turn returns a gamestate.
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
        center_position=(220, 575),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text=f"Reset",
        action=GameState.RESET_POS,
    )

    next_lvl_btn = UIElement(
        center_position=(875, 575),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text=f"Go to Level { player.level + 1 }",
        action=GameState.NEXT_LEVEL,
    )

    buttons = RenderUpdates(return_btn, reset_pos_btn, next_lvl_btn)

    return _game_loop(screen, buttons)

def game_credits(screen):
    """Handles the credits section of the game - shows developer names and version number.

    Args:
        `screen` - The screen which we use to draw sprites on.\n
    
    Returns:
        `_game_loop()` function call, which in turn returns a gamestate.
    """
    return_btn = UIElement(
        center_position=(80, 575),
        font_size=20,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Go Back",
        action=GameState.TITLE,
    )

    label_1 = UIElement(
        center_position=(CENTERED_WIDTH, 100),
        font_size=25,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Created by fireheartjerry and greb-the-awesome.",
        btn=False,
        font="Consolas",
        font_path=False
    )

    label_2 = UIElement(
        center_position=(CENTERED_WIDTH, 175),
        font_size=25,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Version: 0.0.1 Pre-Alpha.",
        btn=False,
        font="Consolas",
        font_path=False
    )

    label_3 = UIElement(
        center_position=(CENTERED_WIDTH, 250),
        font_size=25,
        bg_rgb=None,
        text_rgb=WHITE,
        text="Started dev work on 2023 August 19th.",
        btn=False,
        font="Consolas",
        font_path=False
    )

    label_4 = UIElement(
        center_position=(CENTERED_WIDTH, 325),
        font_size=25,
        bg_rgb=None,
        text_rgb=WHITE,
        text=f"Copyright {datetime.now().year}, MIT License.",
        btn=False,
        font="Consolas",
        font_path=False
    )

    buttons = RenderUpdates(return_btn, label_1, label_2, label_3, label_4)
    return _game_loop(screen, buttons)

def _game_loop(screen, buttons):
    """Handles game loop until an action is return by a button in the buttons sprite renderer.

    Args:
        `screen` - The screen which we use to draw sprites on.\n
        `player` - The player object (which is just a rectangle with stats).\n
    Returns:
        A gamestate from the GameState enum.
    """
    while True:
        mouse_up = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return GameState.QUIT
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_up = True
        screen.fill(BLACK)

        for button in buttons:
            ui_action = button.update(pygame.mouse.get_pos(), mouse_up)
            if ui_action is not None:
                return ui_action

        buttons.draw(screen)
        pygame.display.flip()