import pygame as pg
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from main import Game


class Ball:
	def __init__(self, game: "Game"):
		"""Initialization."""
		self.screen = game.screen
		self.settings = game.settings

		self.screen_rect = self.screen.get_rect()

		self.rect = pg.Rect(0, 0, self.settings.ball_width, self.settings.ball_width)
		self.rect.center = self.screen_rect.center
		self.speed = self.settings.ball_speed.copy()

		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def updating(self, delta_time: int) -> None:
		"""Updates the ball's position."""
		self.x += self.speed[0] * delta_time
		self.y += self.speed[1] * delta_time

		self.rect.x = self.x
		self.rect.y = self.y

	def increase_speed(self) -> None:
		"""Increases speed."""
		self.speed[0] *= 1.03
		self.speed[1] *= 1.03

	def reduce_speed(self) -> None:
		"""Reduces speed."""
		self.speed[0] /= 1.06
		self.speed[1] /= 1.06

	def set_position(self, point_p) -> None:
		"""Set position for a ball."""
		self.rect.center = point_p.rect.center
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def depict(self) -> None:
		"""Draws a ball on the screen."""
		pg.draw.rect(self.screen, self.settings.white, self.rect)
