import pygame
from Bullet import Bullet
# from Tank import Tank
from Obstacle import Obstacle
from Obstacles import Obstacles


class Bullets:
    def __init__(self, screen: pygame.Surface):
        self.screen = screen
        self.list_of_bullets = []

    def add_bullets(self, bullet: Bullet):
        self.list_of_bullets.append(bullet)

    def draw(self):
        for bullet in self.list_of_bullets:
            bullet.draw()

    def move(self):
        for bullet in self.list_of_bullets:
            bullet.move()

    def remove_dead_bullet(self):
        for k in range(len(self.list_of_bullets) - 1, -1, -1):
            bullet = self.list_of_bullets[k]
            if bullet.has_exploded is True or bullet.hit_by_tank is True or bullet.is_hit_by_obstacles is True:
                del self.list_of_bullets[k]

    def handle_explosions_obstacles(self, obstacles: Obstacles):
        for bullet in self.list_of_bullets:
            for obstacle in obstacles.obstacles:
                if bullet.is_hit_by_obstacles(obstacle):
                    if bullet.bounces >= 4:
                        bullet.explode()
                        self.remove_dead_bullet()
                    else:
                        if obstacle.x < bullet.x < obstacle.x + obstacle.width:
                            bullet.v_speed = bullet.v_speed * (-1)
                            bullet.bounces += 1
                        if obstacle.y < bullet.y < obstacle.y + obstacle.height:
                            bullet.h_speed = bullet.h_speed * (-1)
                            bullet.bounces += 1
