import pygame


class Obstacle:
    def __init__(self, screen, x, y, width, height, image):
        self.x = x
        self.y = y
        self.image = image
        self.width = width
        self.height = height
        self.image_scale = pygame.transform.scale(self.image, (self.width, self.height))
        self.screen = screen
        self.hit_box = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        self.screen.blit(self.image_scale, (self.x, self.y))
