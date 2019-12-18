'''
Merge Sort ​ - ​ Write a program to do Merge Sort of list of Strings.
a. Logic -> ​ To Merge Sort an array, we divide it into two halves, sort the two halves
independently, and then merge the results to sort the full array. To sort a[lo, hi),
we use the following recursive strategy:
b. Base case: If the subarray length is 0 or 1, it is already sorted.
c. Reduction step: Otherwise, compute mid = lo + (hi - lo) / 2, recursively sort the
two subarrays a[lo, mid) and a[mid, hi), and merge them to produce a sorted
result.
'''

from utils import Util

elements_number = int(input("Enter number of elements : "))
merge_object = Util()
result_array = merge_object.merge_sort(elements_number)
