import exceptions
import json
import os
import random
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

if __name__ == '__main__':
	pass