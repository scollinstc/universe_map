import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class RelationshipType:
    def __init__(self):
        self._name = None
        self._default_direction = None

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid RelationshipType name. Must be a string.")
        self._name = value

    @name.deleter
    def name(self):
        del self._name

    @property
    def default_direction(self):
        return self._default_direction

    @default_direction.setter
    def default_direction(self, value):
        if not isinstance(value, str):
            raise ValueError("Invalid RelationshipType default_direction value. Must be a string.")
        self._default_direction = value


