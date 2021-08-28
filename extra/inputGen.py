import sys
import random

file = open("input7.txt", 'w')
file.write("{")
for x in range(1000):
	file.write("({x}, 0), ".format(x = x))
	file.write("(0, {x}), ".format(x = x))
file.write("(0, 0)}")
file.close()