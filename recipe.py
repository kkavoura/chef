class Recipe():
	def __init__(self, name):
		self._name = name
		self._ingredients = []
		self._steps = []
		self._tags = []
		self._difficulty = 0
		self._notes = ""

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
	


	def add_ingredient(self, new_ingredient):
			self._ingredients.append(new_ingredient)

	def remove_ingredient(self, new_ingredient):
			self._ingredients.remove(new_ingredient)

	def add_step(self, step):
		self.steps.append(step)

	def add_tag(self, tag_text):
		self.tags.append(tag_text)


#------------------PRINT------------------------------------------------------
	def print_out(self):
		print(self.name)
		print()
		print("Ingredients: ")
		for ingredient in self._ingredients:
			print(" -" + ingredient.name)
		print()
		for step in self._steps:
			print(str(step.number) + ". "+step.description)
		print()
		print("Notes: " + self.notes)
		print()
		print("Tags: ")
		for tag in self.tags:
			print(" -" + tag)