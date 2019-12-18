'''
6. Factors
Desc -> Computes the prime factorization of N using brute force.
I/P -> Number to find the prime factors
Logic -> Traverse till i*i <= N instead of i <= N for efficiency​ .
O/P -> Print the prime factors of number N.
'''

from utils import Util

number = int(input("Enter an integer: "))

prime_object = Util()
prime = prime_object.prime_factors(number)
print(prime)
