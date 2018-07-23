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

