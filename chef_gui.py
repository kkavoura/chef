import tkinter as tk
from manager import Manager
from coordinate import Coordinate

gui_manager = Manager()
current_recipe = gui_manager.initialize_recipe()


FRAMES_BG_COLOR = "#BDE8DF"
MAIN_WINDOW_BG_COLOR = "#85C5B7"
LIGHTER_ACCENT_COLOR = "#FEFFF5"

current_coords = Coordinate(1,1)


# ------------------------------------------------- INPUT VERIFICATION ----------------------------------------------------------------------------------------------------------------------#
# Verify ingredients aren't empty
def verify_ingredients_input():
	if ingredients_entry.get() == "":
		print("Verifying input: Ingredient cannot be empty")
		return False
	else:
		return True

#------------------------------------------------- Functions that retrieve relevant inputs and add them to current recipe -------------------------------------------------------------------#

# Gets ingredient from Entry widget, adds it to current Recipe object and clears Entry widget
def add_ingredient():
	if verify_ingredients_input():
		print("Adding ingredient: " + ingredients_entry.get())
		new_ingredient = gui_manager.create_new_ingredient(ingredients_entry.get())
		current_recipe.add_ingredient(new_ingredient)
		ingredients_entry.delete(0, tk.END)
	else:
		print("Ingredient not verified, cannot proceed to add ingredient")
		return

# Gets step from Entry widget, adds it to current Recipe object and clears Entry widget
def add_step():
	print("Adding step: " + step_entry.get())
	new_step = gui_manager.create_new_step(step_entry.get())
	current_recipe.add_step(new_step)
	step_entry.delete(0, tk.END)

# Gets tag from Entry widget, adds it to current Recipe object and clears Entry widget
def add_tag():
	print("Adding tag: " + tag_entry.get())
	new_tag = tag_entry.get()
	current_recipe.add_tag(new_tag)
	tag_entry.delete(0, tk.END)

# Gets note from Entry widget, adds it to current Recipe object and clears Entry widget
def add_note():
	print("Adding note: " + note_entry.get())
	new_note = note_entry.get()
	current_recipe.add_note(new_note)
	note_entry.delete(0, tk.END)

def print_current_recipe():
	current_recipe.print_out()


#------------------- Initialize Window ------------------------------------------
window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window.title('Chef')
window.maxsize(screen_width, screen_height)
window.option_add( "*font", "Cambria" )
window.config(bg=MAIN_WINDOW_BG_COLOR)

#------------------- Build Input Frame -------------------------------------------------------------------------------------------------------#
input_frame = tk.Frame(window, width=screen_width*0.29, height=500, bg=FRAMES_BG_COLOR)
input_frame.grid(row=0, column=0, padx=8, pady=8)
input_frame.grid_propagate(0)

# Inside input frame
recipe_name_input_frame =  tk.Frame(input_frame,  width=screen_width*0.29,  height=20, bg=FRAMES_BG_COLOR)
recipe_name_input_frame.grid(row=0,  column=0, pady=(20,0), ipady=10)
recipe_name_input_frame.grid_propagate(0)

	# Inside recipe name input frane
recipe_name_input_label = tk.Label(recipe_name_input_frame, text="Recipe Name: ", bg=FRAMES_BG_COLOR)
recipe_name_input_label.grid(row=0, column=0)
recipe_name_entry = tk.Entry(recipe_name_input_frame, width=40)
recipe_name_entry.grid(row=0, column=1)
	# Exit recipe_name_input_frame

	# Inside components input frame
components_input_frame = tk.Frame(input_frame, width=screen_width*0.29, height=400, bg=FRAMES_BG_COLOR)
components_input_frame.grid(row=1, column=0, pady=20)
components_input_frame.grid_propagate(0)

# Gui and input for ingredients
ingredients_input_label = tk.Label(components_input_frame, text = 'Ingredients:', bg=FRAMES_BG_COLOR)
ingredients_input_label.grid(row=1, column=0, pady=(10,5))
ingredients_entry = tk.Entry(components_input_frame)
ingredients_entry.grid(row=1, column=1, pady=(10,5), padx=5)
# add_ingredient_button = tk.Button(components_input_frame, width=15, text="Add Ingredient", command=lambda:[verify_ingredients_input(),add_ingredient(),refresh_display_frame()])
add_ingredient_button = tk.Button(components_input_frame, width=15, text="Add Ingredient", command=lambda:[add_ingredient()])
add_ingredient_button.grid(row=1, column=2, padx=5, pady=(10,5))

