from dial import Dial, DialReader
import unittest


class DialTestCase(unittest.TestCase):
	def setUp(self):
		super(DialTestCase)
		self.test_id = "wxm026"
		self.attacker_test_id = "wxm028"
		self.target_test_id = "wxm024"

		self.dial_data = DialReader(self.test_id)
		self.attacker_dial_data = DialReader(self.attacker_test_id)
		self.target_dial_data = DialReader(self.target_test_id)

	def test_create_dial(self):
		dial = Dial(self.dial_data)
		self.assertIsInstance(dial, Dial)

	def test_dial_roll(self):
		dial = Dial(self.dial_data)
		roll = 0				
		self.assertIsNotNone(roll)
		self.assertIsInstance(roll, int)

	def test_set_name(self):
		dial = Dial(self.dial_data)
		name = self.dial_data.get("name")
		dial.set_name(self.dial_data)
		self.assertEqual(name, dial.name)

	def test_set_id(self):
		dial = Dial(self.dial_data)
		uid = self.dial_data.get("id")
		dial.set_id(self.dial_data)
		self.assertEqual(uid, dial.id)

	def test_set_set(self):
		dial = Dial(self.dial_data)
		setid = self.dial_data.get("set")
		dial.set_set(self.dial_data)
		self.assertEqual(setid, dial.set)

	def test_set_cost(self):
		dial = Dial(self.dial_data)
		cost = self.dial_data.get("points")
		dial.set_cost(self.dial_data)
		self.assertEqual(cost, dial.cost)

	def test_set_targets(self):
		dial = Dial(self.dial_data)
		targets = self.dial_data.get("targets")
		dial.set_targets(self.dial_data)
		self.assertEqual(targets, dial.targets)

	def test_set_range(self):
		dial = Dial(self.dial_data)
		rangeval = self.dial_data.get("range")
		dial.set_range(self.dial_data)
		self.assertEqual(rangeval, dial.range)
	
	def test_make_attack(self):		
		attacker_dial = Dial(self.attacker_dial_data)
		target_dial = Dial(self.target_dial_data)
		
		attack_roll = attacker_dial.roll_to_hit(target_dial) 
		if attack_roll:
			attack_damage = attacker_dial.calculate_damage()			
			target_dial.add_damage(attack_damage)
		
		self.assertIsNotNone(attack_roll)

	def test_ko_flag(self):
		testUnit = Dial(self.attacker_dial_data)
		testUnit.add_damage(len(self.attacker_dial_data.get("dial"))-1)		
		self.assertTrue(testUnit.is_ko)

	def test_print_get_click(self):
		dial = Dial(self.dial_data)
		current_click = dial.get_current_click()

		self.assertIsInstance(current_click, dict)


class DialReaderTestCase(unittest.TestCase):
	def setUp(self):
		super(DialTestCase)
		self.test_unit_id = "wxm025"
		self.fake_unit_id = "wxm025a"

	def test_import_dial(self):
		self.assertTrue(DialReader)

	def test_dial_create_new_dial(self):
		dial = DialReader(self.test_unit_id)
		self.assertTrue(dial)

	def test_unit_id_validate_from_local(self):
		# Validate real ID
		dial_real_id = DialReader(self.test_unit_id)
		self.assertTrue(dial_real_id.validate_id())

		# Validate false ID
		with self.assertRaises(FileNotFoundError) as context:
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

	def test_get_starting_click(self):
		dial = DialReader(self.test_unit_id).get("dial")		
		expected_starting_click = "click_1"
		first_click = next(iter(dial))
		self.assertEqual(expected_starting_click, first_click)

		
if __name__ == "__main__":
	unittest.main()