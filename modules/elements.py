import pygame
from constants import RED

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