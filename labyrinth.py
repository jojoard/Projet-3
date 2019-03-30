#Libraries importation
#import pygame
#from pygame.locals import *
import os

from classes import *
from functions import *

os.chdir("C:/Users/Jonathan/OneDrive/OpenClassrooms/Projet 3/Projet-3")

def main():
	map = Map("levels/level1.txt")

	h = Hero
	print(h.position)

	"""load_pygame()
			
				#Variable qui continue la boucle si = 1, stoppe si = 0
				keep_on = 1
			
				while keep_on:
					for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
						if event.type == QUIT:     #Si un de ces événements est de type QUIT
							keep_on = 0      #On arrête la boucle"""


if __name__ == '__main__':
	main()
