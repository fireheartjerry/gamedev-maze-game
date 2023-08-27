from .constants import GameState, WHITE, BLACK, SCREEN_WIDTH, MAX_LEVEL
from .elements import Maze, Wall
from .ui_element import UIElement
import pygame
from pygame.sprite import RenderUpdates
from datetime import datetime
from enum import Enum

class Levels:
    LEVELS = [
        Maze([
            Wall(126, 67, 229, 148),
            Wall(96, 183, 234, 229)
        ], (0, 0), (600, 800)),
        # Maze([])
    ]