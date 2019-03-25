"""Functions of the game"""

import pygame
from pygame.locals import * 

from variables import *

#Function for loading background
def loading_background(window, x_position, y_position):
	game_background = pygame.image.load(background_img).convert()
	window.blit(game_background, (x_position,y_position))

#Function for loading a character or an object
def loading_character_object(window, x_position, y_position, character_object_file):
	game_character_object = pygame.image.load(character_object_file).convert_alpha()
	window.blit(game_character_object, (x_position,y_position))

def character_move():
	

