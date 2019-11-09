from exceptions import InvalidMapID
from maps import Map
import unittest

class MapsTestCase(unittest.TestCase):
	
	def test_import_map(self):
		self.assertIsNotNone(Map)

	def test_new_map_no_id(self):
		new_map = Map()

	def test_select_map_invalid_id(self):
		with self.assertRaises(InvalidMapID):
			new_map = Map('wwwwwwww')

	def test_select_map(self):
		new_map = Map('wcr0')
		self.assertIsNotNone(new_map.map_id)

	def test_list_maps(self):
		new_map = Map('wcr0')
		list_of_maps = new_map.list_maps()
		list_of_maps_top = list_of_maps[0]
		self.assertTrue(isinstance(list_of_maps_top, tuple))		
		self.assertEqual(2, len(list_of_maps_top))		
		self.assertTrue(isinstance(list_of_maps_top[0], str))
		self.assertTrue(isinstance(list_of_maps_top[1], str))



if __name__ == '__main__':
	unittest.main()