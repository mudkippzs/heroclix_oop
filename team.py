from exceptions import InvalidUnitDataType, TeamPointLimitOutOfRange, DialListCostTooHigh
from dial import Dial

class Team:

	roster = []
	sideteam = []
	
	@property
	def max_points(self):
		return self.point_limit	
	
	def __init__(self, dials = None, points = 300, sideteam = None):

		if points > 0 and points < 5000:
			self.points = points
		else:
			raise TeamPointLimitOutOfRange
		
		self.point_limit = self.points

		if dials:
			if isinstance(dials, list):
				if self.check_list_point_limit(dials):
					self.add_list_of_units(dials)
				else:
					raise DialListCostTooHigh
			elif isinstance(dials, Dial):
				self.add_unit(dials)
			else:
				raise InvalidUnitDataType

		if sideteam:
			if isinstance(sideteam, list):
				self.add_list_of_units_to_sideteam(sideteam)				
			elif isinstance(sideteam, Dial):
				self.add_unit_to_sideteam(sideteam)
			else:
				raise InvalidUnitDataType


	def add_unit(self, dial):
		self.points = self.points - dial.cost
		self.roster.append(dial)

	def add_list_of_units(self, ListOfDials):
		for dial in ListOfDials:
			self.add_unit(dial)

	def add_unit_to_sideteam(self, dial):
		self.sideteam.append(dial)

	def add_list_of_units_to_sideteam(self, ListOfDials):
		for dial in ListOfDials:
			self.add_unit_to_sideteam(dial)

	def check_list_point_limit(self, ListOfDials):
		total = 0
		for dial in ListOfDials:
			total = total + dial.cost

		return False if total > self.max_points else True

