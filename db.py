import sqlite3

con = sqlite3.connect("chef.db") #create connection to db or new db if non existent
cur = con.cursor() #create cursor for connection

# Create tables
def create_tables():
	con = sqlite3.connect("chef.db") 
	cur = con.cursor() 	

	cur.execute("""
		CREATE TABLE IF NOT EXISTS recipes(
			recipe_id INTEGER PRIMARY KEY AUTOINCREMENT,
			name TEXT NOT NULL
			)
		""")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS ingredients(
			name TEXT PRIMARY KEY)
		""")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS tags(
			name TEXT PRIMARY KEY)
		""")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS steps(
			step_number INTEGER,
			description TEXT NOT NULL,
			recipe_id INTEGER,
			FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id)
			)
		""")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS notes(
			description TEXT,
			recipe_id INTEGER,
			FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id) 
			)
		""")

	#------------------------ junction tables -----------------	
	cur.execute("""
		CREATE TABLE IF NOT EXISTS recipes_ingredients(
			recipe_id INTEGER,
			ingredient TEXT,
			PRIMARY KEY (recipe_id, ingredient),
			FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
			FOREIGN KEY (ingredient) REFERENCES ingredients(name)
			)
		""")
	cur.execute("""
		CREATE TABLE IF NOT EXISTS recipes_tags(
			recipe_id INTEGER,
			tag TEXT,
			PRIMARY KEY (recipe_id, tag),
			FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
			FOREIGN KEY (tag) REFERENCES tags(name)
			)
		""")

##  INSERTS 

# Inserts a recipe name into recipe db. Return the autoincremented ID(primary key) for the recipe
def insert_recipe(recipe_name):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor() 	
	print("Inserting recipe  "+ recipe_name + " into recipes table")
	cur.execute("""
		INSERT INTO recipes (name) VALUES (?)
		""", (recipe_name,))
	last_id = cur.lastrowid
	print_tables()
	con.commit()
	return last_id

# Updates an existing recipe. Updates current recipe name. Checks all ingredients associated with the recipe and removes them from the db if they've been deleted
def update_recipe(target_recipe_id, recipe_name):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor()
	update_query = """
		UPDATE recipes
		SET name = ?
		WHERE recipe_id = ?
	"""
	cur.execute(update_query, (recipe_name, target_recipe_id))
	con.commit()

# inserts ingredient into ingredients table, ignoring dupicates. Also inserts into ingredients_recipes table using the recipe_id of the associated recipe
def insert_ingredient(ingredient_name, recipe_id):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor()
	cur.execute("""
		INSERT OR IGNORE INTO ingredients (name) VALUES (?)
		""", (ingredient_name,))
	cur.execute("""
		INSERT INTO recipes_ingredients (recipe_id, ingredient) VALUES (?, ?)
		""", (recipe_id, ingredient_name))
	print_tables()
	con.commit()

# inserts tag into tags table, ignoring dupicates
def insert_tag(tag_name, recipe_id):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor()
	print("Inserting tag  "+ tag_name + " into tags table")
	cur.execute("""
		INSERT OR IGNORE INTO tags (name) VALUES (?)
		""", (tag_name,))
	cur.execute("""
		INSERT INTO recipes_tags (recipe_id, tag) VALUES (?, ?)
		""", (recipe_id, tag_name))
	print_tables()
	con.commit()

# inserts step into steps table
def insert_step(current_step_number, current_description, current_recipe_id):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor()
	cur.execute("""
		INSERT INTO steps (step_number, description, recipe_id) VALUES (?, ?, ?)
		""", (current_step_number, current_description, current_recipe_id))
	con.commit()

# Inserts notes into notes table
def insert_note(current_description, current_recipe_id):
	con = sqlite3.connect("chef.db") 
	cur = con.cursor()
	cur.execute("""
		INSERT INTO notes (description, recipe_id) VALUES (?, ?)
		""", (current_description, current_recipe_id))
	con.commit()

# print out data to console for debugging - DELETE THIS	
def print_out():
	con = sqlite3.connect("chef.db") #create connection to db or new db if non existent
	cur = con.cursor() #create cursor for connection
	try:
		res = cur.execute("SELECT * FROM recipes;")
		print("Recipes: " + str(res.fetchall()))
		res = cur.execute("SELECT * FROM ingredients;")
		print("Ingredients:  " + str(res.fetchall()))
		res = cur.execute("SELECT * FROM steps;")
		print("Steps:  " + str(res.fetchall()))
		res = cur.execute("SELECT * FROM notes;")
		print("Notes: " + str(res.fetchall()))
		res = cur.execute("SELECT * FROM tags;")
		print("Tags: " + str(res.fetchall()))
	except:
		"ERROR ON PRINTING"

# emtpies all tables
def empty_table():
	con = sqlite3.connect("chef.db")
	cur = con.cursor()

	cur.execute("""
		DROP TABLE recipes
		""")
	cur.execute("""
		DROP TABLE tags
		""")
	cur.execute("""
		DROP TABLE ingredients
		""")
	cur.execute("""
		DROP TABLE notes
		""")
	cur.execute("""
		DROP TABLE steps
		""")
	cur.execute("""
		DROP TABLE recipes_ingredients
		""")
	cur.execute("""
		DROP TABLE recipes_tags
		""")
	create_tables()
	con.commit()
	con.close()

# prints out current tables in db
def print_tables():
	con = sqlite3.connect("chef.db")
	cur = con.cursor()
	cur.execute("""
		SELECT name from sqlite_master WHERE type='table'
		""")
	tables = cur.fetchall()
	for table in tables:
		print(table)


create_tables()
con.close()