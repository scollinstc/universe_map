import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CharacterName:

    def __init__(self, general_name_type, names, name_types):
        # First, assert that names and types are the same length
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
    # List being used to preserve indexing order
    name_list = []
    for i in range(len(names)):
        char_dict = {'name': names[i], 'type': name_types[i]}
        name_list.append(char_dict)
    return name_list


class Character:
    def __init__(self):
        self._names = []

    @property
    def names(self):
        return self._names

    @names.setter
    def names(self, value):
        self._names = value

    def add_name(self, general_name_type, names, name_types):
        self._names.append(CharacterName(general_name_type, names, name_types))

    def add_name_from_string(self, general_name_type, name_string):
        # Need to convert to type, name list, name_type list to create character name.
        name_list = name_string.split(' ')
        assert len(name_list) > 0, 'Invalid name.'
        name_types = get_default_name_type_list(name_list)
        self._names.append(CharacterName(general_name_type, name_list, name_types))


def get_default_name_type_list(name_list):
    if len(name_list) == 1:
        return ['Mononym']
    name_types = [None for _ in name_list]
    name_types[0] = 'First'
    name_types[-1] = 'Surname'
    for num in range(1, (len(name_types) - 1)):
        name_types[num] = 'Middle'
    return name_types




