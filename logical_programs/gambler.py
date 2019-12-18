'''
Gambler
a. Desc -> Simulates a gambler who start with $stake and place fair $1 bets until
he/she goes broke (i.e. has no money) or reach $goal. Keeps track of the number of
times he/she wins and the number of bets he/she makes. Run the experiment N
times, averages the results, and prints them out.
b. I/P -> $Stake, $Goal and Number of times
c. Logic -> Play till the gambler is broke or has won
d. O/P -> Print Number of Wins and Percentage of Win and Loss.
'''

from utils import Util

stake = int(input("Enter stake: "))
goal = int(input("Enter a goal: "))
trials = int(input("Enter no. of trials: "))

gambler_object = Util()
gamble = gambler_object.gambling(stake, goal, trials)
