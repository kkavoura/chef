class Recipe():
	def __init__(self, name):
		self._name = name
		self._ingredients = []
		self._steps = []
		self._tags = []
		self._difficulty = 0
		self._notes = []

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

	def add_tag(self, tag):
		self.tags.append(tag)

	def add_note(self, note):
		self.notes.append(note)


#------------------PRINT------------------------------------------------------
	def print_out(self):
		print(self.name)
		print()
		print("Ingredients: ")
		for ingredient in self._ingredients:
			print("- " + ingredient.name)
		print()
		for step in self._steps:
			print("Step: "+ str(step.number) +". "+ step.description)
		print()
		print("Notes: ")
		for note in self.notes:
			print("- " + note.text)

		print()
		print("Tags: ")
		for tag in self.tags:
			print("- " + tag.text)



	# be consistent in how attributes are called self._attr or self.attr