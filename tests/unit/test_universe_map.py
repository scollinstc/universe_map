import unittest
from universe_map import *

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
		character_name_order = [0, 1, 2, 3, 4]
		character_name = []
		for num in character_name_order:
			char_dict = {} 
			char_dict['name'] = character_names[num]
			char_dict['type'] = character_name_types[num]
			char_dict['sequence'] num
			character_name.append(char_dict)
		
