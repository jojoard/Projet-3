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

	#Sound
	sound = pygame.mixer.Sound(constants.SOUND)

	#Infinite loop
	keep_on = 1
	while keep_on:

		#Loading the welcome screen
		welcome = pygame.image.load(constants.WELCOME_IMG).convert()
		game_window.blit(welcome, (88,153)) #Load welcome background

		#Screen refresh
		pygame.display.flip()

		#Constants
		keep_on_welcome = 1 #To keep on the welcome page
		keep_on_game = 1 #To keep on the game page
		level = 0

		sound.play()

		while keep_on_welcome:

			for event in pygame.event.get():
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					keep_on_game = 0      #Stop the loop
					keep_on_welcome = 0
					keep_on = 0
					sound.stop()
					
				elif event.type == KEYDOWN:				
					#Loading the level 1
					if event.key == K_F1:
						keep_on_welcome = 0	
						level = 1
						

		if level != 0: #To be sure there is a level selected
			"""Creating the different objects and loading the pictures of the game"""
			my_map = Map("levels/level1.txt")
			hero = Hero(my_map, constants.MCGYVER_IMG)
			guard = Guard(my_map, constants.GUARD_IMG)
			ether = Object(my_map, constants.ETHER_IMG)
			tube = Object(my_map, constants.TUBE_IMG)
			needle = Object(my_map, constants.NEEDLE_IMG)
			objList = [ether, tube, needle]
			counter_objects = Counter()
			loading_background(game_window)
			loading_path(game_window, list(my_map.path))
			picking_object(hero, objList, game_window, counter_objects)
			loading_character(game_window, hero)
			loading_character(game_window, guard)
			loading_object(game_window, ether)
			loading_object(game_window, tube)
			loading_object(game_window, needle)
			pygame.display.flip()

		while keep_on_game:

			for event in pygame.event.get():   
				if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
					keep_on_game = 0
					keep_on_welcome = 1
					game_window.fill((0,0,0)) #Erase the background
				elif event.type == KEYDOWN:
					if event.key == K_RIGHT:
						hero.move('right') #If the hero moves on the right
					elif event.key == K_LEFT:
						hero.move('left')
					elif event.key == K_UP:
						hero.move('up')
					elif event.key == K_DOWN:
						hero.move('down')

					loading_background(game_window)
					loading_path(game_window, list(my_map.path))
					picking_object(hero, objList, game_window, counter_objects)
					loading_character(game_window, hero)
					loading_character(game_window, guard)
					loading_object(game_window, ether)
					loading_object(game_window, tube)
					loading_object(game_window, needle)
					if hero.win == 1:
						game_window.fill((0,0,0)) #Erase the background
						winner = pygame.image.load(constants.WINNER_IMG).convert()
						game_window.blit(winner, (6, 200))
					elif hero.win == 2:
						game_window.fill((0,0,0)) #Erase the background
						looser = pygame.image.load(constants.GAME_OVER_IMG).convert()
						game_window.blit(looser, (6, 200))
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

	#pygame.display.flip()

def loading_path(window, list_tuples):
	game_path = pygame.image.load(constants.PATH_IMG).convert()
	x = 0
	y = 0

	for location in list_tuples:
		window.blit(game_path, (location.position[0] * constants.SPRITE_SIZE, location.position[1] * constants.SPRITE_SIZE))

	#pygame.display.flip()

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

	#pygame.display.flip()


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
		#pygame.display.flip()

def picking_object(hero, objList, window, counter):

	collectedAll = True

	for obj in objList:
		if hero.position == obj.position:
			if obj.collected == False:
				counter.counter -= 1
			obj.collected = True

		if obj.collected == False:
			collectedAll = False

	hero.objects_collected = collectedAll

	counter_picture = pygame.image.load(counter.count()).convert_alpha()
	window.blit(counter_picture, (0, 0))