class Universe:
	def __init__(self):
		self._name = None
		self._characters = []
		
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
  
  def add_character(character_object):
  	self._characters.append(character_object)
  
  
