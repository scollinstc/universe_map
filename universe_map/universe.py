from universe_map.relationship import RelationshipType
from universe_map.character import Character

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

