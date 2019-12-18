'''
Write a static function ​ toBinary that outputs the binary (base 2) representation of
the decimal number typed as the input. It is based on decomposing the number into
a sum of powers of 2. For example, the binary representation of 106 is 11010102,
which is the same as saying that 106 = 64 + 32 + 8 + 2. Ensure necessary padding
to represent 4 Byte String.
To compute the binary representation of n, we consider the powers of 2 less than or
equal to n in decreasing order to determine which belong in the binary
decomposition (and therefore correspond to a 1 bit in the binary representation).
'''

from utils import Util

number = int(input("Enter a number: "))

to_binary_object = Util()
decimal_to_binary = to_binary_object.to_binary(number)
