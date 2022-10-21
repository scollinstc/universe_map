import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Character:
    """
    Character object to depict person or character in a story universe.

    This object depicts a character and includes their names or names. Names for characters can be simple or complex,
    so the name is another object within this submodule.

    Attributes
    ----------
    names : list
        List of CharacterName objects associated with this Character.

    """

    def __init__(self):
        """
        Character object to depict person or character in a story universe.

        This object depicts a character and includes their names or names. Names for characters can be simple or complex,
        so the name is another object within this submodule.

        Attributes
        ----------
        names : list
            List of CharacterName objects associated with this Character.
        """
        self._names = []

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, value):
        self._names = value

    def add_name(self, general_name_type, names, name_types):
        """
        Add a name to the Character's names list attribute.

        Parameters
        ----------
        general_name_type : String
            General type of the name. Includes types like 'Familiar', 'Alias', 'Formal', 'Legal', etc.

        names : list
            Full name to be added, presented as a comma-separated string. i.e., ['James', 'Fraser']

        name_types : list
            Type of each name to be added to the list. This should correspond to the list item of the same index in
            the 'names' parameter.
        """
        self._names.append(CharacterName(general_name_type, names, name_types))

    def add_name_from_string(self, general_name_type, name_string):
        """
        Given a general name type and a string of a name separated by spaces, the name is parsed, the individual
        name parts are identified and associated, and they are added to this character's name list.

        Parameters
        ----------
        general_name_type : String
            Specifies the type of name that the name_string parameter is. Includes types like 'Familiar',
            'Alias', 'Formal', 'Legal', etc.

        name_string : String
            Characters name as a string with parts of the name separated by spaces. For example, 'James Alexander
            Malcolm Mackenzie Fraser'.
        """
        name_list = name_string.split(' ')
        assert len(name_list) > 0, 'Invalid name.'
        name_types = get_default_name_type_list(name_list)
        self._names.append(CharacterName(general_name_type, name_list, name_types))


class CharacterName:
    """
    Character name object associated with a Character.

    Attributes
    ----------
     name_type : String
        Specifies what type of name is associated with this name for a character.
        Includes types like 'Familiar', 'Alias', 'Formal', 'Legal', etc.

    name : String
        Name value for the character

    full_name_string : String
        Joins name values together into one string.

    """
    def __init__(self, general_name_type, names, name_types):
        """
        Character name object associated with a Character.

        Attributes
        ----------
        name_type : String
            Specifies what type of name is associated with this name for a character.
            Includes types like 'Familiar', 'Alias', 'Formal', 'Legal', etc.

        name : String
            Name value for the character

        full_name_string : String
            Joins name values together into one string.

        Examples
        --------
        >>> name_type = 'Formal'
        >>> character_names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
        >>> character_name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
        >>> my_character_name = CharacterName(name_type, character_names, character_name_types)
        >>> my_character_name.name_type
        'Formal'
        """
        assert len(names) == len(name_types), logger.info("Names and types lists need to be the same length.")
        self._name_type = general_name_type
        self._name = create_name_list(names, name_types)
        logger.info(str.format(' New %s name added: %s' % (self.name_type, self.full_name_string)))

    @property
    def name_type(self):
        return self._name_type

    @name_type.setter
    def name_type(self, value):
        self._name_type = value

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def full_name_string(self):
        return " ".join([self._name[x]['name'] for x in range(len(self._name))])

def create_name_list(names, name_types):
    """
    Creates a list of names in dictionary format to use with Character objects.

    Parameters
    ----------
    names : list
        List of names
    name_types : list
        List of name types, with indices corresponding to the names given in the names parameter.

    Returns
    -------
    list
        A list of dictionaries including the names and their types
    """
    # List being used to preserve indexing order
    name_list = []
    for i in range(len(names)):
        char_dict = {'name': names[i], 'type': name_types[i]}
        name_list.append(char_dict)
    return name_list

def get_default_name_type_list(name_list):
    """
    Gets the default name type types from a name list. Filler method if you just want general name types rather than
    having to specify them.

    Parameters
    ----------
    name_list : list
        List of names, separated by a comma. Example: ['Claire', 'Elizabeth', 'Beauchamp']

    Returns
    -------
    name_types : list
        List of name types associated with the name_list names.

    Examples
    --------
    >>> name = "James Alexander Malcolm Mackenzie Fraser"
    >>> name_list = name.split()
    """
    if len(name_list) == 1:
        return ['Mononym']
    name_types = [None for _ in name_list]
    name_types[0] = 'First'
    name_types[-1] = 'Surname'
    for num in range(1, (len(name_types) - 1)):
        name_types[num] = 'Middle'
    return name_types
