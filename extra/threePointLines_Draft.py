import sys
import time
from point_line import *

def parseText(text):
	vals = text.translate(None, "{}(),").split()
	points = set()

	for x in range(0, len(vals), 2):
		point = Point(float(vals[x]), float(vals[x + 1]))
		points.add(point)
	return list(points)

def getLineSegment(pointL, pointR):
	if pointL.x == pointR.x:
		return Line(True, 0.0, pointL.x)
	m = (pointL.y - pointR.y) / (pointL.x - pointR.x)
	b = pointL.y - (m * pointL.x)
	return Line(False, m, b)

def main():
	start = time.time()
	points = []
	lines = []
	with open(sys.argv[1], "r") as input:
		points = parseText(input.readline())
	print("Points parsed: " + str(time.time() - start) + "s")

	for pointL in points:
		for pointR in points[points.index(pointL) + 1:]:
			line = getLineSegment(pointL, pointR)
			try:
				lineIndex = lines.index(line)
			except ValueError:
				lines.append(line)
				lineIndex = -1
			lines[lineIndex].points.add(pointL)
			lines[lineIndex].points.add(pointR)
	print("Lines determined: " + str(time.time() - start) + "s")

	with open(sys.argv[2], "w") as output:
		for line in lines:
			if len(line.points) >= 3:
				output.write(line + "\n")

	print("Program finished: " + str(time.time() - start) + "s")

if __name__ == '__main__':
	main()