import pygame as pg
import pygame.constants as pgc
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from main import Game


class Racket:
    def __init__(self, game: "Game", offset: int, move_up: pgc, move_down: pgc):
        """Initialization."""
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = self.screen.get_rect()

        self.rect = pg.Rect(0, 0, self.settings.racket_width, self.settings.racket_height)
        self.rect.centery = self.screen_rect.centery
        self.rect.x = offset
        self.speed = self.settings.racket_speed
        self.move_up, self.move_down = move_up, move_down

        self.y = float(self.rect.y)

    def updating(self, delta_time: int) -> None:
        """Updates the racket position."""
        keys = pg.key.get_pressed()
        if keys[self.move_up] and self.rect.top >= 0:
            self.y -= self.speed * delta_time
        if keys[self.move_down] and self.rect.bottom <= self.screen_rect.bottom:
            self.y += self.speed * delta_time
        self.rect.y = self.y

    def increase_speed(self) -> None:
        """Increases speed."""
        self.speed *= 1.03

    def reduce_speed(self) -> None:
        """Reduces speed."""
        self.speed /= 1.06

    def set_center(self) -> None:
        """Places the racket in the center."""
        self.rect.centerx = self.screen_rect.centerx

    def depict(self) -> None:
        """Draws a racket on the screen."""
        pg.draw.rect(self.screen, self.settings.white, self.rect)


class Player1(Racket):
    """First player."""
    def __init__(self, game: "Game"):
        offset = 20
        move_up = pgc.K_w
        move_down = pgc.K_s
        super().__init__(game, offset, move_up, move_down)


class Player2(Racket):
    """Second player."""
    def __init__(self, game: "Game"):
        offset = game.settings.screen_width - 30
        move_up = pgc.K_UP
        move_down = pgc.K_DOWN
        super().__init__(game, offset, move_up, move_down)
