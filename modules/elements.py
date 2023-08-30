import pygame
from .constants import *

class Player:
    """Player class, the user-controlled part of the game.\n
        Args:\n
            `lives` (int, optional): Player lives. Defaults to 3.\n
            `level` (int, optional): Current level. Defaults to 1.\n
            `x` (int, optional): x position. Defaults to 0.\n
            `y` (int, optional): y position. Defaults to 35.\n
    """

    def __init__(self, lives=3, level=1, x=0, y=35):
        self.lives, self.level = lives, level
        self.x = self.dx = x
        self.y = self.dy = y
        self.speed = 0.2
        self.body = pygame.Rect(x, y, 30, 30)

    def update(self, walls, buttons, surface, fps):
        """Update the player. (Should be called every frame)

        Args:
            `walls`: A list of Wall objects
            `buttons`: A sprite group of buttons
            `surface`: The surface to draw onto
        """
        for wall in walls:
            if self.body.colliderect(wall):
                if wall.kind == "lose":
                    self.reset()
                elif wall.kind == "ice":
                    self.speed = 340/fps
                elif wall.kind == "win":
                    from .game import win_screen
                    win_screen(surface, buttons, self)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.y -= self.speed
        if keys[pygame.K_s]:
            self.y += self.speed
        if keys[pygame.K_a]:
            self.x -= self.speed
        if keys[pygame.K_d]:
            self.x += self.speed
        self.speed = 120/fps

    def draw(self, surface):
        """Draw the player."""
        self.body.x = self.x
        self.body.y = self.y
        pygame.draw.rect(surface, GREEN, self.body)

    def reset(self):
        """Reset player position to default x and y."""
        self.x = self.dx
        self.y = self.dy

class Wall(pygame.Rect):
    """A maze wall, another vital aspect of the game.\n
        Args:\n
            `x` (int): x position.\n
            `y` (int): y position.\n
            `width` (int): width of the wall.\n
            `height` (int): height of hte wall\n
            `colour` (tuple(int, int, int), optional): Wall color. Defaults to RED.\n
    """

    def __init__(self, x, y, width, height, colour=None, kind="lose"):   
        super().__init__(x, y, width, height)
        if colour is None:
            if kind == "lose":
                colour = RED
            elif kind == "win":
                colour = GREEN
            elif kind == "ice":
                colour = CYAN
            else:
                colour = RED
        self.colour = colour
        self.kind = kind

    def set_colour(self, colour):
        """Set the colour of the maze wall."""
        self.colour = colour

    def draw(self, surface):
        """Draw the maze wall on a given pygame surface."""
        pygame.draw.rect(surface, self.colour, self)

class Maze:
    """Maze class, main element of game.\n
        Args:\n
            `walls` (list, optional): A list of the maze walls. Defaults to [].\n
            `start` (tuple, optional): Start position. Defaults to (0, 0).\n
            `end` (tuple, optional): End position. Defaults to (0, 0).
    """

    def __init__(self, walls=[], start=(0, 0), end=(0, 0)):    
        self.walls = walls
        self.start = start
        self.end = end

    def add_wall(self, wall):
        """Add a `Wall` object to the maze."""
        self.walls.append(wall)

    def set_start_pos(self, x, y):
        """Set the starting position in the maze."""
        self.start = (x, y)

    def set_end_pos(self, x, y):
        """Set the ending position in the maze."""
        self.end = (x, y)

    def draw(self, surface):
        """Draw the maze walls on a given pygame surface."""
        for wall in self.walls:
            wall.draw(surface)

    def touching(self, player, hack=False):
        """Check if a position (x, y) is valid within the maze."""
        if (hack):
            return False
        return (any(wall.colliderect(player.body) for wall in self.walls))