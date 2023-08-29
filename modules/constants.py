from enum import Enum

# Pygame constants
RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

# Game constants
MAX_LEVEL = 1

class GameState(Enum):
    """An GameState class, which is an extension of the Enum class, containing different game states such as quit, title screen, next level, etc...
    """
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NEXT_LEVEL = 2
    CREDITS = 3
    RESET_POS = 4