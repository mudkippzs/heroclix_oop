import json
import os
import random


class InvalidUnitIdError(Exception):

	def __init__(self):
		super(InvalidUnitIdError)

class InvalidClickNum(Exception):

	def __init__(self):
		super(InvalidClickNum)


class DialReader:	
	attributes = {}

	unit_id = None
	_local_base_path = os.path.dirname(os.path.abspath(__file__))
	_local_file_path = None

	def __init__(self, unit_id):
		self.unit_id = unit_id
		self._local_file_path = self._local_base_path + '\\data\\' + self.unit_id + '.json'
		if self.validate_id() is False:
			raise InvalidUnitIdError
		else:
			self.build_dial()

	def get(self, attr):
		return self.attributes[attr]

	def validate_id(self):
		id_to_check = self.unit_id or None
		if id_to_check:
			try:
				os.path.getsize(self._local_file_path)				
			except os.error as e:
				raise e

			return True
		else:
			return False

	def build_dial(self):
		with open(self._local_file_path) as local_json:
			self.attributes = json.loads(local_json.read())

	def get_click(self, click_num):
		try:
			if self.attributes:
				click = self.attributes["dial"]["click_" + str(click_num)]
				if click:
					return click
		except InvalidClickNum as e:
			raise e


class Dial:

	
	@property
	def move_value(self):
		return int(self.current_click["speed"]["value"][0])
	
	@property
	def attack_value(self):		
		return int(self.current_click["attack"]["value"][0])

	@property
	def defense_value(self):
		return int(self.current_click["defense"]["value"][0])

	@property
	def damage_value(self):
		return int(self.current_click["damage"]["value"][0])
	
	@property
	def current_click(self):
		return self.dial["click_" + str(self.damage_received + 1)]

	@property
	def is_ko(self):
		return True if self.damage_received >= self.dial_size else False
	
	def __init__(self, dial_data):
		self.set_name(dial_data)
		self.set_id(dial_data)
		self.set_set(dial_data)
		self.set_cost(dial_data)
		self.set_targets(dial_data)
		self.set_dial(dial_data)
		self.set_range(dial_data)	
		self.dial_size = len(dial_data.get("dial")) - 1
		self.damage_received = 0

	def set_name(self, dial_data):
		self.name = dial_data.get("name")

	def set_id(self, dial_data):
		self.id = dial_data.get("id")

	def set_set(self, dial_data):
		self.set = dial_data.get("set")

	def set_cost(self, dial_data):
		self.cost = dial_data.get("points")

	def set_targets(self, dial_data):
		self.targets = dial_data.get("targets")

	def set_range(self, dial_data):
		self.range = dial_data.get("range")
	
	def set_dial(self, dial_data):
		self.dial = dial_data.get("dial")

	def get_current_click(self):
		return {
				'move': {'value': self.move_value,},
				'attack': {'value': self.attack_value,},
				'defense': {'value': self.defense_value,},
				'damage': {'value': self.damage_value,},
				}

	def roll(self, n):		
		rolled = 0
		result = []
		while rolled < n:
			result.append(random.randint(1,6))
			rolled = rolled +1

		return int(sum(map(int, result)))

	def roll_to_hit(self, target):
		attack_roll = self.roll(2) + int(self.attack_value)
		if attack_roll > target.defense_value:
			return True
		return False

	def add_damage(self, damage):
		self.damage_received = self.damage_received + damage

	def heal_damage(self, heal):
		self.damage_received = damage_received - heal

	def calculate_damage(self):
		return self.damage_value


