import pygame
import pygame.freetype
from pygame.rect import Rect
from pygame.sprite import Sprite
from enum import Enum

# starting variables
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# special variables
FPS_clock = pygame.time.Clock()
FONT = pygame.font.Font(None, 36)
width = 1000
height = 600

game_font = pygame.font.SysFont('Impact', 40)

running = True

WALLS = [
    Rect(25, 0, 20, 540),
    Rect(70, 0, 20, 200),
    Rect(70, 230, 20, 375),
    Rect(115, 0, 20, 200),
    Rect(115, 0, 20, 540),
    Rect(160, 0, 20, 200),
    Rect(160, 230, 20, 375),
    Rect(205, 0, 20, 200),
    Rect(205, 0, 20, 540),
    Rect(250, 0, 20, 200),
    Rect(250, 230, 20, 375),
    Rect(295, 0, 20, 540),
    Rect(295, 0, 20, 200),
    Rect(340, 230, 20, 375),
    Rect(340, 0, 20, 200),
    Rect(385, 0, 20, 540),
    Rect(385, 0, 20, 200),
    Rect(430, 230, 20, 375),
    Rect(430, 0, 20, 200),
    Rect(475, 0, 20, 540),
    Rect(475, 0, 20, 200),
    Rect(520, 50, 85, 85),
    Rect(520, 160, 85, 85),
    Rect(520, 270, 85, 85),
    Rect(520, 380, 85, 85),
    Rect(520, 490, 415, 85),
    Rect(630, 50, 85, 85),
    Rect(630, 160, 85, 85),
    Rect(630, 270, 85, 85),
    Rect(630, 380, 85, 85),
    Rect(630, 490, 85, 85),
    Rect(740, 50, 85, 85),
    Rect(740, 160, 85, 85),
    Rect(740, 270, 85, 85),
    Rect(740, 380, 85, 85),
    Rect(740, 490, 85, 85),
    Rect(850, 50, 85, 85),
    Rect(850, 160, 85, 85),
    Rect(850, 270, 85, 85),
    Rect(850, 380, 85, 85),
    Rect(850, 490, 85, 85)
]

def create_surface_with_text(text: str, font_size: int, text_rgb: tuple[int, int, int], bg_rgb: tuple[int, int, int]) -> pygame.surface.Surface:
    '''Returns a surface with text written on it'''
    font = pygame.freetype.SysFont("Courier", font_size, bold=True)
    surface, _ = font.render(text=text, fgcolor=text_rgb, bgcolor=bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    """ User interface element that can be added to a surface """

    def __init__(self, center_position: tuple[int, int], text: str, font_size: int, bg_rgb: tuple[int, int, int], text_rgb: tuple[int, int, int]) -> None:
        self.mouse_over = False  # indicates if the mouse is over the element

        # create the default image
        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # create the image that shows when mouse is over the element
        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        # add both images and their rects to lists
        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # calls the init method of the parent sprite class
        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)

def main():
    pygame.init()

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Maze Game!")
    screen.fill(BLACK)

    ui_element = UIElement(
        center_position=(500, 300),
        font_size=30,
        bg_rgb=BLACK,
        text_rgb=WHITE,
        text="Maze Game",
    )

    running = True
    while running:
        for event in pygame.event.get():
            pass

        screen.fill(BLACK)
        ui_element.update(pygame.mouse.get_pos())
        ui_element.draw(screen)
        pygame.display.flip()

if __name__ == "__main__":
    main()