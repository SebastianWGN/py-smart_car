import pygame

from models.object import Object


class Obstacle(Object):
    def __init__(self, x, y, width, height, obstacleType, speed):
        Object.__init__(self, x, y, width, height)
        self.obstacleType = obstacleType
        self.image = None
        self.speed = speed



    def draw(self, display):

        if self.obstacleType == 0:
            self.image = pygame.image.load("assets/loli2.png")
        if self.obstacleType == 1:
            self.image = pygame.image.load("assets/loli1.png")
        if self.obstacleType == 2:
            self.image = pygame.image.load("assets/loli1.png")
        display.blit(self.image, (self.x, self.y))

    def setObstacleType(self, obstacleType):
        self.obstacleType = obstacleType

    def goDown(self):
        self.y -= self.speed / 4