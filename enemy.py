import os
import pygame as pg

# Complete me! - TODO
class Enemy(pg.sprite.Sprite):
    def __init__(self, position):
        super(Enemy, self).__init__()

        # loads enemy image
        self.image = pg.image.load(os.path.join('assets', 'Ship3.png')).convert_alpha()

        self.rect = self.image.get_rect()

        self.rect.center = position
        
        self.speed_x = 100
        self.speed_y = 100

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self, delta):
        self.rect.x += self.speed_x * delta
        self.rect.y += self.speed_y * delta

        # keeps enemies in screen if they go out of bounds
        if self.rect.right > 1024:
            self.rect.left = 0

        if self.rect.left < 0:
            self.rect.right = 1024;
            
        if self.rect.y > 768:
            self.rect.y = -self.rect.height