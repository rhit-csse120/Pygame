import math
import pygame
from Obstacle import Obstacle


class Bullet:
    def __init__(self, screen: pygame.Surface, x, y, angle, tank):
        self.screen = screen
        self.x = x
        self.y = y
        self.tank = tank
        self.h_speed = 5 * math.cos(angle * math.pi / 180)
        self.v_speed = 5 * math.sin(angle * math.pi / 180)
        self.height = 10
        self.width = 8
        self.hit_by_tank = False
        self.hit_by_obstacles = False
        self.has_exploded = False
        self.color = "magenta"
        self.bounces = 0

    def draw(self):
        pygame.draw.line(self.screen, self.color,
                         (self.x, self.y),
                         (self.x + self.height, self.y),
                         self.width)

    def move(self):
        self.x += self.h_speed
        self.y -= self.v_speed

    def is_hit_by_obstacles(self, obstacle: Obstacle):
        obstacle_rect = pygame.Rect(obstacle.x, obstacle.y,
                                    obstacle.hit_box.width, obstacle.hit_box.height)
        bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        return bullet_rect.colliderect(obstacle_rect)

    # def is_hit_by_tanks(self, obstacle: Obstacle):
    #     obstacle_rect = pygame.Rect(obstacle.x, obstacle.y,
    #                                 obstacle.hit_box.width, obstacle.hit_box.height)
    #     bullet_rect = pygame.Rect(self.x, self.y, self.width, self.height)
    #     return bullet_rect.collidepoint(obstacle_rect)

    def explode(self):
        self.has_exploded = True
