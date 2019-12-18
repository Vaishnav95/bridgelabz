"""Palindrome Checker using deque
A palindrome is a string that reads the same forward and backward, for
example, radar, toot, and madam. We would like to construct an algorithm to
input a string of characters and check whether it is a palindrome.
"""

from data_structures_util import Deque

input_string = input("Enter the string to be checked: ")

deque_object = Deque()
deque_object.palindrome_checker(input_string)
