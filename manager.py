from recipe import Recipe
from ingredients import Ingredient
from steps import Step

class Manager():
	def __init__(self):
		return

	def save_recipe(self, recipe_name):
		print("SAVING RECIPE WITH NAME " + recipe_name)

	def add_ingredient(self, ingredient):
		print("Manager adding ingredient " + str(ingredient))
		return ingredient

	def search_by_name(self,current_recipe, target_ingredient):
		for ingredient in current_recipe.ingredients:
			if ingredient.name == target_ingredient:
				return current_recipe.ingredients.index(ingredient)

	def remove_ingredient(self, ingredient, current_recipe):
		target_index = self.search_by_name(current_recipe, ingredient)
		current_recipe.ingredients.remove(current_recipe.ingredients[target_index])
		print("Manager removing ingredient " + ingredient)
		print(current_recipe.ingredients)


	def initialize_recipe(self):
		current_recipe = Recipe("")
		print("Initializing recipe")
		return current_recipe

	#create new Ingredient object
	def create_new_ingredient(self, ingredient):
		print("Creating new ingredient: " + ingredient)
		current_ingredient = Ingredient(ingredient)
		return current_ingredient

	#create new Step object
	def create_new_step(self, step):
		print("Creating new step: " + step)
		current_step = Step(step)
		return current_step