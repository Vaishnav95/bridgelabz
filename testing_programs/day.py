'''
To the Util Class add ​ dayOfWeek static function that takes a date as input and
prints the day of the week that date falls on. Your program should take three
command-line arguments: m (month), d (day), and y (year). For m use 1 for January,
2 for February, and so forth. For output print 0 for Sunday, 1 for Monday, 2 for
Tuesday, and so forth. Use the following formulas, for the Gregorian calendar (where
/ denotes integer division):
y ​ 0​ = ​ y ​ − (14 − ​ m ) ​ / 12
x ​ = ​ y 0​ ​ + ​ y ​ 0​ /4 − ​ y 0​ ​ /100 + ​ y ​ 0​ /400
m ​ 0​ = ​ m ​ + 12 × ((14 − ​ m ​ ) / 12) − 2
d ​ 0​ = (​ d ​ + ​ x ​ + 31​ m ​ 0​ / 12) mod 7
'''

from utils import Util

year = int(input('Enter a year: '))
month = int(input('Enter a month: '))
day = int(input('Enter a day: '))

day_object = Util()
day_of_the_week = day_object.day_of_week(year, month, day)
print(day_of_the_week)
