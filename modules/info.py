from enum import Enum

RED = (255, 0, 0)
GREEN = (0, 255, 0)
CYAN = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class GameState(Enum):
    QUIT = -1
    TITLE = 0
    NEWGAME = 1
    NEXT_LEVEL = 2
    CREDITS = 3
    RESET_POS = 4