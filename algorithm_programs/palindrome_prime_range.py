'''
Extend the above program to find the prime numbers that are Anagram and
Palindrome
'''

from utils import Util

lower = int(input("Enter a lower limit: "))
upper = int(input("Enter an upper limit: "))

palindrome_object = Util()
prime = palindrome_object.palindrome_prime(lower, upper)
