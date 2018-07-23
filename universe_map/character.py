class CharacterName:
    def __init__(self, general_name_type, names, name_types):
        # First, assert that names and types are the same length
        assert len(names) == len(name_types), "Names and types lists need to be the same length."
        self._name_type = general_name_type
        self._name = create_name_list(names, name_types)

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
