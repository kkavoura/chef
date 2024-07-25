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

	def search_by_name(self,current_recipe, target_ingredient):
		for ingredient in current_recipe.ingredients:
			if ingredient.name == target_ingredient:
				return current_recipe.ingredients.index(ingredient)

	def remove_ingredient(self, ingredient, current_recipe):
		target_index = self.search_by_name(current_recipe, ingredient)
		current_recipe.ingredients.remove(current_recipe.ingredients[target_index])
		print("Manager removing ingredient " + ingredient)
		print(current_recipe.ingredients)

	# creates a new Ingredient and adds it to the current Recipe
	def add_ingredient(self, ingredient:str) -> None:
		print("Manager creating & adding ingredient " + str(ingredient))
		current_ingredient = Ingredient(ingredient)
		self.current_recipe.add_ingredient(current_ingredient)

	#create new Step and add it to the current Recipe
	def add_step(self, step_text:str) -> Type[Step]:
		print("Creating new step: " + step_text)
		current_step = Step(step_text)
		current_step.increase_step_counter()
		self.current_recipe.add_step(current_step)

	# remove a Step object from the current Recipe 
	def remove_step(self):
		print("manager removing step")
		Step.remove_astep(self)

	# creates a new Tag and adds it to the current Recipe	
	def add_tag(self, tag_text:str) -> None :
		print("Manager creating new tag: " + tag_text)
		current_tag = Tag(tag_text)
		self.current_recipe.add_tag(current_tag)

	def add_note(self, note_text:str) -> None :
		print("Manager creating new note: " + note_text)
		current_note = Note(note_text)
		self.current_recipe.add_note(current_note)

	# gets the Step class variable "counter"
	def get_current_step_number(self) -> int:
		return(getattr(Step, "counter"))

	# prints the current recipe and attributes to the console
	def print_recipe(self) ->None : 
		print(self.current_recipe.print_out())






	# don't duplicate ingredients