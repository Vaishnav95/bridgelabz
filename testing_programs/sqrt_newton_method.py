'''
Write a static function ​ sqrt t ​ o compute the square root of a nonnegative number c
given in the input using Newton's method:
- initialize t = c
- replace t with the average of c/t and t
- repeat until desired accuracy reached using condition Math.abs(t - c/t) > epsilon*t
where epsilon = ​ 1e-15​
'''

from utils import Util

c = abs(int(input("Enter a non negative number: ")))

root_object = Util()
square_root = root_object.sqrt_newton(c)
