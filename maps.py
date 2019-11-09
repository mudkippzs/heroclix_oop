from exceptions import InvalidMapID
import json

class Map():

	@property
	def map_id(self):
		return self.map_selected

	def __init__(self, map_id=None):
		with open("map_index.json") as map_index_json:
			self.map_list = json.loads(map_index_json.read())

		if map_id:
			if self.map_id_valid(map_id):
				self.set_selected_map(map_id)
			else:
				raise InvalidMapID		

	def list_maps(self):
		listOfMaps = []
		for map_meta in self.map_list["maps"]:
			listOfMaps.append((map_meta["id"], map_meta["name"]))
		return listOfMaps

	def map_id_valid(self, map_id):
		for map_meta in self.map_list["maps"]:
			if map_id in map_meta["id"]:
				return True
		return False

	def set_selected_map(self, map_id):
		self.map_selected = map_id