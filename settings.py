class Settings:
    """Класс для хранения всех настроек игры Alien Invasion"""
    def __init__(self):
        """Инициализирует статические настройки игры"""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.fps = 60
        self.bg_color = 'black'
        # Настройки корабля
        self.ship_limit = 3
        # Настройки пришельцев
        self.fleet_drop_speed = 10
        # fleet_direction = 1 обозначает движение вправо; а -1 - влево
        self.fleet_direction = 1
        # Параметры снаряда
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (200, 0, 100)
        self.bullet_allowed = 3
        # Темп ускорения игры
        self.speedup_scale = 1.1
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        """Инициализирует настройки, изменяющиеся по ходу игры"""
        self.ship_speed = 5.0
        self.bullet_speed = 6.0
        self.alien_speed = 1.0
        self.star_speed = 3.0
        # 1 - вправо, -1 - влево
        self.fleet_direction = 1
        # Подсчет очков
        self.alien_points = 50
    def increase_speed(self):
        """Увеличивает настройки скорости и очки за поверженных противников"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale
        self.star_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
