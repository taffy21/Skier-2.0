import pygame
import random
import cfg

class Obstacle(pygame.sprite.Sprite):
    """creates instances of trees"""
    def __init__(self, window, image, scale):
        super().__init__()
        self.window = window
        self.x = random.randint(0, cfg.WIDTH)
        self.y = random.randint(cfg.HEIGHT//2, cfg.HEIGHT+400)
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, scale)
        self.rect = self.image.get_rect(center = (self.x, self.y))

    def update(self):
        self.rect.move_ip(0, -2)

    def draw(self):
        self.window.blit(self.image, self.rect)


