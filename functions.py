"""Functions of the game"""

import pygame
from pygame.locals import * 

import variables as constants

#Loading the game
def load_pygame():
	#Initialization of PyGame library
	pygame.init()

	#Window creation
	game_window = pygame.display.set_mode((constants.NUMBER_SPRITES * constants.SPRITE_SIZE, constants.NUMBER_SPRITES * constants.SPRITE_SIZE))
	#Icon
	icon = pygame.image.load(constants.ICON_IMG)
	pygame.display.set_icon(icon)
	#Title
	pygame.display.set_caption(constants.WINDOW_TITLE)

	#Loading background
	window_x = 0
	window_y = 0

	while window_x < constants.NUMBER_SPRITES * constants.SPRITE_SIZE:
		while window_y < constants.NUMBER_SPRITES * constants.SPRITE_SIZE:
			loading_background(game_window, window_x, window_y)
			window_y += 40
		window_x += 40
		window_y = 0

	#Refreshing screen
	pygame.display.flip()

#Function for loading background
def loading_background(window, x_position, y_position):
	game_background = pygame.image.load(constants.WALL_IMG).convert()
	window.blit(game_background, (x_position,y_position))

#Function for loading a character or an object
def loading_character_object(window, x_position, y_position, character_object_file):
	game_character_object = pygame.image.load(character_object_file).convert_alpha()
	window.blit(game_character_object, (x_position,y_position))


	

