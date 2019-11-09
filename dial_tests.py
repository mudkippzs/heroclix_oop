from dial import Dial
from dial_reader import DialReader
from unittest import mock
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
	
	@mock.patch.object(Dial, 'roll')
	def test_make_attack_hits(self, mockRoll):		
		attacker_dial = Dial(self.attacker_dial_data)
		target_dial = Dial(self.target_dial_data)
		mockRoll.return_value = 2 # will miss

		attack_roll = attacker_dial.roll_to_hit(target_dial) 
		if attack_roll:		
			attack_damage = attacker_dial.calculate_damage()			
			target_dial.add_damage(attack_damage)
		
		self.assertFalse(attack_roll)

	@mock.patch.object(Dial, 'roll')
	def test_make_attack_misses(self, mockRoll):
		attacker_dial = Dial(self.attacker_dial_data)
		target_dial = Dial(self.target_dial_data)
		mockRoll.return_value = 12 # will hit

		attack_roll = attacker_dial.roll_to_hit(target_dial) 
		if attack_roll:
			attack_damage = attacker_dial.calculate_damage()			
			target_dial.add_damage(attack_damage)
				
		self.assertTrue(attack_roll)

	def test_roll(self):
		testUnit = Dial(self.attacker_dial_data)
		roll = testUnit.roll(2)
		self.assertGreater(roll, 0)
		self.assertLess(roll, 13)

	def test_add_damage(self):
		testUnit = Dial(self.attacker_dial_data)
		testUnit.add_damage(1)
		self.assertEqual(1, testUnit.damage_received)		
	
	def test_heal_damage(self):
		testUnit = Dial(self.attacker_dial_data)
		testUnit.add_damage(3)
		testUnit.heal_damage(2)
		self.assertEqual(1, testUnit.damage_received)

	
	def test_ko_flag(self):
		testUnit = Dial(self.attacker_dial_data)
		testUnit.add_damage(len(self.attacker_dial_data.get("dial"))-1)		
		self.assertTrue(testUnit.is_ko)

	def test_print_get_click(self):
		dial = Dial(self.dial_data)
		current_click = dial.get_current_click()

		self.assertIsInstance(current_click, dict)
		
if __name__ == "__main__":
	unittest.main()