step_label = tk.Label(components_input_frame, text = 'Steps:', bg=FRAMES_BG_COLOR)
step_label.grid(row=2, column=0, pady=5)
step_entry = tk.Entry(components_input_frame)
step_entry.grid(row=2, column=1, pady=5, padx=5)
add_step_button = tk.Button(components_input_frame, width=15, text="Add Step", command=add_step)
add_step_button.grid(row=2, column=2, padx=5, pady=5)

note_label = tk.Label(components_input_frame, text = 'Notes:', bg=FRAMES_BG_COLOR)
note_label.grid(row=3, column=0, pady=5)
note_entry = tk.Entry(components_input_frame)
note_entry.grid(row=3, column=1, pady=5, padx=5)
add_note_button = tk.Button(components_input_frame, width=15, text="Add Note", command=add_note)
add_note_button.grid(row=3, column=2, padx=5, pady=5)

tag_label = tk.Label(components_input_frame, text = 'Tags:', bg=FRAMES_BG_COLOR)
tag_label.grid(row=4, column=0, pady=5)
tag_entry = tk.Entry(components_input_frame)
tag_entry.grid(row=4, column=1, pady=5, padx=5)
add_tag_button = tk.Button(components_input_frame, text="Add tag", width=15, command=add_tag)
add_tag_button.grid(row=4, column=2, padx=5, pady=5)

save_button = tk.Button(components_input_frame, text="Save", padx=50, pady=10, command=lambda:[print_current_recipe()], bg=MAIN_WINDOW_BG_COLOR, fg=LIGHTER_ACCENT_COLOR)
save_button.grid(row=5, column=1, padx=5, pady=20)

test_button = tk.Button(components_input_frame, text="TEST", padx=50, pady=10, command=lambda:[testing_this()], bg=MAIN_WINDOW_BG_COLOR, fg=LIGHTER_ACCENT_COLOR)
test_button.grid(row=6, column=1, padx=5, pady=20)

#--------------------------- Build Display Frame ------------------------------------------------------------------------------------------------------#
display_frame = tk.Frame(window, width=screen_width*0.69, height=500, bg=FRAMES_BG_COLOR)
display_frame.grid(row=0, column=1)
display_frame.grid_propagate(0)

# display recipe name
recipe_name_display_label = tk.Label(display_frame, bg=FRAMES_BG_COLOR, font="Cambria 20 bold underline")
recipe_name_display_label.grid(row=0,  column=0)
recipe_name_display_label.grid_propagate(0)

ingredients_display_label = tk.Label(display_frame, font="Cambria 15 underline", bg=FRAMES_BG_COLOR, text="Ingredients", width=10, anchor="w")
ingredients_display_label.grid(row=1,  column=0)

# display ingredients - dynamic number of labels inside a frame
ingredients_display_frame = tk.Frame(display_frame, bg=FRAMES_BG_COLOR)
ingredients_display_frame.grid(row=2,  column=0, pady=10)
recipe_name_display_label.grid_propagate(0)

ingredient_label_list = []

# returns tuple with the coordinates of a label
def get_label_coords(current_label):
	row    = current_label.grid_info()['row']      # Row of the button
	column = current_label.grid_info()['column']
	return(row, column)


# given coordinates and text, creates a label with that text at those coords
def create_label(ingredient_text, coordinates):
	current_label = tk.Label(ingredients_display_frame, text=ingredient_text, bg=LIGHTER_ACCENT_COLOR, relief="raised")
	# current_label.bind("<Button-1>", lambda _: [gui_manager.remove_ingredient(current_ingredient.name, current_recipe), remove_ingredient_label(current_label)])
	current_label.bind("<Button-1>", lambda _: [current_coords.go_to_previous_coordinates()])
	current_label.bind("<Button-2>", lambda _: [get_label_coords(current_label)])	
	current_label.bind("<Button-3>", lambda _:[remove_ingredient_label(current_label)])
	current_label.bind("<Enter>", lambda _:[current_label.config(relief="sunken")])
	current_label.bind("<Leave>", lambda _:[current_label.config(relief="raised")])
	print('ccord row: ' + str(current_coords.row) + ' ccord col: ' + str(current_coords.column))
	current_label.grid(row=current_coords.row, column=current_coords.column, pady=10, padx=10, ipady=5, ipadx=5)
	ingredient_label_list.append(current_label)
	current_coords.go_to_next_coordinates()
	# current_coords.row = new_coords[0]
	# current_coords.column = new_coords[1]
	return current_label

