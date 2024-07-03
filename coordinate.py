class Coordinate():
	def __init__(self, row, column):
		self._row = row
		self._column = column

	@property
	def row(self):
		return self._row

	@row.setter
	def row(self, new_row):
		self._row = new_row

	@property
	def column(self):
		return self._column

	@column.setter
	def column(self, new_column):
		self._column = new_column

	def get_next_coords(self):
		return [self.row, self.column]

	# calculate and return next coordinates, given a set of coordinates
	def get_next_coordinates(self):
		if self.column == 4:
			new_row_coord = self.row + 1
			new_col_coord = 1
		else:
			new_row_coord = self.row
			new_col_coord = self.column + 1
		return (new_row_coord, new_col_coord)

	# calculate and return previous coordinates, given a set of coordinates
	def get_previous_coordinates(self):
		new_col_coord = self.column - 1
		if new_col_coord == 0:
			new_col_coord = 4
			new_row_coord = self.row - 1
		else:
			new_row_coord = self.row
		return (new_row_coord, new_col_coord)

	# update current row and column to the next values
	def go_to_next_coordinates(self):
		if self.column == 4:
			self.row += 1
			self.column = 1
		else:
			self.column += 1

	# update current row and column to previous values
	def go_to_previous_coordinates(self):
		self.column -= 1
		if self.column == 0:
			self.column = 4
			self.row -= 1

	# sets the current coordinates to new coordinates (tuple)
	def move_to_new_coords(self, new_coords):
		self.row = new_coords[0]
		self.column = new_coords[1]

	# resets current coordinates to starting point (1,1)
	def reset(self):
		self.row = 1
		self.column = 1
