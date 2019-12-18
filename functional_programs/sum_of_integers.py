'''
Sum of three Integer adds to ZERO
a. Desc -> A program with cubic running time. Read in N integers and counts the
number of triples that sum to exactly 0.
b. I/P -> N number of integer, and N integer input array
c. Logic -> Find distinct triples (i, j, k) such that a[i] + a[j] + a[k] = 0
d. O/P -> One Output is number of distinct triplets as well as the second output is to
print the distinct triplets.
'''

from utils import Util

number_of_elements = int(input("Enter number of elements : "))

sum_object = Util()
triplets_result = sum_object.triplets(number_of_elements)
print(triplets_result)
