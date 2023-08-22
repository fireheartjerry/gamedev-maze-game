import pygame
from constants import RED

class Player:
    """ Stores information about a player """

    def __init__(self, lives=3, level=1, x=0, y=35):
        self.lives = lives
        self.level = level
        self.x = x
        self.y = y
        self.hack = False
        self.body = pygame.Rect(x, y, 30, 30)

    def reset(self):
        self.x = 0
        self.y = 35

class Wall(pygame.Rect):
    def __init__(self, x, y, width, height, colour=RED):
        super().__init__(x, y, width, height)
        self.colour = colour
    
    def set_colour(self, colour):
        """
        Set the colour of the maze wall.

        Args:
            `colour` (tuple): A tuple representing the RGB colour.
        """
        self.colour = colour

    def draw(self, surface):
        """
        Draw the maze wall on a given pygame surface.

        Args:
            `surface` (pygame.Surface): The surface to draw the wall on.
        """
        pygame.draw.rect(surface, self.colour, self)

class Maze:
    def __init__(self):
        self.walls = []  # List to store MazeWall objects
        self.start = None  # Starting position in the maze
        self.end = None    # Ending position in the maze

    def add_wall(self, wall):
        """
        Add a MazeWall object to the maze.

        Args:
            wall (MazeWall): The MazeWall object to add.
        """
        self.walls.append(wall)

    def set_start(self, x, y):
        """
        Set the starting position in the maze.

        Args:
            `x` (int): The x-coordinate of the starting position.
            `y` (int): The y-coordinate of the starting position.
        """
        self.start = (x, y)

    def set_end(self, x, y):
        """
        Set the ending position in the maze.

        Args:
            `x` (int): The x-coordinate of the ending position.
            `y` (int): The y-coordinate of the ending position.
        """
        self.end = (x, y)

    def draw(self, surface):
        """
        Draw the maze walls on a given pygame surface.

        Args:
            `surface` (pygame.Surface): The surface to draw the maze on.
        """
        for wall in self.walls:
            wall.draw(surface)

    def touching(self, player, hack=False):
        """
        Check if a position (x, y) is valid within the maze.

        Args:
            `player`: An instance of the player class

        Returns:
            bool: True if the player is not touching a wall, False otherwise.
        """
        if (hack):
            return True
        return (any(wall.colliderect(player.body) for wall in self.walls))