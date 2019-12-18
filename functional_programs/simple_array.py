"""
2D Array
a. Desc -> A library for reading in 2D arrays of integers, doubles, or booleans from
standard input and printing them out to standard output.
b. I/P -> M rows, N Cols, and M * N inputs for 2D Array. Use Java Scanner Class
c. Logic -> create 2 dimensional array in memory to read in M rows and N cols
d. O/P -> Print function to print 2 Dimensional Array. In Java use PrintWriter with
OutputStreamWriter to print the output to the screen.
"""

from utils import Util

rows = int(input("Enter the number of rows: "))
columns = int(input("Enter the number of columns: "))

array_object = Util()
result_matrix = array_object.array_2d(rows, columns)
print(result_matrix)
