class GameStats():
    """Отслеживание статистики игры AlienInvasion"""
    def __init__(self, ai_game):
        """Инициализация статистики"""
        # Рекорд не должен сбрасываться
        self.high_score = 0
        self.settings = ai_game.settings
        self.reset_stats()
        # Игра запускается в неактивном состоянии
        self.game_active = False
    def reset_stats(self):
        """Инициализация статистики в ходе игры"""
        self.ships_left = self.settings.ship_limit
        self.score = 0
        self.level = 1