import unittest
from universe_map.universe import Universe
from universe_map.character import Character, CharacterName
from universe_map.relationship import RelationshipType


class TestUniverseMap(unittest.TestCase):
    def test_create_universe(self):
        universe = Universe()
        self.assertIsNotNone(universe)

    def test_name_universe(self):
        universe = Universe()
        universe.name = 'Outlander'
        self.assertTrue(universe.name == 'Outlander')

    def test_create_character(self):
        character = Character()
        self.assertIsNotNone(character)

    def test_create_character_name(self):
        general_name_type = 'Formal'
        character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
        character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
        character_name = CharacterName(general_name_type, character_names, character_name_types)
        self.assertEqual(character_name.name_type, general_name_type)
        self.assertEqual(character_name.full_name_string, ' '.join(character_names))

    def test_add_character_to_universe(self):
        universe = Universe()
        char = Character()
        general_name_type = 'Formal'
        character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
        character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
        char.add_name(general_name_type, character_names, character_name_types)
        universe.add_character(char)
        self.assertEqual(universe.characters[0], char)

    def test_add_name_to_universe_character(self):
        universe = Universe()
        char = Character()
        general_name_type = 'Formal'
        character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
        character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
        char.add_name(general_name_type, character_names, character_name_types)
        universe.add_character(char)
        alias_type = 'Alias'
        alias_names = ['Alexander', 'Malcolm']
        alias_name_types = ['First', 'Surname']
        universe.characters[0].add_name(alias_type, alias_names, alias_name_types)
        self.assertEqual(universe.characters[0].names[1].name_type, 'Alias')
        self.assertEqual(universe.characters[0].names[1].full_name_string, 'Alexander Malcolm')
        self.assertEqual(len(universe.characters), 1)
        self.assertEqual(len(universe.characters[0].names), 2)

    def test_add_string_name_character(self):
        char = Character()
        general_name_type = 'Formal'
        character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
        character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
        char.add_name(general_name_type, character_names, character_name_types)
        alias_type = 'Alias'
        alias_string_name = 'Alexander Malcolm'
        char.add_name_from_string(alias_type, alias_string_name)
        self.assertEqual(char.names[1].full_name_string, 'Alexander Malcolm')
        self.assertEqual(char.names[1].name_type, 'Alias')
        self.assertEqual(char.names[1].name[0]['name'], 'Alexander')
        self.assertEqual(char.names[1].name[1]['name'], 'Malcolm')
        self.assertEqual(char.names[1].name[0]['type'], 'First')
        self.assertEqual(char.names[1].name[1]['type'], 'Surname')
        second_alias_type = 'Alias'
        second_alias_string_name = 'Jamie Mackenzie MacTavish'
        char.add_name_from_string(second_alias_type, second_alias_string_name)
        self.assertEqual(char.names[2].full_name_string, 'Jamie Mackenzie MacTavish')
        self.assertEqual(char.names[2].name_type, 'Alias')
        self.assertEqual(char.names[2].name[0]['name'], 'Jamie')
        self.assertEqual(char.names[2].name[1]['name'], 'Mackenzie')
        self.assertEqual(char.names[2].name[2]['name'], 'MacTavish')
        self.assertEqual(char.names[2].name[0]['type'], 'First')
        self.assertEqual(char.names[2].name[1]['type'], 'Middle')
        self.assertEqual(char.names[2].name[2]['type'], 'Surname')
        third_alias_type = 'Alias'
        third_alias_string_name = 'MacDubh'
        char.add_name_from_string(third_alias_type, third_alias_string_name)
        self.assertEqual(char.names[3].full_name_string, 'MacDubh')
        self.assertEqual(char.names[3].name_type, 'Alias')
        self.assertEqual(char.names[3].name[0]['name'], 'MacDubh')
        self.assertEqual(char.names[3].name[0]['type'], 'Mononym')

    def test_create_relationship_type(self):
        relationship_type = RelationshipType()
        self.assertIsNotNone(relationship_type)

    def test_set_relationship_type_name(self):
        type_name = "married_to"
        relationship_type = RelationshipType()
        relationship_type.name = type_name
        self.assertEqual(relationship_type.name, type_name)
        new_type_name = "divorced_from"
        relationship_type.name = new_type_name
        self.assertEqual(relationship_type.name, new_type_name)
        wrong_type_name = 4
        with self.assertRaises(ValueError):
            relationship_type.name = wrong_type_name

    def test_set_relationship_default_direction(self):
        relationship_type = RelationshipType()
        default_direction = "both"
        relationship_type.default_direction = default_direction
        self.assertEqual(relationship_type.default_direction, default_direction)
        invalid_default = 4
        with self.assertRaises(ValueError):
            relationship_type.default_direction = invalid_default






if __name__ == '__main__':
    unittest.main()
