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
		game_window.blit(welcome, (88,153)) #Load welcome background

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
						hero = Hero(my_map, constants.MCGYVER_IMG)
						guard = Guard(my_map, constants.GUARD_IMG)
						ether = Object(my_map, constants.ETHER_IMG)
						tube = Object(my_map, constants.TUBE_IMG)
						needle = Object(my_map, constants.NEEDLE_IMG)

		if level != 0: #To be sure there is a level selected
			loading_background(game_window)
			loading_path(game_window, list(my_map.path))
			loading_character(game_window, hero)
			loading_character(game_window, guard)
			loading_object(game_window, ether)
			loading_object(game_window, tube)
			loading_object(game_window, needle)
			#game_object = pygame.image.load(constants.NEEDLE_IMG).convert_alpha()
			#game_window.blit(game_object, (1 * 40 , 2 * 40))

		while keep_on_game:

			for event in pygame.event.get():   
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					keep_on_game = 0
					keep_on_welcome = 1
					game_window.fill((0,0,0)) #Erase the background
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT:
						hero.move('right')
						loading_path(game_window, list(my_map.path))
						loading_character(game_window, hero)
						loading_character(game_window, guard)
						loading_object(game_window, ether)
						loading_object(game_window, tube)
						loading_object(game_window, needle)
						if hero.win == True:
							game_window.fill((0,0,0)) #Erase the background
							winner = pygame.image.load(constants.WINNER_IMG).convert()
							game_window.blit(winner, (6, 200))
						pygame.display.flip()
					elif event.key == K_LEFT:
						hero.move('left')
						loading_path(game_window, list(my_map.path))
						loading_character(game_window, hero)
						loading_character(game_window, guard)
						loading_object(game_window, ether)
						loading_object(game_window, tube)
						loading_object(game_window, needle)
						if hero.win == True:
							game_window.fill((0,0,0)) #Erase the background
							winner = pygame.image.load(constants.WINNER_IMG).convert()
							game_window.blit(winner, (6, 200))
						pygame.display.flip()
					elif event.key == K_UP:
						hero.move('up')
						loading_path(game_window, list(my_map.path))
						loading_character(game_window, hero)
						loading_character(game_window, guard)
						loading_object(game_window, ether)
						loading_object(game_window, tube)
						loading_object(game_window, needle)
						if hero.win == True:
							game_window.fill((0,0,0)) #Erase the background
							winner = pygame.image.load(constants.WINNER_IMG).convert()
							game_window.blit(winner, (6, 200))
						pygame.display.flip()
					elif event.key == K_DOWN:
						hero.move('down')
						loading_path(game_window, list(my_map.path))
						loading_character(game_window, hero)
						loading_character(game_window, guard)
						loading_object(game_window, ether)
						loading_object(game_window, tube)
						loading_object(game_window, needle)
						if hero.win == True:
							game_window.fill((0,0,0)) #Erase the background
							winner = pygame.image.load(constants.WINNER_IMG).convert()
							game_window.blit(winner, (6, 200))
						pygame.display.flip()

#Function for loading background
def loading_background(window):
	game_background = pygame.image.load(constants.WALL_IMG).convert()
	x = 0
	y = 0

	while x < constants.NUMBER_SPRITES:
		while y < constants.NUMBER_SPRITES:
			window.blit(game_background, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
			y += 1
		x += 1
		y = 0

	pygame.display.flip()

def loading_path(window, list_tuples):
	game_path = pygame.image.load(constants.PATH_IMG).convert()
	x = 0
	y = 0

	for location in list_tuples:
		while x < constants.NUMBER_SPRITES:
			while y < constants.NUMBER_SPRITES:
				if hash(location) == hash((x, y)):
					window.blit(game_path, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				y += 1
			x += 1
			y = 0
		x = 0
	
	pygame.display.flip()

def loading_character(window, char_to_load):
	game_hero = pygame.image.load(char_to_load.picture).convert_alpha()
	x = 0
	y = 0

	for location in char_to_load.position:
		while x < constants.NUMBER_SPRITES:
			while y < constants.NUMBER_SPRITES:
				if hash(location) == hash((x, y)):
					window.blit(game_hero, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
				y += 1
			x += 1
			y = 0
		x = 0

	pygame.display.flip()


#Function for loading an object
def loading_object(window, object_to_load):
	game_object = pygame.image.load(object_to_load.picture).convert_alpha()
	x = 0
	y = 0

	if object_to_load.collected == False:
		for location in object_to_load.position:
			while x < constants.NUMBER_SPRITES:
				while y < constants.NUMBER_SPRITES:
					if hash(location) == hash((x, y)):
						window.blit(game_object, (x * constants.SPRITE_SIZE, y * constants.SPRITE_SIZE))
					y += 1
				x += 1
				y = 0
			x = 0
		pygame.display.flip()

