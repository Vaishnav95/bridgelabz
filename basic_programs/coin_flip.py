'''
2. Flip Coin and print percentage of Heads and Tails
a. I/P -> The number of times to Flip Coin. ​ Ensure it is positive integer ​ .
b. Logic -> Use Random Function to get value between 0 and 1. If < 0.5 then tails or
heads
c. O/P -> Percentage of Head vs Tails
'''

from utils import Util

flips = int(input("Enter the number of flips: "))

flip_object = Util()
percent_probability = flip_object.flipping_coins(flips)
print(percent_probability)
