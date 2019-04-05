import variables as constants
import random

class Hero:
	"""docstring for Hero"""
	def __init__(self, map, picture):
		self.map = map
		self.picture = picture
		self.position = self.map.start
		self.win = 0 #0 = Null, 1 = Win, 2 = Loose
		self.objects_collected = False

	def move(self, direction):
		x = 0
		y = 0

		if direction == 'left':
			for location in list(self.position):
				while x < constants.NUMBER_SPRITES:
					while y < constants.NUMBER_SPRITES:
						if hash(location) == hash((x, y)):
							new_position = Position(x-1, y)
						y += 1
					x += 1
					y = 0
				x = 0
		elif direction == 'right':
			for location in list(self.position):
				while x < constants.NUMBER_SPRITES:
					while y < constants.NUMBER_SPRITES:
						if hash(location) == hash((x, y)):
							new_position = Position(x+1, y)
						y += 1
					x += 1
					y = 0
				x = 0
		elif direction == 'up':
			for location in list(self.position):
				while x < constants.NUMBER_SPRITES:
					while y < constants.NUMBER_SPRITES:
						if hash(location) == hash((x, y)):
							new_position = Position(x, y-1)
						y += 1
					x += 1
					y = 0
				x = 0
		elif direction == 'down':
			for location in list(self.position):
				while x < constants.NUMBER_SPRITES:
					while y < constants.NUMBER_SPRITES:
						if hash(location) == hash((x, y)):
							new_position = Position(x, y+1)	
						y += 1
					x += 1
					y = 0
				x = 0

		if new_position in self.map:
				self.position = {new_position}

		"""win = 1 if the player wins and win = 2 if the player looses"""
		if self.position == self.map.arrival and self.objects_collected == True:
			self.win = 1
		elif self.position == self.map.arrival and self.objects_collected == False:
			self.win = 2
		
class Position:
	"""Give the position"""
	def __init__(self, x, y):
		self.position = (x, y)

	def __repr__(self):
		return str(self.position)

	def __hash__(self):
		return hash(self.position)

	def __eq__(self, pos):
		return self.position == pos.position

class Guard:
	"""docstring for Guard"""
	def __init__(self, map, picture):
		self.map = map
		self.picture = picture
		self.position = self.map.arrival

		
class Object:
	"""docstring for Object"""
	def __init__(self, map, picture):
		self.map = map
		self.picture = picture
		self.list_positions = list(self.map.path)

		for location in self.list_positions:
			for loc in list(self.map.start):
				if hash(location) == hash(loc):
					self.list_positions.remove(location)

		for location in self.list_positions:
			for loc in list(self.map.arrival):
				if hash(location) == hash(loc):
					self.list_positions.remove(location)

		self.position = set()
		my_position = random.choice(self.list_positions)
		self.position.add(my_position)

		self.collected = False

		
class Map:
	"""docstring for Map"""
	def __init__(self, filename):
		self.filename = filename
		
		self.path = set()
		self.start = set()
		self.arrival = set()
		self.objects = set()

		self.load_from_file()

	def __contains__(self, position):
		return position in self.path

	def load_from_file(self):

		with open(self.filename) as infile:
			for x, line in enumerate(infile):
				for y, col in enumerate(line):
					if col == constants.PATH_CHAR:
						self.path.add(Position(x, y))
					elif col == constants.START_CHAR:
						self.start.add(Position(x, y))
						self.path.add(Position(x, y))
					elif col == constants.ARRIVAL_CHAR:
						self.arrival.add(Position(x, y))
						self.path.add(Position(x, y))


class Counter:
	"""docstring for Counter"""
	def __init__(self):
		self.counter = 3

	def count(self):
		if self.counter == 3:
			return constants.THREE
		elif self.counter == 2:
			return constants.TWO
		elif self.counter == 1:
			return constants.ONE
		elif self.counter == 0:
			return constants.ZERO