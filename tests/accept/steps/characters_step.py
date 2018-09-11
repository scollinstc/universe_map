from behave import *
from universe_map.universe import Universe
from universe_map.character import Character
from universe_map.relationship import RelationshipType

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
    context.universe.characters[0].add_name_from_string(type, name)


@then("the additional names will appear in the character's list of names")
def verify_names_added(context):
    """
    :type context: behave.runner.Context
    """
    pass


@given("I have created six characters")
def create_six_characters(context):
    """
    :type context: behave.runner.Context
    """
    name_type = 'Familiar'
    character_list = ["Jenny Fraser",
                      "Ian Murray",
                      "Column Mackenzie",
                      "Dougal Mackenzie",
                      "Brianna Randall",
                      "Hector Cameron"]

    for character in character_list:
        char = Character()
        char.add_name_from_string(name_type, character)
        context.universe.add_character(char)


@given("I have created three relationship types")
def create_three_relationship_types(context):
    """
    :type context: behave.runner.Context

    """
    relationship_types = ["married_to", "sibling_of", "knows_of"]
    relationship_default_directions = ["both", "both", "one"]

    for i in range(len(relationship_types)):
        rt = RelationshipType()
        rt.name = relationship_types[i]
        rt.default_direction = relationship_default_directions[i]
        context.universe.add_relationship_type(rt)

@when(
    "I call the relate_characters function on (?P<character_L>.+) and (?P<character_R>.+) characters with relationship direction (?P<direction>.+) and relationship type (?P<type>.+)")
def step_impl(context, character_L, character_R, direction, type):
    """
    :type context: behave.runner.Context
    :type character_L: str
    :type character_R: str
    :type direction: str
    :type type: str
    """
    pass


@then("the relationship will be listed under the universe's list of relationships")
def step_impl(context):
    """
    :type context: behave.runner.Context
    """
    pass