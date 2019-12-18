"""Bubble Sort
a. Desc -> Reads in integers prints them in sorted order using Bubble Sort
b. I/P -> read in the list ints
c. O/P -> Print the Sorted List
"""

from utils import Util

elements_number = int(input("Enter number of elements : "))
bubble_object = Util()
result_array = bubble_object.bubble_sort(elements_number)
