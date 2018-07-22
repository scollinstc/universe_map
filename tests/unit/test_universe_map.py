import unittest
from universe_map import Universe, Character

class TestUniverseMap(unittest.TestCase):
	def test_create_universe(self):
		universe = Universe_Map()
		self.assertIsNotNone(universe)
		
	def test_name_universe(self):
		universe = Universe_Map()
		universe.name = 'Outlander'
		
	def test_create_character(self):
		character = Character()
		self.assertIsNotNone(character)
		
	def test_create_character_name(self):
		character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
		character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
		general_character_name_type = 'Formal'
		character_name = CharacterName(general_character_name_type, character_names, character_name_types)
		self.assertEqual(character_name['general_type'], 'Formal')
		self.assertEqual(character_name['full_name_string'], 'James Alexander Malcolm Mackenzie Fraser')
		
			
		
