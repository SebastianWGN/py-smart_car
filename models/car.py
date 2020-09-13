import pygame

from message import message_display
from models.object import Object


class Car(Object):

    def __init__(self, x, y, width, height=150):
        Object.__init__(self, x, y, width, height)
        self.image = pygame.image.load("assets/icar2.png")


    def draw(self, display):
        display.blit(self.image, (self.x,self.y))

    def move(self, direction):
        if direction == -1:
            self.x -= (self.width + 60)
        elif direction == 1:
            self.x += (self.width + 60)

    def crash(self, display):
        message_display("Car Crashed", display)
