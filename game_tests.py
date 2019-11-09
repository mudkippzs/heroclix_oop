from game import Game
import unittest

class GameTestCase(unittest.TestCase):
	
	def test_game_import(self):
		self.assertIsNotNone(Game)

	def test_create_new_game(self):
		new_game = Game()
		self.assertTrue(isinstance(new_game, Game))

	def test_create_game_with_args(self):
		args = {
		'name': 'Test Game',		
		'map_name': 'sentinel_factory'
		}

		new_game = Game(**args)
		self.assertEqual(args['name'], new_game.name)
		self.assertIsNotNone(new_game.game_map.map_id)

if __name__ == '__main__':
	unittest.main()