from recipe import Recipe
from ingredients import Ingredient
from steps import Step
from typing import Type
from tag import Tag
from note import Note

class Manager():
	def __init__(self):
		return

	def initialize_recipe(self):
		self.current_recipe = Recipe("")
		print("Initializing recipe")

	def save_recipe(self, recipe_name):
		print("SAVING RECIPE WITH NAME " + recipe_name)

	# given a string with an ingredient name, calls Recipe to remove that Ingredient
	def remove_ingredient(self, ingredient: str) -> None:
		print("Manager removing ingredient " + str(ingredient))
		self.current_recipe.remove_ingredient(ingredient)

	# creates a new Ingredient and adds it to the current Recipe
	def add_ingredient(self, ingredient:str) -> None:
		print("Manager creating & adding ingredient " + str(ingredient))
		current_ingredient = Ingredient(ingredient)
		self.current_recipe.add_ingredient(current_ingredient)

	#create new Step and add it to the current Recipe
	def add_step(self, step_text:str) -> Type[Step]:
		current_step = Step(step_text)
		print("Creating new step: " + step_text + " and with step number: "+ str(current_step.number))
		current_step.increase_step_counter()
		self.current_recipe.add_step(current_step)
		return current_step

	# remove a Step object from the current Recipe 
	def remove_step(self, step):
		print("manager removing step")
		self.current_recipe.steps.pop(step.number-1)
		self.current_recipe.reassign_step_numbers()
		Step.decrease_step_counter(self)

	def add_note(self, note_text:str) -> None :
		print("Manager creating new note: " + note_text)
		current_note = Note(note_text)
		self.current_recipe.add_note(current_note)

	def remove_note(self, note_text:str) -> None:
		self.current_recipe.remove_note(note_text)

	# creates a new Tag and adds it to the current Recipe	
	def add_tag(self, tag_text:str) -> None :
		print("Manager creating new tag: " + tag_text)
		current_tag = Tag(tag_text)
		self.current_recipe.add_tag(current_tag)

	def remove_tag(self, tag_text:str) -> None :
		self.current_recipe.remove_tag(tag_text)

	# gets the Step class variable "counter" ###RENAME because its class var
	def get_current_step_number(self) -> int:
		return(getattr(Step, "counter"))

	# prints the current recipe and attributes to the console
	def print_recipe(self) ->None : 
		print(self.current_recipe.print_out())

	# call recipe to check if ingredient is duplicate
	def check_duplicate_ingredient(self, ingredient_text:str) -> bool :
		 return self.current_recipe.has_ingredient(ingredient_text)

	def check_duplicate_tag(self, tag_text:str) -> bool:
		return self.current_recipe.has_tag(tag_text)





	# don't duplicate ingredients