# given an ingredient label return the next label in ingredients display
def get_next_ingredient_label(current_label):
	number_of_ingredient_labels = len(ingredients_display_frame.winfo_children())
	print("this many ingredient labels: "+ str(number_of_ingredient_labels))

# remove an ingredient label from display
# gets coordinates of label clicked, moves current coordinates here, deletes label, moves all subsequent labels to proper coords
def remove_ingredient_label(target_label):
	coords_for_removal = get_label_coords(target_label)
	ingredient_text = target_label['text']
	print(ingredient_text)
	gui_manager.remove_ingredient(ingredient_text, current_recipe)
	current_coords.move_to_new_coords(get_label_coords(target_label))
	target_label.destroy()
	current_coords.reset()
	for ingredient_label in ingredients_display_frame.winfo_children():
		ingredient_label.grid(row=current_coords.row, column=current_coords.column)
		current_coords.go_to_next_coordinates()

# reset coords to 1,1
# for label in ingredient labels, row=cur row, col=cur col. current coords move to next








# def save_recipe():
# 	my_recipe_name = recipe_name.get()
# 	if my_recipe_name == "":
# 		print("Must enter recipe name")
# 		return
# 	gui_manager.save_recipe(my_recipe_name)

#------------------------------------------ Keybinds for entry widgets--------------------------------------#
# enter data with return key
ingredients_entry.bind("<Return>", lambda x:[add_ingredient(), create_label(current_recipe.ingredients[-1].name, current_coords)])
# step_entry.bind("<Return>", lambda x:[add_step(), refresh_display_frame()])

#------------------------------------------- Run -----------------------------------------------------------#

def testing_this():
	print('test')



# window.bind("<x>", lambda x: print(str(current_coords.row) +" , "+ str(current_coords.column)+ str(current_coords.go_to_previous_coordinates())))
window.mainloop()


# Maybe make pad numbers constants?
# Make sure padx pady are all in consistent order
# Make sizes constants, adjustable
# Do verification for entry types
# Add Recipe attributes: difficulty, rating
# Clear relevant entry when button is clicked
# Make "Enter" work on entry
# Make fonts constants
# Make Ingredients_ ingredient (singular) to match tag, note etc
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! consider having manager do more of the work. ? Move current_recipe ? !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Make return bind decorator ? lambda is always doing the same thing
# Capitalize input
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Create canvas for scrolling !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# Really consider switching to pyQT
# get resolution, scale window to res
# use underscore instead of x for lambdas with unused args
# ingredients - on verification check for duplicate entry
# search to see if it makes sense to have a class function call another class function (manager search by name) to see if this is bad practice
# BEHAVIOR - when hitting Save it updates the display in the way that it adds the last ingredient added as a new ingredient
# ingredient labels on hover behavior
# don't add label when ingredient doesn't verify

#create attr current position. Update current position on add or remove. When placing label place at current pos!
# 		have main current position and temp current position. when label is removed, update temp current pos based on where removed label was. update row, col of all subsequent
# 		labels (from label list), incrementing from temp current position
# row change is triggering at pos x,4
# gotta make it into dict to change vals
# could make coords input adjustable so that it's a variable number of ingredients per row

# Feel like this is getting very stupid and complicated. Don't need dict with values? just use the global row and column counter values
# rename update_label_coords because it's actually not just updating but also doing the displaying

#get next coord function

#check how we're adding labels
#change to adding labels properly by coord
# nextCoord? to be use to get location for next placement
# then after removing a label, we cycle through all the remaining labels, placing them at the correct coords. might need getnextlabel, getnextcoord

# should getting previous or next coords return an updated coords object ?