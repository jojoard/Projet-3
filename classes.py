import variables as constants

class Hero:
	"""docstring for Hero"""
	def __init__(self, map):
		self.map = map
		self.position = self.map.start

	def move(self, direction):
		"""getattr() can access an object property using a string"""
		new_position = getattr(self.position, direction)()
		if new_position in self.map:
			self.position = new_position
		


class Position:
	"""Give the position of Mc Gyver"""
	def __init__(self, x, y):
		self.position = (x, y)

	def __repr__(self):
		return str(self.position)

	def __hash__(self):
		return hash(self.position)

	def __eq__(self, pos):
		return self.position == pos.position

	def up(self):
		x, y = self.position
		return Position(x-1, y)

	def down(self):
		x, y = self.position
		return Position(x+1, y)

	def right(self):
		x, y = self.position
		return Position(x, y+1)

	def left(self):
		x, y = self.position
		return Position(x, y-1)
		


class Guard:
	"""docstring for Guard"""
	def __init__(self, arg):
		super(Guard, self).__init__()
		self.arg = arg
		


class Object:
	"""docstring for Object"""
	def __init__(self, arg):
		super(Object, self).__init__()
		self.arg = arg
		


class Map:
	"""docstring for Map"""
	def __init__(self, filename):
		self.filename = filename
		
		self._path = set()
		self._start = set()
		self._end = set()
		self.objects = set()

		self.load_from_file()

	@property
	def start(self):
		return list(self._start)[0]

	@property
	def end(self):
		return list(self._end)[0]

	def __contains__(self, position):
		return position in self._path

	def load_from_file(self):

		with open(self.filename) as infile:
			for x, line in enumerate(infile):
				for y, col in enumerate(line):
					if col == constants.PATH_CHAR:
						self._path.add(Position(x, y))
					elif col == constants.START_CHAR:
						self._start.add(Position(x, y))
						self._path.add(Position(x, y))
					elif col == constants.ARRIVAL_CHAR:
						self._end.add(Position(x, y))
						self._path.add(Position(x, y))




def main():
	map = Map("levels/level1.txt")

	p = Position(3, 2)
	print(p in map)

	h = Hero
	print(h in map)

if __name__ == '__main__':
	main()