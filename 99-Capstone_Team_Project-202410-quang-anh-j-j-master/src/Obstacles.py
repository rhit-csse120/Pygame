import random

import pygame

from Obstacle import Obstacle


class Obstacles:
    def __init__(self, screen):
        self.image_1 = pygame.image.load("../media/pumpkin_1.png")
        self.image_2 = pygame.image.load("../media/pumpkin_2.png")
        self.image_3 = pygame.image.load("../media/ghost.png")
        self.list_image = [self.image_1, self.image_2, self.image_3]
        self.x = random.randrange(250, 350)
        self.y = random.randrange(190, 400)
        self.obstacles = []
        # construct obstacle
        for _ in range(1):
            for _ in range(2):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 85, 85,
                                               self.list_image[self.a]))
                self.y += 77

        self.x = random.randrange(500, 700)
        self.c = self.x
        self.y = random.randrange(450, 550)
        for i in range(2):
            for _ in range(2 - i):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 85, 85,
                                               self.list_image[self.a]))
                self.x += 75
            self.y += 75
            self.x = self.c + 75 / 2

        self.x = random.randrange(950, 1070)
        self.c = self.x
        self.y = random.randrange(150, 400)
        for _ in range(2):
            for _ in range(2):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 85, 85,
                                               self.list_image[self.a]))
                self.x += 75
            self.y += 75
            self.x = self.c

        self.x = random.randrange(550, 750)
        self.c = self.x
        self.y = random.randrange(135, 160)
        for _ in range(2):
            for _ in range(2):
                self.a = random.randint(0, 2)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 85, 85,
                                               self.list_image[self.a]))
                self.x += 75
            self.y += 75
            self.x = self.c
        # construct the field
        self.image1 = pygame.image.load("../media/obstacle 1.png")
        self.image2 = pygame.image.load("../media/obstacle 2.png")
        self.image3 = pygame.image.load("../media/obstacle 3.png")
        self.image4 = pygame.image.load("../media/obstacle 4.png")
        self.list = [self.image1, self.image2, self.image3, self.image4]
        self.x = 0
        self.y = 0
        for _ in range(2):
            for _ in range(11):
                self.b = random.randrange(0, 3)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 73, 73, self.list[self.b]))
                self.y += 73
            self.x += 1430
            self.y = 0
        self.x = 73
        for _ in range(2):
            for _ in range(17):
                self.b = random.randrange(0, 4)
                self.obstacles.append(Obstacle(screen, self.x, self.y, 80, 73,
                                               self.list[self.b]))
                self.x += 80
            self.x = 73
            self.y = 730

    def draw(self):
        for obstacle in self.obstacles:
            obstacle.draw()
