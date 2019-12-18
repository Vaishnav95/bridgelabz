'''
3. Leap Year
a. I/P -> Year, ensure it is a 4 digit number.
b. Logic -> Determine if it is a Leap Year.
c. O/P -> Print the year is a Leap Year or not.
'''

from utils import Util

year = int(input("Enter a year: "))

year_object = Util()
year = year_object.leap_year(year)
print(year)
