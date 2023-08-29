from .constants import *
from .elements import Maze, Wall
from .ui_element import UIElement
import pygame
from pygame.sprite import RenderUpdates
from datetime import datetime
from enum import Enum

_stuff = [[151, 5, 56, 484, 'lose'], [155, 542, 46, 54, 'lose'], [283, 112, 43, 479, 'lose'], [281, 7, 28, 36, 'lose'], [400, 6, 33, 73, 'lose'], [405, 106, 28, 44, 'lose'], [407, 243, 38, 75, 'lose'], [410, 374, 22, 82, 'lose'], [403, 525, 524, 46, 'lose'], [510, 577, 304, 16, 'lose'], [437, 7, 342, 504, 'ice'], [469, 30, 49, 52, 'lose'], [574, 33, 36, 48, 'lose'], [562, 201, 64, 87, 'lose'], [489, 167, 59, 86, 'lose'], [535, 369, 68, 83, 'lose'], [647, 114, 49, 66, 'lose'], [689, 284, 61, 79, 'lose'], [658, 410, 74, 60, 'lose'], [465, 408, 61, 47, 'lose'], [771, 10, 15, 343, 'lose'], [777, 418, 24, 108, 'lose'], [782, 326, 180, 20, 'lose'], [787, 422, 168, 19, 'lose'], [941, 344, 13, 77, 'win']]
_2 = []

for x in _stuff:
    _2.append(Wall(x[0], x[1], x[2], x[3], None, x[4]))



class Levels:
    LEVELS = [
        Maze(_2, (0, 0), (600, 800)),
        # Maze([])
    ]