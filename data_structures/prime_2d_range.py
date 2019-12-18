"""Prime Numbers Range in a 2D array:
Take a range of 0 - 1000 Numbers and find the Prime numbers in that range. Store
the prime numbers in a 2D Array, the first dimension represents the range 0-100,
100-200, and so on. While the second dimension represents the prime numbers in
that range
"""

from data_structures_util import PrimeNumbers
lower = 0
upper = 1000

prime = PrimeNumbers()
result = prime.prime_range(lower, upper)