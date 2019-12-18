'''
Write a program ​ Distance.java t ​ hat takes two integer command-line arguments x
and y and prints the Euclidean distance from the point (x, y) to the origin (0, 0). The
formulae to calculate distance = sqrt(x*x + y*y). Use Math.power function
'''

from utils import Util

x = float(input("Enter the value of x: "))
y = float(input("Enter the value of y: "))

formula_object = Util()
result = formula_object.euclidean_formula(x, y)
