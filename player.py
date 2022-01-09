from utility_funcs import load_image
from config import *
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, hp=100, image=load_image(PICS[3]), x=0, y=0):
        super(Player, self).__init__()
        self.hp = hp
        self.image = pygame.transform.scale(image, (100, 100))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def update(self, right, left, up, down):
        if self.x <= 50:
            self.x = 50
        if self.y <= 50:
            self.y = 50
        if self.x >= SIZE[0] - 50:
            self.x = SIZE[0] - 50
        if self.y >= SIZE[1] - 50:
            self.y = SIZE[1] - 50
        if right:
            self.x += 10
        if left:
            self.x -= 10
        if up:
            self.y -= 10
        if down:
            self.y += 10

        self.rect.x = self.x
        self.rect.y = self.y
    
    