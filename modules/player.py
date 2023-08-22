class Player:
    """ Stores information about a player """

    def __init__(self, lives=3, level=1, x=0, y=35):
        self.lives = lives
        self.level = level
        self.x = x
        self.y = y
        self.hack = False