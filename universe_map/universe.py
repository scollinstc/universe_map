from universe_map.relationship import RelationshipType
from universe_map.character import Character
from universe_map.error import NotExistsError

class Universe:
    def __init__(self):
        self._name = None
        self._characters = []
        self._relationship_types = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, list_value):
        self._characters = list_value

    def add_character(self, character_object):
        if not isinstance(character_object, Character):
            raise ValueError("Input must be a Character object.")
        self._characters.append(character_object)

    @property
    def relationship_types(self):
        return self._relationship_types

    @relationship_types.setter
    def relationship_types(self, list_value):
        for item in list_value:
            if not isinstance(item, RelationshipType):
                raise ValueError("All values must be RelationshipType objects.")
        self._relationship_types = list_value

    def add_relationship_type(self, relationship_type_object):
        if not isinstance(relationship_type_object, RelationshipType):
            raise ValueError("Input must be a RelationshipType object.")
        self._relationship_types.append(relationship_type_object)

    def get_character_by_name(self, search_name):
        """

        :param character_name:
        :return:
        """
        for character in self._characters:
            if search_name in character.name_strings:
                return character
        raise NotExistsError(self.characters, "Searched name does not appear in character list.")

    def establish_relationship(self, left_entity, right_entity, direction, relationship_type_name):
        """

        :param left_entity:
        :param right_entity:
        :param relationship_type_name:
        :return:
        """
        # First, establish that the correct relationship type exists.
        # Then, make the Relationship object
        # Then, make a unique dictionary name, and add the relationship to a dictionary of relationships
        current_relationship_type = None
        for rel_type in self._relationship_types:
            if rel_type.name == relationship_type_name:
                current_relationship_type = rel_type
        if current_relationship_type is not None:
            raise NotExistsError(self.relationship_types, "Specified relationship type does not appear in relationship types.")
        self.add_relationship(left_entity, right_entity, current_relationship_type)



