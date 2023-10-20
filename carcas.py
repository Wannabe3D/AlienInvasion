import pygame
from pygame.sprite import Sprite
from random import randint
pygame.init()
WIDTH, HEIGHT = 800, 600
FPS = 60
window = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
class StarDrop(Sprite):
    def __init__(self):
        self.px, self.py = randint(0, WIDTH), randint(0, HEIGHT)
    def update(self):
        self.py += 5
        if self.py > HEIGHT:
            self.py = randint(-HEIGHT, 0)
    def draw(self):
        pygame.draw.circle(window, 'white', (self.px, self.py), 1)
rain = []
for _ in range(100):
    rain.append(StarDrop())
play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
    for drop in rain:
        drop.update()

    window.fill('black')
    for drop in rain:
        drop.draw()
    pygame.display.update()
    clock.tick(FPS)
pygame.quit()