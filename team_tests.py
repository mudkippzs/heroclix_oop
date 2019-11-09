from dial import Dial
from dial_reader import DialReader
from exceptions import DialListCostTooHigh, TeamPointLimitOutOfRange, InvalidUnitDataType
from team import Team
import unittest

class TeamsTestCase(unittest.TestCase):
	
	def setUp(self):
		super(TeamsTestCase)
		dial_1_id = "wxm034"		
		dial_2_id = "wxm031"
		dial_3_id = "wxm024"
		dial_4_id = "wxm024"
		dial_5_id = "wxm023a"
		dial_6_id = "wxm026"


		self.dial_1_data = DialReader(dial_1_id)
		self.dial_2_data = DialReader(dial_2_id)
		self.dial_3_data = DialReader(dial_3_id)

		self.dial_side_1_data = DialReader(dial_4_id)
		self.dial_side_2_data = DialReader(dial_5_id)
		self.dial_side_3_data = DialReader(dial_6_id)		

	def test_import_team_module(self):		
		self.assertTrue(Team)

	def test_create_empty_team_legal_points(self):
		team = Team(points=300)
		teamSize = team.max_points
		self.assertEqual(teamSize, 300)

	def test_create_empty_team_illegal_points(self):
		with self.assertRaises(TeamPointLimitOutOfRange):
			team = Team(points=8700)		

	def test_create_team_to_big(self):
		dials = [
			Dial(self.dial_1_data), 
			Dial(self.dial_2_data), 
			Dial(self.dial_3_data)
			]

		with self.assertRaises(DialListCostTooHigh):
			team = Team(dials)

	def test_create_team_from_list(self):
		dials = [
			Dial(self.dial_1_data),
			Dial(self.dial_2_data)
		]

		team = Team(dials)
		self.assertLess(team.points, team.max_points)
	
	def test_create_team_from_dial(self):
		dial = Dial(self.dial_1_data)
		team = Team(dials = dial, points = 300, sideteam = [])
		self.assertLess(team.points, team.max_points)


	def test_create_team(self):
		dial = True
		with self.assertRaises(InvalidUnitDataType):
			team = Team(dial)


	def test_add_to_sideteam_single_dial(self):
		dial = Dial(self.dial_side_1_data)
		dials = [
			Dial(self.dial_1_data),
			Dial(self.dial_2_data)
		]

		team = Team(dials=dials, points= 300, sideteam=dial)


	def test_add_to_sideteam(self):
		dials = [
			Dial(self.dial_1_data),
			Dial(self.dial_2_data)
		]

		sidedials = [
			Dial(self.dial_side_1_data),
			Dial(self.dial_side_2_data),
			Dial(self.dial_side_3_data)
		]

		team = Team(dials = dials, points = 300, sideteam = sidedials)


	def test_add_to_sideteam_invalid_unit_datatype(self):		
		sidedials = True
		with self.assertRaises(InvalidUnitDataType):
			team = Team(sideteam = sidedials)


if __name__ == '__main__':
	unittest.main()