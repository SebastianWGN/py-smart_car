import pygame	
import time 	
import random 	
from gameLogic import game_loop

#initiate pygame
pygame.init()	

#display pygame
display = pygame.display.set_mode((1000,600))		#set width & height of display
pygame.display.set_caption("Colette")		#set window name

#game starts
game_loop(display)		
pygame.quit()	
quit()	#game is stop