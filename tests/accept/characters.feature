Feature: Add characters

	As a user, I want to add characters to a universe
	
	@character
	Scenario Outline: Characters are added to universe
		Given I have created a universe
		Given I create a character named <first_name> <last_name>
		When I call the add_character function with character <first_name> <last_name>
		Then Character <first_name> <last_name> appears in the universe's character list
		
		Example: Characters
			| first_name | last_name |
			| John       | Doe       |
			| Jane       | Eyre      |

	@character
	Scenario Outline: Additional names are given to a character
		Given I have created a universe
		Given I have created a character named James Alexander Malcolm Mackenzie Fraser
		Given I have added that character to the universe
		When I call the add_character_name function with character type <type>, names <names>, and name_types <name_types>
		Then the additional names will appear in the character's list of names
		
		Example: Character Names
		| type          | names                    | name_types                |
		| Familiar      | ['Jamie', 'Fraser']      | ['First Name', 'Surname'] |
		| Alias         | ['Jamie', 'Roy']         | ['First Name', 'Surname'] |
		| Alias         | ['Alexander', 'Malcolm'] | ['First Name', 'Surname'] |         
