from behave import *
from universe_map.universe import Universe
from universe_map.character import Character

use_step_matcher("re")


@given("I have created a universe")
def create_universe(context):
    """
    :type context: behave.runner.Context
    """
    context.universe = Universe()
    context.universe.name = 'Outlander'


@given("I have added a character with the formal name James Alexander Malcolm Mackenzie Fraser to that universe")
def create_character_and_add_to_universe(context):
    """
    :type context: behave.runner.Context
    """
    name_type = 'Formal'
    names = ['James', 'Alexander', 'Malcolm', 'Mackenzie', 'Fraser']
    name_types = ['First', 'Middle', 'Middle', 'Middle', 'Surname']
    context.character = Character()
    context.character.add_name(name_type, names, name_types)
    context.universe.add_character(context.character)

@when(
    "I call the add_name_from_string function on that character in the universe with character type (?P<type>.+) and name (?P<name>.+)")
def add_names_to_character_in_a_universe(context, type, name):
    """
    :type context: behave.runner.Context
    :type type: str
    :type names: str
    :type name_types: str
    """
    print('Adding additional name...')
    context.universe.characters[0].add_name_from_string(type, name)


@then("the additional names will appear in the character's list of names")
def verify_names_added(context):
    """
    :type context: behave.runner.Context
    """
    pass
