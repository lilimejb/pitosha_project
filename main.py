import pygame

from utility_funcs import load_image
from player import Player
from config import *

clock = pygame.time.Clock()


class Game:
    def __init__(self):
        pygame.init()
        cat_image = load_image(PICS[0])
        dog_image = load_image(PICS[1])
        gibon_image = load_image(PICS[2])

        self.cat_image = pygame.transform.scale(cat_image, (50, 50))
        self.dog_image = pygame.transform.scale(dog_image, (50, 50))
        self.gibon_image = pygame.transform.scale(gibon_image, (50, 50))
        self.images = [self.cat_image, self.dog_image, self.gibon_image]
        self.current_image = 0

        self.right = False
        self.left = False
        self.up = False
        self.down = False
        self.player = Player()

        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        self.running = True
        self.screen = pygame.display.set_mode(SIZE)
        self.played = 0

    def events(self):
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_image += 1
                if event.key == pygame.K_DOWN:
                    self.current_image -= 1
                if event.key == pygame.K_w:
                    self.up = True
                if event.key == pygame.K_a:
                    self.left = True
                if event.key == pygame.K_s:
                    self.down = True
                if event.key == pygame.K_d:
                    self.right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_w:
                    self.up = False
                if event.key == pygame.K_a:
                    self.left = False
                if event.key == pygame.K_s:
                    self.down = False
                if event.key == pygame.K_d:
                    self.right = False


    def update(self):
        ms = clock.tick(60)
        self.played += ms / 1000
        self.played = round(self.played, 2)
        pygame.display.set_caption(str(self.played))
        self.player.update(self.right, self.left, self.up, self.down)
        # if self.x <= 50:
        #     self.x = 50
        # if self.y <= 50:
        #     self.y = 50
        # if self.x >= SIZE[0] - 50:
        #     self.x = SIZE[0] - 50
        # if self.y >= SIZE[1] - 50:
        #     self.y = SIZE[1] - 50
        # if self.right:
        #     self.x += 10
        # if self.left:
        #     self.x -= 10
        # if self.up:
        #     self.y -= 10
        # if self.down:
        #     self.y += 10

    def render(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(self.images[self.current_image % len(self.images)], (300, 300))
        self.all_sprites.draw(self.screen)
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.render()


if __name__ == '__main__':
    game = Game()
    game.run()