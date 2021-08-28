Three Point Lines - TerraVerde Challenge Problem

	DESCRIPTION:
This Python2.7 program will take in a specified file containing a list of points in a graph, converting it into a list of usable values. Then it determines the line created by those 2 points, saves it to a dictionary, and specifies how many times it has been found. In the event of a line being found at least twice (meaning it intersects at least 3 points) it is written to a specified output file for the user to read. 


	MODULE:
There is an module included in the zip file titled point_line.py. This module contains 2 classes used by the main program: Point and Line. These allow for easy visualization of the data being saved. Note that the classes override a few operations in order to be immutable and able to be hashed. This was neccessary as I was saving them in sets and dictionaries.


	FILE OUTPUT:
The program will write a line to the output file in one of 3 formats:
Line(x = _)					(note: _ is a stand-in for a value)
Line(y = _)
Line(y = _x + _)


	CONSOLE OUTPUT:
The program only prints 3 lines to the console, and those are timestamps for:
1. When the points have been converted
2. When all lines have been created
3. When all lines containing at least 3 points have been written to the output file and the program finishes


	PYTHON VERSION:
I made this program using Python2.7.11, not for any reason in particular. Python3 should be fine to run this program as is, but let me know if I was mistaken.


	USAGE:
This program takes in 2 input variables which are simply the input file and the output file name. Below is an example of the usage in a Linux based terminal:

python threePointLines.py input.input output.output


	INPUTS AND OTHER FILES:
Included in the zip file is another folder which contains (mostly) unnecessary files. One of these is my first draft of the program, in which I used a list instead of a dictionary. It did not scale well so I looked for other solutions, but it is still very similar to the end result.
Other files are sample inputs that I used for testing throughout the process. Some are simple to test easily checkable solutions, others are large and give many many answers.
Finally I included the python code I used and altered to generate test cases.


	AUTHOR:
This program was created by 
Zach Domke		8/25/2021 - 8/27/2021
zach.domke.hiring@gmail.com
/in/zachary-domke
(408) 218-5535