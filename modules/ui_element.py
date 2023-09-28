import pygame.font
from .constants import CYAN
import time
from pygame.sprite import Sprite

def get_text_surface(text, font_size, txt_rgb, bg_rgb, font, font_path=True):
	"""Returns a surface with text written on it."""
	font_label = pygame.font.Font(font, int(font_size)) if font_path else pygame.font.SysFont(font, int(font_size))
	surface = font_label.render(text, True, txt_rgb, bg_rgb)
	return surface.convert_alpha()

class UIElement(Sprite):
	"""User interface element that can be added to a surface\n

		Args:\n
			`center_position` - tuple (x, y).\n
			`text` - string of text to write.\n
			`font_size` - int.\n
			`bg_rgb` (background colour) - tuple (r, g, b).\n
			`text_rgb` (text colour) - tuple (r, g, b).\n
			`action` - the gamestate change associated with this button. Defaults to `None`\n
			`btn` - whether this should be a button or not (hoverable). Defaults to `True`\n
			`font` - the text font displayed with this. Defaults to `./static/gamefont.ttf`\n
			`font_path` - whether or not the font is custom (use font path or not). Defaults to `True`\n
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
		"""Updates the `mouse_over` variable and returns the button's action value when clicked."""
		if self.rect.collidepoint(mouse_pos):
			self.mouse_over = True
			if mouse_up:
				return self.action
		else:
			self.mouse_over = False

	def draw(self, surface):
		"""Draws element onto a surface"""
		surface.blit(self.image, self.rect)

class Timer(Sprite):
	"""
	A timer (for speedrunning purpose)
	"""
	def __init__(self, center_position, text, font_size, bg_rgb, text_rgb, font="./static/gamefont.ttf", font_path=True):
		self.default_image = get_text_surface(
			text=text,
			font_size=font_size,
			txt_rgb=text_rgb,
			bg_rgb=bg_rgb,
			font=font,
			font_path=font_path
		)
		self.font_size = font_size
		self.text_rgb = text_rgb
		self.bg_rgb = bg_rgb
		self.font = font
		self.font_path = font_path
		self.drect = self.default_image.get_rect(center=center_position)
		self.timestarted = -1
		self.text = text
		super().__init__()
	@property
	def image(self):
		return self.default_image

	@property
	def rect(self):
		return self.drect

	def update(self, mouse_pos, mouse_up):
		"""Updates the time."""
		if self.timestarted == -1:
			self.default_image = get_text_surface(
				text=self.text,
				font_size=self.font_size,
				txt_rgb=self.text_rgb,
				bg_rgb=self.bg_rgb,
				font=self.font,
				font_path=self.font_path
			)
		else:
			self.default_image = get_text_surface(
				text=str(time.time() - self.timestarted),
				font_size=self.font_size,
				txt_rgb=self.text_rgb,
				bg_rgb=self.bg_rgb,
				font=self.font,
				font_path=self.font_path
			)

	def draw(self, surface):
		"""Draws element onto a surface"""
		surface.blit(self.image, self.drect)
	def start(self):
		self.timestarted = time.time()
	def reset(self):
		self.timestarted = -1
	def get_elapsed(self):
		return time.time() - self.timestarted