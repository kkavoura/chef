#-----------------------------------STEPS-------------------------------------------------------------------------------------------------------------------#
class Step():
	counter = 0

	def __init__(self, description):
		self._number = Step.counter + 1
		self._description = description
		self._ingredients = []
		self._actions = []

	# @property
	# def number(self):
	# 	return self._number

	@property
	def description(self):
		return self._description
	@description.setter
	def description(self, text_description):
		self._description = text_description

	@property
	def ingredients(self):
		return self._ingredients

	@property
	def actions(self):
		return self._actions

	@property
	def number(self):
		return self._number
	
	
	def increase_step_counter(self):
		Step.counter += 1

	def remove_astep(self):
		Step.counter -= 1

	