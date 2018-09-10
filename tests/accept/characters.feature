Feature: Add characters

	As a user, I want to add characters to a universe

	@character
	Scenario Outline: Additional names are given to a character in a universe
		Given I have created a universe
		Given I have added a character with the formal name James Alexander Malcolm Mackenzie Fraser to that universe
		When I call the add_name_from_string function on that character in the universe with character type <type> and name <name>
		Then the additional names will appear in the character's list of names
		
		Examples: Additional Character Names
		| type          | name                        |
		| Familiar      | 'Jamie Fraser'              |
		| Alias         | 'Jamie Mackenzie MacTavish' |
		| Alias         | 'Alexander Malcolm'         |

	@relationship
	Scenario Outline: Basic relationship defined for two characters in a universe
		Given I have created a universe
		Given I have created six characters
		Given I have created three relationship types
        When I call the relate_characters function on <character_L> and <character_R> characters with relationship direction <direction> and relationship type <type>
        Then the relationship will be listed under the universe's list of relationships

        Examples: Relating characters
        | character_L      | character_R      | direction | type       |
        | Jenny Fraser     | Ian Murray       | both      | married_to |
        | Colum Mackenzie  | Dougal Mackenzie | both      | sibling_of |
        | Brianna Randall  | Ellen Mackenzie  | one       | knows_of   |
