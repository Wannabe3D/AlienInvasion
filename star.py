import pygame
from pygame.sprite import Sprite
from random import randint
class StarDrop(Sprite):
    """Класс звёзд"""
    def __init__(self, ai_game):
        """Инициализация"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.px, self.py = randint(0, self.settings.screen_width), randint(0, self.settings.screen_height)
    def update(self):
        """Обновление"""
        self.py = (self.py + self.settings.star_speed) % self.settings.screen_height
        if self.py > self.settings.screen_height:
            self.py = randint(self.settings.screen_height, 0)
    def draw(self):
        """Рисование звёзд"""
        pygame.draw.circle(self.screen, 'white', (self.px, self.py), 1)
