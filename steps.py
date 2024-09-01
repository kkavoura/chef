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

	@number.setter
	def number(self, new_number):
		self._number = new_number
	
	
	def increase_step_counter(self):
		Step.counter += 1

	def decrease_step_counter(self):
		Step.counter -= 1

	@classmethod
	def reset_step_counter(cls):
		print("Resetting step counter")
		cls.counter = 0

	#maybe counter and number should not be interchangeable ? whats going on there

	