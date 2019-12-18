'''
Coupon Numbers
a. Desc -> Given N distinct Coupon Numbers, how many random numbers do you
need to generate distinct coupon number? This program simulates this random
process.
b. I/P -> N Distinct Coupon Number
c. Logic -> repeatedly choose a random number and check whether it's a new one.
d. O/P -> total random number needed to have all distinct numbers.
e. Functions => Write Class Static Functions to generate random number and to
process distinct coupons.
'''

from utils import Util

try:
    distinct = int(input("Enter number of distinct coupon number: "))
    if distinct > 0:
        coupon_object = Util()
        random_coupon_count = coupon_object.coupon_numbers(distinct)
        print(random_coupon_count)
    else:
        print("Enter a positive value!")

except:
    print("Enter an integer value!")
