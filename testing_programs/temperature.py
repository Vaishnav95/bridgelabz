'''
To the Util Class add ​ temperaturConversion static function, given the temperature
in fahrenheit as input outputs the temperature in Celsius or viceversa using the
formula
Celsius to Fahrenheit: (°C × 9/5) + 32 = °F
Fahrenheit to Celsius: (°F − 32) x 5/9 = °C
'''

from utils import Util

unit = str(input("Choose the unit of temperature as input\n(Press 'c' for Celsius or 'f' for Fahrenheit): "))

temperature_object = Util()
convert = temperature_object.temperature_conversion(unit)
