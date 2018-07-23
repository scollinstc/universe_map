class Character:
	def __init__(self):
		self._names = []
		
	def add_name(self, type, names, name_types):
		self._names.append(CharacterName(type, names, name_types)
		
class CharacterName:
	def __init__(self, type, names, name_types):
		# First, assert that names and types are the same length
		assert len(names) == len(types), "Names and types lists need to be the same length."
		self._type = general_type(general_type)
		self._name = name(names, types)
		
	@property
	def type(self):
		return self._type
		
	@type.setter
	def type(self, value):
		self._type = value
		
	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, names, name_types):
		# List being used to preserve indexing order
		name_list = []
		for i in range(len(names)):
			char_dict = {} 
			char_dict['name'] = names[i]
			char_dict['type'] = name_types[i]
			name_list.append(char_dict)
		return name_list
	
	@property
	def full_name_string(self):
		return " ".join([self._name[x]['name'] for x in range(len(self._name))])
		
		
	
	
	
