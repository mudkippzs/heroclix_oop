from maps import Map

class Game():

	def __init__(self, name='Unnamed Game', map_name=None):
		self.name = name
		if map_name:
			self.map_name = map_name
		else:
			self.map_name = 'savage_land' # Default Map

		self.set_map()

	def set_map(self):
		self.game_map = Map(self.map_name)


