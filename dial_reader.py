import json
import os
from exceptions import InvalidUnitIdError, InvalidClickNum

class DialReader:	
	attributes = {}

	unit_id = None
	_local_base_path = os.path.dirname(os.path.abspath(__file__))
	_local_file_path = None

	def __init__(self, unit_id=None):
		self.unit_id = unit_id
		try:
			if self.validate_id():
				self.build_dial()
		except:
			raise InvalidUnitIdError

	def get(self, attr):
		return self.attributes[attr]

	def validate_id(self):
		self._local_file_path = self._local_base_path + '\\data\\' + self.unit_id + '.json'			
		if self._local_file_path:
			try:
				os.path.getsize(self._local_file_path)				
			except os.error as e:
				raise e
			return True

	def build_dial(self):
		with open(self._local_file_path) as local_json:
			self.attributes = json.loads(local_json.read())

	def get_click(self, click_num):
		if self.attributes:
			try:
				return self.attributes["dial"]["click_" + str(click_num)]				
			except KeyError as e:
					raise e

if __name__ == '__main__':
	pass