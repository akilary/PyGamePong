class Settings:
	def __init__(self):
		"""Initialization constants."""
		self.resolution = self.screen_width, self.screen_height = 1300, 750
		self.background_color = (0, 0, 0)
		self.fps = 0

		self.white = (255, 255, 255)
		self.racket_width, self.racket_height = 15, 100
		self.racket_speed = 0.568

		self.ball_width = 16
		self.ball_speed = [0.62, 0.62]

		self.start_score = 0
		self.max_score = 11

		self.font_name = "Impact"
		self.font_size = 324
		self.font_color = (40, 40, 40)
