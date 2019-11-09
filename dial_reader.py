import json
import os
from exceptions import InvalidUnitIdError, InvalidClickNum

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

if __name__ == '__main__':
	pass