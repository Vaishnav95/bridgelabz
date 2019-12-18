"""
An Anagram Detection Example
a. Desc -> One string is an anagram of another if the second is simply a
rearrangement of the first. For example, 'heart' and 'earth' are anagrams...
b. I/P -> Take 2 Strings as Input such abcd and dcba and Check for Anagrams
c. O/P -> The Two Strings are Anagram or not....
"""

from utils import Util

string_1 = input("Enter the first string: ")
string_2 = input("Enter the second string: ")

anagram_object = Util()
result = anagram_object.anagram_string(string_1, string_2)
