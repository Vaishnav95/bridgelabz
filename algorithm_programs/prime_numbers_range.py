'''
Take a range of 0 - 1000 Numbers and find the Prime numbers in that range.
'''

from utils import Util

lower = int(input("Enter a lower limit: "))
upper = int(input("Enter an upper limit: "))

prime_object = Util()
prime = prime_object.prime_numbers_range(lower, upper)
