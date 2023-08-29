from .constants import *
from .elements import Maze, Wall
from .ui_element import UIElement
import pygame
from pygame.sprite import RenderUpdates
from datetime import datetime
from enum import Enum

_stuff = [[65, 178, 53, 202], [110, 252, 87, 40], [182, 188, 45, 150], [285, 192, 113, 26], [287, 197, 34, 143], [302, 261, 93, 22], [281, 322, 110, 14], [462, 196, 0, 143], [462, 322, 4, 0], [451, 196, 12, 125], [464, 290, 79, 31], [570, 210, 43, 104], [614, 276, 54, 37], [692, 205, 88, 104]];
_2 = []

for x in _stuff:
    _2.append(Wall(x[0], x[1], x[2], x[3]))

_2.append(Wall(790, 0, 10, 600, GREEN, "win"))

class Levels:
    LEVELS = [
        Maze(_2, (0, 0), (600, 800)),
        # Maze([])
    ]