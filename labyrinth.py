#Libraries importation
import pygame
from pygame.locals import *

from functions import *
from variables import *

#Initialization of PyGame library
pygame.init()

#Window creation
game_window = pygame.display.set_mode((window_hor, window_vert))
#Icon
icon = pygame.image.load(icon_img)
pygame.display.set_icon(icon)
#Title
pygame.display.set_caption(window_title)

#Loading background
window_x = 0
window_y = 0

while window_x < window_hor:
	while window_y < window_vert:
		loading_background(game_window, window_x, window_y)
		window_y += 40
	window_x += 40
	window_y = 0

#Refreshing screen
pygame.display.flip()







#Variable qui continue la boucle si = 1, stoppe si = 0
keep_on = 1

while keep_on:
	for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
		if event.type == QUIT:     #Si un de ces événements est de type QUIT
			keep_on = 0      #On arrête la boucle