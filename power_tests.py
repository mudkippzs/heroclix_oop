from power import Power
import unittest
from exceptions import InvalidPowerArgs


class PowerTestCases(unittest.TestCase):
	
	def test_power_import(self):
		self.assertIsNotNone(Power)

	def test_create_power(self):
		with self.assertRaises(InvalidPowerArgs):
			new_power = Power()

	def test_create_power_with_args(self):
		args = {'name': 'charge', 'rule': 'Can move at half speed (rnd up) and then attack!', 'colour': 'green'}
		new_power = Power(**args)
		self.assertIsNotNone(new_power)


if __name__ == '__main__':
	unittest.main()