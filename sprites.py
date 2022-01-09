from utility_funcs import load_image
from config import *
import pygame


class Cat(pygame.sprite.Sprite):
    def __init__(self, hp=100, image=load_image(PICS[0]), x=0, y=0):
        super(Cat, self).__init__()
        self.hp = hp
        self.image = image
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def update(self):
        pass

    def move(self, x, y):
        pass