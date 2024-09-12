import pygame as pg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from main import Game


class HUD:
	def __init__(self, game: "Game", offset: int):
		"""Initialization."""
		self.screen = game.screen
		self.settings = game.settings
		self.offset = offset
		self.screen_rect = self.screen.get_rect()
		self.score = self.settings.start_score

		self.font = pg.font.SysFont(self.settings.font_name, self.settings.font_size)
		self.image = None
		self.rect = None
		self._update_image()

	def _update_image(self) -> None:
		"""Updates player score images."""
		self.image = self.font.render(str(self.score), True, self.settings.font_color, self.settings.background_color)
		self.rect = self.image.get_rect()
		self.rect.center = self.screen_rect.center
		self.rect.centerx = self.rect.centerx + self.offset

	def add_point(self) -> None:
		"""Increases the score."""
		self.score += 1
		self._update_image()

	def show(self) -> None:
		"""Draws the score."""
		self.screen.blit(self.image, self.rect)


class PointP1(HUD):
	def __init__(self, game):
		offset = -320
		super().__init__(game, offset)


class PointP2(HUD):
	def __init__(self, game):
		offset = 320
		super().__init__(game, offset)
