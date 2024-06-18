from recipe import *
from ingredients import *
from steps import *

myRecipe = Recipe('Hearty Black Bean Quesadilla')

#input ingredients
black_beans = Ingredient('black beans')
frozen_corn = Ingredient('frozen corn')
red_onion = Ingredient('red onion')
garlic = Ingredient('garlic')
cilantro = Ingredient('cilantro')
shredded_cheddar_cheese = Ingredient('shredded cheddar cheese')
taco_seasoning = Ingredient('taco seasoning')
flour_tortillas = Ingredient('flour tortillas')

all_ingredients=[black_beans, frozen_corn, red_onion, garlic, cilantro, shredded_cheddar_cheese, taco_seasoning, flour_tortillas]

#input steps
#TODO: add step behavior that adds new steps to end and increments by 1
step1 = Step(1)
step1.description = "Drain the black beans and add them to a bowl along with the frozen corn (no need to thaw)."
step2 = Step(2)
step2.description = "Finely dice the onion, mince the garlic, and roughly chop the cilantro."
step3 = Step(3)
step3.description = "Add the onion, garlic, cilantro, shredded cheddar, and taco seasoning to the bowl with the beans and corn. Stir until everything is evenly combined and coated in seasoning."
step4 = Step(4)
step4.description = "Place a half cup of the filling on one side of each tortilla and fold over. \
Cook the quesadillas in a skillet over medium heat on each side until brown and crispy and the cheesy filling has melted. Slice into triangles then serve."
step5 = Step(5)
step5.description = "To freeze the quesadillas, stack the filled and uncooked quesadillas with a piece of parchment paper between each quesadilla.\
Place in a freezer bag and freeze for up to three months.\
To reheat either microwave (for a soft quesadilla) or cook in a skillet on low heat (make sure to use low heat so that the filling has time to thaw and melt before the outside burns)."
all_steps = [step1, step2, step3, step4, step5]
tags = ['mexican', 'cheap', 'versatile', 'good for using leftovers']

for ingredient in all_ingredients:
	myRecipe.add_ingredient(ingredient)

for step in all_steps:
	myRecipe.add_step(step)

for tag in tags:
	myRecipe.add_tag(tag)

myRecipe.notes = "I used my homemade taco seasoning here, but you can use a store-bought packet of taco seasoning if needed."


myRecipe.print_out()