from recipe import Recipe
from ingredients import Ingredient
from steps import Step
from typing import Type
from tag import Tag
from note import Note
import db as db

class Manager():
	def __init__(self):
		return

	def new_recipe(self):
		self.current_recipe = Recipe("")
		print("Initializing recipe")

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

	# calls database to empty table
	def empty_table(self):
		db.empty_table()
		Step.reset_step_counter()


	# saves Recipe to db
	def save_recipe(self, recipe_name):

		self.current_recipe.name = recipe_name

		# If recipe already has been saved, updates it
		if(self.current_recipe.is_saved):
			print("Recipe already exists in db, updating")
			db.update_recipe(self.current_recipe.recipe_id, self.current_recipe.name)
			return

		self.current_recipe.recipe_id = db.insert_recipe(self.current_recipe.name)

		for ingredient in self.current_recipe.ingredients:
			db.insert_ingredient(ingredient, self.current_recipe.recipe_id)

		for tag in self.current_recipe.tags:
			db.insert_tag(tag, self.current_recipe.recipe_id)

		for step in self.current_recipe.steps:
			db.insert_step(step.number, step.description, self.current_recipe.recipe_id)

		for note in self.current_recipe.notes:
			db.insert_note(note, self.current_recipe.recipe_id)

		db.print_out()
		self.current_recipe.save()


	# Initializes a new recipe. Creates a new recipe object and clears all data from interface
	def create_new_recipe(self) -> None:
		print("Step number before creating new recipe is " + str(Step.counter))
		Step.reset_step_counter()
		self.current_recipe = Recipe("")
		for ingredient in self.current_recipe.ingredients:
			print(type(ingredient))





	# make sure it's not saving if a part of the recipe entry fails
	# have function check for removed ingredients when saving
	# if recipe has been saved, instead of not saving, update.
	# Why is recipe name becoming blank?
	# Recipe name is never saved! Just inserted.

	# When clicked quickly, button breaks app

# drop table should delete ingredients in ui