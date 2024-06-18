#-----------------------------INGREDIENTS--------------------------------------------------------------------------------------------------------------------#
class Ingredient():
	def __init__(self, name):
		self._name = name
		self._cost_per_unit = 0
		self._have_it = False

	@property
	def name(self):
		return self._name

	@property
	def cost_per_unit(self):
		return self._cost_per_unit
	
	@property
	def have_it(self):
		return self._have_it
