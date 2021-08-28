# Import sys, time, and classes from point_line.py
import sys
import time
from point_line import *

# Takes in the line of text from the input file and returns a list of Points
def parseText(text):
	# Remove all unnecessary symbols included in the text and return a list of values
	vals = text.translate(None, "{}(),").split()
	# Cycle through every value in the list, converting the value into a float, and saving it as a Point
	points = set()
	for x in range(0, len(vals), 2):
		point = Point(float(vals[x]), float(vals[x + 1]))
		points.add(point)
	return list(points)

# Take in 2 Points and return the Line that connects them (note: them being left and right is arbitrary)
def getLineSegment(pointL, pointR):
	# Determine if the Line is vertical and return it as such
	if pointL.x == pointR.x:
		return Line(True, 0.0, pointL.x)
	# Calculate the slope (m) and the y-intercept (b)
	m = (pointL.y - pointR.y) / (pointL.x - pointR.x)
	b = pointL.y - (m * pointL.x)
	return Line(False, m, b)

def main():
	start = time.time()
	points = []
	lines = {}

	if len(sys.argv) >= 2:
		# Open the input file and call parseText()
		with open(sys.argv[1], 'r') as input:
			points = parseText(input.readline())
	else:
		# If there is no given input filename, take user's input instead
		userInput = raw_input("Enter your points in the correct format:\n")
		start = time.time()
		points = parseText(userInput)
	print("Points parsed: " + str(time.time() - start) + "s")


	# Cycle through every pair of Points (note: there are no duplicate Points as they were saved to a set)
	for pointL in points:
		for pointR in points[points.index(pointL) + 1:]:
			# Calculate the Line between the 2 arbitrary Points and save the Line to the dictionary
			line = getLineSegment(pointL, pointR)
			if line in lines:
				# If the Line already exists, then increment the value
				lines[line] = lines[line] + 1
			else:
				lines[line] = 1
	print("Lines determined: " + str(time.time() - start) + "s")

	# Generate output filename if none is given
	if len(sys.argv) >= 3:
		outFileName = sys.argv[2]
	else:
		outFileName = "output.txt"

	# Open the specified output file, overwriting any existing file by that name
	with open(outFileName, 'w') as output:
		for line, value in lines.items():
			# If the value occurs 2 or more times (contains at least 3 points) output the Line
			if value >= 2:
				output.write(str(line) + "\n")

	# Write to terminal how many seconds the program took to run
	print("Program finished: " + str(time.time() - start) + "s")


if __name__ == '__main__':
	main()