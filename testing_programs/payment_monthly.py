'''
Write a Util Static Function to calculate ​ monthlyPayment that reads in three
command-line arguments P, Y, and R and calculates the monthly payments you
would have to make over Y years to pay off a P principal loan amount at R per cent
interest compounded monthly.
'''

from utils import Util

P = float(input("Enter the principle loan amount: "))
Y = float(input("Number of years would it take to pay off: "))
R = float(input("Percent of Interest : "))

payment_object = Util()
payment = payment_object.monthly_payment(P, Y, R)
