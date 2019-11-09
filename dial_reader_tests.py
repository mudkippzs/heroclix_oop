import unittest
from dial_reader import DialReader
from exceptions import InvalidUnitIdError, InvalidClickNum

class DialReaderTestCase(unittest.TestCase):
	def setUp(self):
		super(DialReaderTestCase)
		self.test_unit_id = "wxm025"
		self.fake_unit_id = "wxm025a"

	def test_import_dial(self):
		self.assertTrue(DialReader)

	def test_dial_create_new_dial(self):
		dial = DialReader(self.test_unit_id)
		self.assertTrue(dial)

	def test_dial_create_new_dial_wrong_id(self):
		with self.assertRaises(InvalidUnitIdError):
			dial = DialReader("invalidID")     

	def test_dial_create_new_dial_wrong_id(self):
		with self.assertRaises(InvalidUnitIdError):
			dial = DialReader()     

	def test_unit_id_validate_from_local(self):
		# Validate real ID
		dial_real_id = DialReader(self.test_unit_id)
		self.assertTrue(dial_real_id.validate_id())

		# Validate false ID
		with self.assertRaises(InvalidUnitIdError) as context:
			dial_fake_id = DialReader(self.fake_unit_id)
			dial_fake_id.validate_id()

	def test_build_dial(self):
		dial = DialReader(self.test_unit_id)		
		expected_name = "Polaris"
		name_from_file = dial.get("name")		
		self.assertEqual(name_from_file, expected_name)

	def test_get_click_1(self):
		expected_base_speed = "8"
		expected_base_attack = "10"
		expected_base_defence = "17"
		expected_base_damage = "4" 
		expected_base_targets = "2"
		expected_base_range = 6  #TODO(make all dial values ints)
		
		dial = DialReader(self.test_unit_id)
		dial_click_1 = dial.get("dial")["click_1"]
		
		speed_val = dial_click_1["speed"]["value"][0]
		attack_val = dial_click_1["attack"]["value"][0]
		defence_val = dial_click_1["defense"]["value"][0]
		damage_val = dial_click_1["damage"]["value"][0]
		targets_val = dial.get("targets")
		range_val =  dial.get("range")

		self.assertEqual(expected_base_speed, speed_val)
		self.assertEqual(expected_base_attack, attack_val)
		self.assertEqual(expected_base_defence, defence_val)
		self.assertEqual(expected_base_damage, damage_val)
		self.assertEqual(expected_base_targets, targets_val)
		self.assertEqual(expected_base_range, range_val)

	def test_get_click_2(self):
		dial = DialReader(self.test_unit_id)
		click_2 = dial.get_click(2)

		expected_base_speed = "8"
		expected_base_attack = "9"
		expected_base_defence = "16"
		expected_base_damage = "3" 
		
		speed_val = click_2["speed"]["value"][0]
		attack_val = click_2["attack"]["value"][0]
		defence_val = click_2["defense"]["value"][0]
		damage_val = click_2["damage"]["value"][0]
		
		self.assertEqual(expected_base_speed, speed_val)
		self.assertEqual(expected_base_attack, attack_val)
		self.assertEqual(expected_base_defence, defence_val)
		self.assertEqual(expected_base_damage, damage_val)

	def test_get_out_of_bounds_click(self):
		with self.assertRaises(KeyError):
			dial = DialReader(self.test_unit_id)
			random_click = dial.get_click(200)

	def test_get_starting_click(self):
		dial = DialReader(self.test_unit_id).get("dial")		
		expected_starting_click = "click_1"
		first_click = next(iter(dial))
		self.assertEqual(expected_starting_click, first_click)

if __name__ == "__main__":
	unittest.main()