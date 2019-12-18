"""Insertion Sort
Desc -> Reads in strings and prints them in sorted order using insertion sort.
I/P -> read in the list words
Logic -> Use Insertion Sort to sort the words in the String array
O/P -> Print the Sorted List
"""

from utils import Util

elements_number = int(input("Enter number of elements : "))
insertion_object = Util()
result_array = insertion_object.insertion_sort(elements_number)