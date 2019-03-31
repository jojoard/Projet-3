"""Functions of the game"""

import pygame
from pygame.locals import * 

import variables as constants
from classes import *

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

	keep_on = 1
	while keep_on:

		#Loading the welcome screen
		welcome = pygame.image.load(constants.WELCOME_IMG).convert()
		game_window.blit(welcome, (88,153))

		#Screen refresh
		pygame.display.flip()

		#Constants
		keep_on_welcome = 1
		keep_on_game = 1
		level = 0

		while keep_on_welcome:

			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					keep_on_game = 0      #Stop the loop
					keep_on_welcome = 0
					keep_on = 0
					
				elif event.type == KEYDOWN:				
					#Loading the level 1
					if event.key == K_F1:
						keep_on_welcome = 0	
						level = 1
						my_map = Map("levels/level1.txt")
						hero = Hero(my_map)
						guard = Guard(my_map)
					#Loading the level 2
					elif event.key == K_F2:
						keep_on_welcome = 0
						level = 2
						my_map = Map("levels/level2.txt")
						hero = Hero(my_map)
						guard = Guard(my_map)


		if level != 0: #To be sure there is a level selected
			loading_background(game_window)
			loading_path(game_window, list(my_map.path))
			loading_hero(game_window, list(hero.position))
			loading_guard(game_window, list(guard.position))


		while keep_on_game:

			for event in pygame.event.get():   
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					keep_on_game = 0
					keep_on = 0
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT:
						hero.move()
						pygame.display.flip()
					elif event.key == K_LEFT:
						hero.move.left()
						pygame.display.flip()
					elif event.key == K_UP:
						hero.move.up()
						pygame.display.flip()
					elif event.key == K_DOWN:
						hero.move.down()
						pygame.display.flip()

#Function for loading background
def loading_background(window):
	game_background = pygame.image.load(constants.WALL_IMG).convert()
	x = 0
	y = 0

	while x < constants.NUMBER_SPRITES * constants.SPRITE_SIZE:
		while y < constants.NUMBER_SPRITES * constants.SPRITE_SIZE:
			window.blit(game_background, (x, y))
			y += 40
		x += 40
		y = 0

	pygame.display.flip()

def loading_path(window, list_tupples):
	game_path = pygame.image.load(constants.PATH_IMG).convert()
	x = 0
	y = 0

	for location in list_tupples:
		while x < constants.NUMBER_SPRITES:
			while y < constants.NUMBER_SPRITES:
				if hash(location) == hash((x, y)):
					window.blit(game_path, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				y += 1
			x += 1
			y = 0
		x = 0
	
	pygame.display.flip()

def loading_hero(window, list_tupples):
	game_hero = pygame.image.load(constants.MCGYVER_IMG).convert()
	x = 0
	y = 0

	for location in list_tupples:
		while x < constants.NUMBER_SPRITES:
			while y < constants.NUMBER_SPRITES:
				if hash(location) == hash((x, y)):
					window.blit(game_hero, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				y += 1
			x += 1
			y = 0
		x = 0

	pygame.display.flip()

def loading_guard(window, list_tupples):
	game_guard = pygame.image.load(constants.GUARD_IMG).convert()
	x = 0
	y = 0

	for location in list_tupples:
		while x < constants.NUMBER_SPRITES:
			while y < constants.NUMBER_SPRITES:
				if hash(location) == hash((x, y)):
					window.blit(game_guard, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				y += 1
			x += 1
			y = 0
		x = 0
	
	pygame.display.flip()

#Function for loading a character or an object
def loading_character_object(window, x_position, y_position, character_object_file):
	game_character_object = pygame.image.load(character_object_file).convert_alpha()
	window.blit(game_character_object, (x_position,y_position))


	

