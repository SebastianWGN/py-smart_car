import pygame
import time


#colours
grey = (118,119,110)	
white =(255,255,255)
black = (0,0,0)	


def message_display(text, display):		#create function for message edit
	largetext=pygame.font.Font("freesansbold.ttf",80)	#message in this style and the size will be 80
	textsurf,textrect=text_object(text,largetext, black)	#create function to edit message 
	textrect.center=((400),(300))	#show the message position in display
	display.blit(textsurf,textrect)	#display this message 
	pygame.display.update()	#update display
	#time.sleep(1)		#after crashed 1 sec restart the game

def generation_message_display(text, display):		#create function for message edit
	largetext=pygame.font.Font("freesansbold.ttf",20)	#message in this style and the size will be 80
	textsurf,textrect=text_object(text,largetext, white)	#create function to edit message 
	textrect=((10),(450))	#show the message position in display
	display.blit(textsurf,textrect)	#display this message 

def genoma_message_display(text, display):		#create function for message edit
	largetext=pygame.font.Font("freesansbold.ttf",20)	#message in this style and the size will be 80
	textsurf,textrect=text_object(text,largetext, white)	#create function to edit message 
	textrect=((10),(480))	#show the message position in display
	display.blit(textsurf,textrect)	#display this message 

def time_message_display(text, display):		#create function for message edit
	largetext=pygame.font.Font("freesansbold.ttf",20)	#message in this style and the size will be 80
	textsurf,textrect=text_object(text,largetext, white)	#create function to edit message 
	textrect=((10),(510))	#show the message position in display
	display.blit(textsurf,textrect)	#display this message 



def text_object(text,font, color):		#display after crash the car
	textsurface=font.render(text,True, color)	#display in this colour
	return textsurface,textsurface.get_rect()	#after that restart the game & ready to give some input