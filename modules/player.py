class Player:
    """ Stores information about a player """

    def __init__(self, score=0, lives=3, level=1):
        self.score = score
        self.lives = lives
        self.level = level