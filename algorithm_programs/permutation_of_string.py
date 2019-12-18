'''
Write static functions to return all permutations of a String using iterative method and
Recursion method. Check if the arrays returned by two string functions are equal.
'''

from utils import Util
new_string = input("Enter a string: ")

combinations = Util.permutation_string(new_string)
print(combinations)

count = 0
for characters in combinations:
    count += 1
print("Number of Combinations: ", count)
