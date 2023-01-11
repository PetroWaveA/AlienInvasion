class Settings():
	"""Класс для хранения всех настроек игры Alien Invasion."""

	def __init__(self):
		"""Инициализирует настройки игры."""
		#Параметры экрана
		self.screen_width = 1300
		self.screen_height = 700
		self.bg_color = (230, 230, 230)
		#Настройки корабля
		self.ship_speed = 3.5
		self.ship_limit = 3
		#Настройки снаряда
		self.bullet_speed = 2
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (60, 60, 60)
		self.bullet_allowed = 3
		#Настройки пришельцев
		self.alien_speed = 1.0
		self.fleet_drop_speed = 10
		# fleet_direction = 1 обозначает движение вправо; а -1 - влево.
		self.fleet_direction = 1 