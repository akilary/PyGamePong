import pygame as pg
from sys import exit

from ball import Ball
from settings import Settings
from hud import PointP1, PointP2
from racket import Player1, Player2
from typing import TYPE_CHECKING
if TYPE_CHECKING:
	from hud import HUD


class Game:
	def __init__(self):
		"""Initialization."""
		pg.init()
		self.settings = Settings()
		self.clock = pg.time.Clock()
		self.screen = pg.display.set_mode(self.settings.resolution)
		self.delta_time = 1

		self.ball = None
		self.player1, self.player2 = None, None
		self.point_p1, self.point_p2 = None, None
		self._reset()

	def _reset(self) -> None:
		"""Restart the game."""
		self.ball = Ball(self)
		self.player1 = Player1(self)
		self.player2 = Player2(self)
		self.point_p1 = PointP1(self)
		self.point_p2 = PointP2(self)

	def run(self) -> None:
		"""Starts the game."""
		while True:
			for event in pg.event.get():
				if event.type == pg.QUIT or event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
					pg.quit()
					exit()
			self.player1.updating(self.delta_time)
			self.player2.updating(self.delta_time)
			self.ball.updating(self.delta_time)
			self._check_collision()
			if self._is_winner():
				self._reset()

			self._update_screen()

	def _update_screen(self) -> None:
		"""Updates objects on the screen."""
		self.screen.fill(self.settings.background_color)

		self.point_p1.show()
		self.point_p2.show()
		self.player1.depict()
		self.player2.depict()
		self.ball.depict()

		pg.display.flip()

		self.delta_time = self.clock.tick(self.settings.fps)
		pg.display.set_caption(f"PingPong - {self.clock.get_fps():.1f} FPS")

	def _check_collision(self) -> None:
		"""Checks for collisions with obstacles."""
		if self.player1.rect.colliderect(self.ball.rect) and self.ball.speed[0] < 0:
			self._player_collision()
		elif self.player2.rect.colliderect(self.ball.rect) and self.ball.speed[0] > 0:
			self._player_collision()

		if self.ball.rect.top <= 0 and self.ball.speed[1] < 0:
			self.ball.speed[1] *= -1
		elif self.ball.rect.bottom >= self.settings.screen_height and self.ball.speed[1] > 0:
			self.ball.speed[1] *= -1

		self._check_out()

	def _is_winner(self) -> bool:
		"""Checks if the game is over."""
		if self.point_p1.score >= self.settings.max_score or self.point_p2.score >= self.settings.max_score:
			return True

	def _check_out(self) -> None:
		"""Checking the ball for out screen."""
		if self.ball.rect.right <= 0:
			self._handle_score(self.point_p2)
		elif self.ball.rect.left >= self.settings.screen_width:
			self._handle_score(self.point_p1)

	def _player_collision(self) -> None:
		"""Sets parameters for a collision with a racket."""
		self.ball.speed[0] *= -1
		self.ball.increase_speed()
		self.player1.increase_speed()
		self.player2.increase_speed()

	def _handle_score(self, point_p: "HUD") -> None:
		"""Sets parameters when the ball is released."""
		point_p.add_point()
		self.ball.set_position(point_p)
		self.ball.reduce_speed()
		self.player1.reduce_speed()
		self.player2.reduce_speed()


if __name__ == '__main__':
	game = Game()
	game.run()
