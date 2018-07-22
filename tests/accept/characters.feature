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



