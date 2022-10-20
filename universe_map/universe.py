from universe_map.character import Character

class Universe:
    """
    A class used to represent a story's world, or 'universe'. This includes the collection of characters,
    names they are known by, their relationships, the places in the universe, events, and other critical
    components to the story.

    """
    def __init__(self, name=None, characters=None):
        """
        Attributes
        ----------
        name : str
            A string that gives the name of the universe instance.
        characters : list
            A list of universe_map.Character objects comprising the characters present in this universe.

        """
        self._name = None
        self._characters = []

        if name is not None:
            self.name = name

        if characters is not None:
            self.characters = characters

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def characters(self):
        return self._characters

    @characters.setter
    def characters(self, list_value):
        self._characters = list_value

    def add_character(self, character_object):
        """
        Adds a character to the Universe object's list of characters.

        character_object : Character
            universe_map.Character object to go in this universe instance's Character list.

        Raises
        ------
        ValueError
            If the input character_object is not of type universe_map.Character.
        """
        if isinstance(character_object, Character):
            self._characters.append(character_object)
        else:
            raise ValueError('Only objects of type universe_map.Character can be appended to the character list.')
