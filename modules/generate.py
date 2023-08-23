from .constants import GameState, WHITE, BLACK, SCREEN_WIDTH, MAX_LEVEL
from .elements import Maze, Wall
from .ui_element import UIElement
import pygame
from pygame.sprite import RenderUpdates
from datetime import datetime
from enum import Enum

class Levels:
    LEVEL1 = Maze([
        Wall(0, 0, 100, 100)
    ], (0, 0), (600, 800))