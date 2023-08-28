import pygame.font
from .constants import CYAN
from pygame.sprite import Sprite

def get_text_surface(text, font_size, txt_rgb, bg_rgb, font, font_path=True):
    '''Returns a surface with text written on it'''
    if (font_path):
        font_label = pygame.font.Font(font, int(font_size))
    else:
        font_label = pygame.font.SysFont(font, int(font_size))
    surface = font_label.render(text, True, txt_rgb, bg_rgb)
    return surface.convert_alpha()

class UIElement(Sprite):
    """ User interface element that can be added to a surface\n    
         
        Args:
            `center_position` - tuple (x, y) \n
            `text` - string of text to write \n
            `font_size` - int \n
            `bg_rgb` (background colour) - tuple (r, g, b) \n
            `text_rgb` (text colour) - tuple (r, g, b) \n
            `action` - the gamestate change associated with this button\n
            `btn` - whether this should be a button or not (hoverable)\n
            `font` - the text font displayed with this\n
            `font_path` - whether or not the font is custom (use font path or not)\n
    """

    def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, action=None, btn=True, font="./static/gamefont.ttf", font_path=True):
        self.mouse_over = False

        default_image = get_text_surface(
            text=text,
            font_size=font_size,
            txt_rgb=text_rgb,
            bg_rgb=bg_rgb,
            font=font,
            font_path=font_path
        )

        highlighted_image = get_text_surface(
            text=text,
            font_size=font_size * 1.15,
            txt_rgb=CYAN,
            bg_rgb=bg_rgb,
            font=font,
            font_path=font_path
        ) if btn else default_image

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
