from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
	from ingredients import Ingredient

class Recipe():
	def __init__(self, name):
		self._name = name
		# self._ingredients = []
		self._ingredients = {}
		self._steps = []
		self._tags = {}
		self._difficulty = 0
		self._notes = {}
		self._is_saved = False
		self._recipe_id = 0

	@property
	def name(self):
		return self._name

	@name.setter
	def name(self, new_name):
		self._name = new_name

	@property
	def ingredients(self):
		return self._ingredients

	@property
	def steps(self):
		return self._steps

	@property
	def tags(self):
		return self._tags

	@property
	def difficulty(self):
		return self._difficulty	

	@property
	def notes(self):
		return self._notes
	@notes.setter
	def notes(self, notes_text):
		self._notes = notes_text

	@property
	def is_saved(self):
		return self._is_saved

	def save(self):
		self._is_saved = True

	@property
	def recipe_id(self):
		return self._recipe_id

	@recipe_id.setter
	def recipe_id(self, new_value):
		self._recipe_id = new_value


	def add_ingredient(self, new_ingredient:type[Ingredient]) -> None:
		self._ingredients[new_ingredient.name] = new_ingredient

	def remove_ingredient(self, ingredient:str) -> None:
		del self._ingredients[ingredient]

	def has_ingredient(self, ingredient_text:str) -> bool:
		for ingredient in self.ingredients:
			if ingredient_text in self.ingredients:
				print("found the ingredient")
				return True
			else:
				return False

	def add_step(self, step):
		self.steps.append(step)

	def remove_step(self, step:str) -> None:
		print(1)

	# when a step has been removed from the Recipe, the step numbers must be reassigned or they will be off
	def reassign_step_numbers(self):
		counter = 1
		for step in self._steps:
			step.number = counter
			counter += 1

	def add_tag(self, tag):
		self.tags[tag.text] = tag

	def remove_tag(self, tag_text:str) -> None:
		del self.tags[tag_text]

	def has_tag(self, tag_text:str) -> bool:
		for tag in self.tags:
			if tag_text in self.tags:
				return True
			else:
				return False		

	def add_note(self, note):
		self.notes[note.text] = note

	def remove_note(self, note_text:str) -> None :
		del self.notes[note_text]



#------------------PRINT------------------------------------------------------
	def print_out(self):
		print(self.name)
		print()
		print("Ingredients: ")
		for ingredient in self._ingredients:
			print("- " + self._ingredients[ingredient].name)
		print()
		for step in self._steps:
			print("Step: "+ str(step.number) +". "+ step.description)
		print()
		print("Notes: ")
		for note in self.notes:
			print("- " + note)

		print()
		print("Tags: ")
		for tag in self.tags:
			print("- " + tag)



	# be consistent in how attributes are called self._attr or self.attr
	# keep calling attr with _attr or .attr consistent
	# Why are ingredients, tags and notes dictionaries?