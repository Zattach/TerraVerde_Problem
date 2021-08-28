# Definition of the Point class, which stores an x-value and a y-value for a given point
class Point:
	# Initializing object instance
	def __init__(self, x, y):
		self.x = x
		self.y = y

	# Operation override for == and !=, allowing for the object to be immutable
	def __eq__(self, point):
		return (self.x == point.x) and (self.y == point.y)
	def __ne__(self, point):
		return not(self == point)

	# Overriide hashing function for the object, allowing the object to be hashable
	def __hash__(self):
		return hash((self.x, self.y))

	# Declare the string form of the object, mostly used in testing
	def __str__(self):
		return "Point({self.x}, {self.y})".format(self = self)

# Definition of the Line class, stores three variables: vert = vertical, m = slope, b = y-intercept
# The line is presented in the y = mx + b format
# The vert variable allows us to determine if the line is in x = c format (vertical line)
class Line:
	# Initializing object instance
	def __init__(self, vert, m, b):
		self.vert = vert
		self.m = m
		self.b = b
		# self.points = set()		Artifact of first draft of Line

	# Operation override for == and !=, allowing for the object to be immutable
	def __eq__(self, line):
		return not(self.vert ^ line.vert) and (self.m == line.m) and (self.b == line.b)
	def __ne__(self, line):
		return not(self == line)

	# Overriide hashing function for the object, allowing the object to be hashable
	def __hash__(self):
		return hash((self.vert, self.m, self.b))

	# Declare the string form of the object, changes the formulation based on the line
	def __str__(self):
		if self.vert:
			return "Line(x = {self.b})".format(self = self)
		elif self.m == 0:
			return "Line(y = {self.b})".format(self = self)
		else:
			return "Line(y = {self.m}x + {self.b})".format(self = self)