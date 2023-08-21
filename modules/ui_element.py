import pygame.freetype
from pygame.sprite import Sprite


def create_surface_with_text(text, font_size, text_rgb, bg_rgb):
    '''Returns a surface with text written on it'''
    font = pygame.font.Font("./static/gamefont.ttf", int(font_size))
    surface = font.render(text, False, text_rgb, bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    """ User interface element that can be added to a surface """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None):
        """
        Args:
            `center_position` - tuple (x, y) \n
            `text` - string of text to write \n
            `font_size` - int \n
            `bg_rgb` (background colour) - tuple (r, g, b) \n
            `text_rgb` (text colour) - tuple (r, g, b) \n
            `action` - the gamestate change associated with this button
        """
        self.mouse_over = False

        default_image = create_surface_with_text(
            text=text, font_size=font_size, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        highlighted_image = create_surface_with_text(
            text=text, font_size=font_size * 1.2, text_rgb=text_rgb, bg_rgb=bg_rgb
        )

        self.images = [default_image, highlighted_image]
        self.rects = [
            default_image.get_rect(center=center_position),
            highlighted_image.get_rect(center=center_position),
        ]

        # assign button action
        self.action = action

        super().__init__()

    # properties that vary the image and its rect when the mouse is over the element
    @property
    def image(self):
        return self.images[1] if self.mouse_over else self.images[0]

    @property
    def rect(self):
        return self.rects[1] if self.mouse_over else self.rects[0]

    def update(self, mouse_pos, mouse_up):
        """ Updates the `mouse_over` variable and returns the button's
            action value when clicked.
        """
        if self.rect.collidepoint(mouse_pos):
            self.mouse_over = True
            if mouse_up:
                return self.action
        else:
            self.mouse_over = False

    def draw(self, surface):
        """ Draws element onto a surface """
        surface.blit(self.image, self.rect)