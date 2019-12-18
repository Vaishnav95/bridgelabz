"""
This is a Util class which contains all the methods performing the mentioned tasks.
Author: Vaishnav Goregaonkar
Date: 17/12/2019
"""


class Util:

    def __init__(self):
        pass

    def get_username(self, name):
        """ Replacing String template
        Parameters:
            name: string as user input

        Returns:
            new_template: prints the string with the username
        """
        template = "Hello <<UserName>>, How are you?"
        if len(name) >= 3:
            # Replacing <<UserName>> with the input string
            new_template = template.replace('<<UserName>>', name.capitalize())
            print(new_template)
        else:
            # Ensure Username has minimum 3 characters
            print("Username should have at least 3 characters")

    def flipping_coins(self, flips):
        """Flip Coin and print percentage of Heads and Tails
        Parameters:
            flips: Number of times to flip a coin

        Returns:
            heads_percent: percentage of heads occurred
            tails_percent: percentage of tails occurred
        """
        import random  # todo
        heads = 0
        tails = 0

        for probability in range(flips):
            coin = random.random()
            # If >= 0.5, then heads or tails
            if coin >= 0.5:
                heads += 1
            else:
                tails += 1
        # Calculating the percentage of heads and tails out of the no. of times the coin was flipped
        heads_percent = (heads / flips) * 100
        tails_percent = (tails / flips) * 100
        print("Percentage of Heads:", round(heads_percent, 2), "%")
        print("Percentage of Tails:", round(tails_percent, 2), "%")

    def leap_year(self, year):
        """Leap Year
        Parameters:
            year: a 4 digit number as user input

        Returns:
            O/P: Whether the input year is a leap year or not
        """

        if 999 < year <= 9999:  # Ensuring it is a 4 digit number
            """
            A given year is a leap year if it is divisible by 4 and not by 100
            If it is divisible by 100, then it is a leap year only if it is further divisible by 4
            """
            if year % 4 == 0:
                if year % 100 == 0:
                    if year % 400 == 0:
                        print("{} is a leap year.".format(year))

                    else:
                        print("{} is not a leap year.".format(year))
                else:
                    print("{} is a leap year.".format(year))
            else:
                print("{} is not a leap year.".format(year))
        else:
            print("Enter a four digit number!")

    def powers_2(self, integer_power):
        """Power of 2
        Parameters:
            integer_power: The power value of 2

        Returns:
            Prints a table of power of 2 that are less than or equal to 2^N
        """
        number = 2

        while True:
            # Only works if 0 <= number < 31 since 2^31 overflows an int
            if 0 <= integer_power < 31:
                for power in range(0, integer_power + 1):
                    print("{}^{} = {}".format(number, power, number * power))# Using for loop to print the power of 2
                break
            else:
                print("Enter a value between 0 and 30")
                continue

    def harmonic(self, number):
        """Harmonic number
        Parameters:
            number: The harmonic value as input

        Returns:
            prints the sum of the series
        """
        if number != 0:  # Ensuring number is not equal to 0
            series = 0
            for value in range(1, number + 1):
                # Computing 1/1 + 1/2 + .....+ 1/number
                series = series + (1 / value)

            print("The sum of the series is", round(series, 3))
        else:
            print("Enter a value other than zero")

    def prime_factors(self, number):
        """Prime Factors
        Parameters:
            number: input number to find the prime factors
        Returns:
            printing out all the prime factors of the given number
        """
        print('Prime factors are: ')
        i = 1
        # Traversing till i*i <= N
        while i * i <= number:
            j = 0
            if number % i == 0:
                k = 1
                while k <= i:
                    if i % k == 0:
                        j += 1
                    k += 1
                if j == 2:
                    print(i)
            i += 1

    def array_2d(self, rows, columns):
        """2D Array
        Parameters:
            rows: number of input rows
            columns: number of input columns
        Returns:
            prints a 2 Dimensional array
        """
        arr = [[0 for j in range(columns)] for i in range(rows)]

        # Taking user input to fill up the array elements
        for i in range(rows):
            for j in range(columns):
                arr[i][j] = input("Enter {} row {} element:".format(i + 1, j + 1))

        print("\n")
        for row in arr:
            print(row)

    def triplets(self, number_of_elements):
        """Sum of three integers adds to ZERO
        Parameters:
            number_of_elements: number of elements in the array

        Returns:
            Prints an array of distinct triplets whose sum is zero
        """
        array_input = []
        for i in range(0, number_of_elements):
            # Taking integer as input to fill up the array
            ele = int(input("Enter a number: "))

            array_input.append(ele)

        print(array_input)

        n = len(array_input)
        found = True

        for i in range(0, n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if array_input[i] + array_input[j] + array_input[k] == 0:
                        print("Result: [{} {} {}]".format(array_input[i], array_input[j], array_input[k]))

        if not found:
            print("Incorrect values")

    def euclidean_formula(self, x, y):
        """Euclidean distance
        Parameters:
            x: X coordinates as integer value
            y: Y coordinates as integer value
        Returns:
            Calculated distance from the origin
        """
        import math
        distance = math.sqrt(x * x + y * y)
        print("Euclidean distance from point({},{}) to the origin(0,0): {}".format(x, y, round(distance, 3)))

    def quadratic_formula(self, a, b, c):
        """Roots of a quadratic equation
        Parameters:
            a, b, c: input integers
        Returns:
            Two roots of the equation
        """
        import math
        delta = (b * b) - (4 * a * c)
        root1_of_x = (-b + (math.sqrt(delta))) / (2 * a)
        root2_of_x = (-b - (math.sqrt(delta))) / (2 * a)

        print("The root of the equation {}*x*x+{}*x+{} are {} and {}".format(a, b, c, root1_of_x, root2_of_x))

    def windchill_formula(self, t, v):
        """Windchill
        Parameters:
            t: Temperature in Fahrenheit
            v: Wind speed in miles per hour
        Returns:
            w: The effective temperature or the wind chill
        """
        # Ensuring if the values are in the range
        if t <= 50 and 3 <= v <= 120:
            w = 35.74 + (0.6215 * t) + (((0.4275 * t) - 35.75) * (v ** 2))
            print("The Effective Temperature = {}".format(round(w, 3)))
        else:
            print("Formula not valid")

    def gambling(self, stake, goal, trials):
        """Gambler
        Parameters:
            stake: Starting stake in dollars
            goal: final goal the user wants to achieve
            trials: Number of times the user wants ot play
        Returns:
            wins: Number of wins
            percentage of wins and losses
        """
        import random
        bets = 0
        wins = 0

        for t in range(trials):
            cash = stake
            # The user bets until he/she reaches the goal or goes broke
            while 0 < cash < goal:
                bets += 1
                if random.randrange(0, 2) == 0:
                    cash += 1
                else:
                    cash -= 1

            if cash == goal:
                wins += 1
        print(str(wins) + ' wins')
        print(str(100 * wins / trials) + '% wins')
        print(str((1 - wins / trials) * 100) + '% loss')

    def coupon_numbers(self, N):
        """Coupon Numbers
        Parameters:
            N: number of distinct coupon numbers
        Returns:
            total random numbers needed to print all the distinct numbers
        """
        import random

        my_list = []
        count = 0

        while len(my_list) < N:
            x = random.randint(1, N)
            count += 1
            # Checking if the random number is a new one
            if x not in my_list:
                my_list.append(x)

        print("Total random numbers needed to have all distinct numbers: ", count)

    def simulate_stopwatch(self):
        """Simulate Stopwatch
        Parameters:
              Pressing Enter to start the stopwatch and stop the stopwatch
        Returns:
              prints the Elapsed time
        """
        import time

        input("Press Enter to Start")
        start_time = time.time()

        input("Press Enter to Stop")
        end_time = time.time()
        # Measuring the elapsed time between start and end
        time_elapsed = end_time - start_time
        print(round(time_elapsed, 4)," seconds")

    def cross_game(self):
        """Cross game or Tic-tac-toe game
        Parameters:
            Taking user input for player1 and player2 to mark X and O
        Returns:
            Prints the board after every step until the result
        """
        def tictactoe():
            board = [0, 1, 2, 3, 4, 5, 6, 7, 8]
            end = False
            # Possible winning outcomes
            win_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

            # Printing the board
            def draw():
                print(board[0], board[1], board[2])
                print(board[3], board[4], board[5])
                print(board[6], board[7], board[8])
                print()

            # Asking Player1 to choose the position to fill up the value and then printing the board
            def player1():
                n = choose_number()
                if board[n] == 'X' or board[n] == 'O':
                    print('\n Value already there')
                    player1()
                else:
                    board[n] = 'X'

            # Asking 2 to choose the position to fill up the value and then printing the board
            def player2():
                n = choose_number()
                if board[n] == 'X' or board[n] == 'O':
                    print('\n Value already there') # if the values are already present then ask again to play
                    player2()
                else:
                    board[n] = 'O'

            def choose_number():
                # Ensuring that the input value is an integer value displaying on the board
                while True:
                    try:
                        a = int(input())
                        if a in board:
                            return a
                        else:
                            print('\n Try Again')
                    except ValueError:
                        print('Not a number. Retry')

            def game_over():
                # if the winning combination is satisfied, then the respective player wins
                count = 0
                for i, j, k in win_combinations:
                    if board[i] == board[j] == board[k] == 'X':
                        print('Player 1 Wins!\n')
                        print('Congratulations!\n')
                        return True
                    if board[i] == board[j] == board[k] == 'O':
                        print('Player 2 Wins!\n')
                        print('Congratulations!\n')
                        return True
                # Printing tie if all the cells are full with no win combinations
                for i in range(9):
                    if board[i] == 'X' or board[i] == 'O':
                        count += 1
                        if count == 9:
                            print('Tie\n')
                            return True

            while not end:
                draw()
                end = game_over()
                if end is True:
                    break
                print('Player 1 play...')
                player1()
                print()
                draw()

                end = game_over()
                if end is True:
                    break
                print('Player 2 play...')
                player2()
                print()

        while True:
            tictactoe()
            if input('Play Again(y/n)\n') != 'y':  # Asking whether the users want to play again
                break

    def vending_machine(self, amount):
        """Finding the fewest notes to be returned for Vending machine
        Parameters:
            amount: the integer value as user input
        Returns:
            Number of notes of the following amount to be printed
        """

        while amount > 0: #todo
            if amount >= 1000:
                a = amount // 1000
                print("1000 X {}".format(a))
                amount = amount - (1000 * a) # Calculating the remaining amount

            elif amount >= 500:
                a = amount // 500
                print("500 X {}".format(a))
                amount = amount - (500 * a)

            elif amount >= 100:
                a = amount // 100
                print("100 X {}".format(a))
                amount = amount - (100 * a)

            elif amount >= 50:
                a = amount // 50
                print("50 X {}".format(a))
                amount = amount - (50 * a)

            elif amount >= 10:
                a = amount // 10
                print("10 X {}".format(a))
                amount = amount - (10 * a)

            elif amount >= 5:
                a = amount // 5
                print("5 X {}".format(a))
                amount = amount - (5 * a)

            elif amount >= 2:
                a = amount // 2
                print("2 X {}".format(a))
                amount = amount - (2 * a)

            elif amount >= 1:
                a = amount // 1
                print("1 X {}".format(a))
                amount = amount - (1 * a)

    def day_of_week(self, year, month, day):
        """Day of the Week
        Parameters:
            year, month, day: integer values as user input
        Returns:
            Prints the day of the date taken from the user
        """
        import datetime
        # Converting the inputs into a date format
        date1 = datetime.date(year, month, day)
        print(date1)

        y = date1.year
        m = date1.month
        d = date1.day
        # Use the following formulas, for the Gregorian calendar
        y0 = y - (14 - m) // 12
        x = y0 + (y0 // 4) - (y0 // 100) + (y0 // 400)
        m1 = m + 12 * ((14 - m) // 12) - 2
        d0 = (d + x + (31 * m1) // 12) % 7

        # Creating a dictionary to print out the day
        day_dict = {0: 'Sunday', 1: 'Monday', 2: 'Tuesday', 3: 'Wednesday', 4: 'Thursday', 5: 'Friday', 6: 'Saturday'}
        print(day_dict[d0])

    def temperature_conversion(self, unit):
        """Temperature Conversion
        Parameters:
            unit: Asking user for the unit of the temperature
        Returns:
            Converted unit value of temperature
        """
        while (unit != 'C' and unit != 'c') and (unit != 'F' and unit != 'f'):
            print("Enter only the above mentioned values!")
            unit = str(input("Choose the unit of temperature as input\n(Press 'c' for Celsius or 'f' for Fahrenheit):"))

        # Conversion from Celsius to Fahrenheit
        if unit == 'C' or unit == 'c':
            temperature = float(input("Enter temperature in Celsius: "))
            print("Conversion from Celsius to Fahrenheit:")
            Fahrenheit = (temperature * (9 / 5)) + 32
            print("{} Celsius = {} Fahrenheit".format(temperature, Fahrenheit))

        # Conversion from Fahrenheit to Celsius
        elif unit == 'F' or unit == 'f':
            temperature = float(input("Enter temperature in Fahrenheit: "))
            print("Conversion from Fahrenheit to Celsius:")
            Celsius = (temperature - 32) * (5 / 9)
            print("{} Fahrenheit = {} Celsius".format(temperature, Celsius))

    def monthly_payment(self, P, Y, R):
        """Monthly Payment
        Parameters:
            P: Principle loan amount
            N: no. of years to pay
            R: rate of interest in percentage
        Returns:
            Monthly payment the user will have to pay
        """
        n = 12 * Y
        r = R / (12 * 100)

        payment = (P * r) / (1 - ((1 + r) ** (-n)))
        print("Monthly Payment = $", round(payment, 2))

    def sqrt_newton(self, c):
        """Square root using Newtons method
        Parameters:
            c: non negative input number
        Returns:
            Square root of the number
        """
        epsilon = 1e-15
        t = c
        # repeating until the desired accuracy is reached
        while abs(t - c / t) > epsilon * t:
            t = (c / t + t) / 2
        print(t)

    def to_binary(self, number):
        """Decimal number to Binary
        Parameters:
            number: taking a number as input
        Returns:
            Binary representation and binary decomposition of the number into the powers of 2
        """
        template = number
        binary_string = "" # Converting the number into a string
        while number:
            remainder = number % 2
            number = number // 2
            # Printing out the remainder while continuously dividing the number by 2
            binary_string += str(remainder)

        # Reversing the remainder string and printing it out
        reverse_binary = binary_string[::-1]
        n = len(binary_string) - 1
        print("Binary representation of {}: {}".format(template, reverse_binary))
        # Powers of 2 in decreasing order
        for i in reverse_binary:
            if i != "0":
                print(str(int(i)*(2**n))+" ", end="")
            n -= 1

    @staticmethod
    def permutation_string(new_string):
        """Permutations of a string
        Parameters:
            new_string: Takes a string as user input
        Returns:
            All the possible permutations of that string
        """
        if len(new_string) == 1:
            return new_string
        # Creating an empty list and appending the combinations of that string
        permutation_list = []
        for i in new_string:
            remaining = [j for j in new_string if j != i]
            a = Util.permutation_string(remaining)

            for k in a:
                permutation_list.append(i + k)
        return permutation_list

    def binary_word_search(self, filename):
        """Binary Search the word from word list
        Parameters:
            filename: text file
            word: input word to be searched in the file
        Returns:
            prints whether the word is found or not
        """
        my_list = []
        # Splitting the words and adding it to an empty list
        with open(filename, 'r') as f:
            for line in f:
                my_list.extend(line.lower().split())

        new_list = my_list
        # Taking input from the user
        word = input("Enter a word to be searched: ")
        # Traversing through the list to find the input word
        for i in range(len(new_list)):
            if word == new_list[i]:
                print("The word is found")
                break
        else:
            print("The word is not found")

    def insertion_sort(self, elements_number):
        """Insertion Sort
        Parameters:
            elements_number: the length of array as input
        Returns:
            Sorted array
        """
        array_input = []
        # Taking inputs from the user to fill up the values in the list
        for i in range(0, elements_number):
            ele = int(input("Enter a number: "))

            array_input.append(ele)

        print("Input array:", array_input)
        # Traversing from 1 to length of the array
        for i in range(1, len(array_input)):
            k = array_input[i]
            # Move elements of array that are greater than k to one position ahead of their current
            j = i - 1
            while j >= 0 and k < array_input[j]:
                array_input[j + 1] = array_input[j]
                j -= 1
            array_input[j + 1] = k

        print("Sorted array: ")
        for i in range(len(array_input)):
            print(array_input[i])

    def bubble_sort(self, elements_number):
        """Bubble Sort
        Parameters:
            elements_number: the length of array as input
        Returns:
            Sorted array
        """
        array_input = []
        # Taking inputs from the user to fill up the values in the list
        for i in range(0, elements_number):
            ele = int(input("Enter a number: "))

            array_input.append(ele)

        print("Input array:", array_input)

        n = len(array_input)
        # Traverse through all the elements of array
        for i in range(n):
            for j in range(0, n - i - 1):
                # Swap if the element is greater than the next element
                if array_input[j] > array_input[j + 1]:
                    array_input[j], array_input[j + 1] = array_input[j + 1], array_input[j]

        print("Sorted array: ")
        for i in range(len(array_input)):
            print(array_input[i])

    def merge_sort(self, elements_number):
        """Merge Sort
        Parameters:
            elements_number: the length of array as input
        Returns:
            Sorted array
        """
        array_input = []
        # Taking inputs from the user to fill up the values in the list
        for i in range(0, elements_number):
            ele = int(input("Enter a number: "))

            array_input.append(ele)

        print("Input array:", array_input)

        def small_sort(array_input):
            # Dividing the array into two halves until length of array is 1
            if len(array_input) > 1:
                mid = len(array_input) // 2
                L = array_input[:mid]
                R = array_input[mid:]

                small_sort(L)  # Sorting the first half
                small_sort(R)  # Sorting the second half

                i = j = k = 0

                while i < len(L) and j < len(R):
                    if L[i] < R[j]:
                        array_input[k] = L[i]
                        i += 1
                    else:
                        array_input[k] = R[j]
                        j += 1
                    k += 1
                while i < len(L):
                    array_input[k] = L[i]
                    i += 1
                    k += 1
                while j < len(R):
                    array_input[k] = R[j]
                    j += 1
                    k += 1

        print("Sorted Array: ")
        small_sort(array_input)
        for i in range(len(array_input)):
            print(array_input[i], end=" ")
            print()

    def anagram_string(self, string_1, string_2):
        """Anagram Detection
        Parameters:
            string_1: string as input from the user
            string_2: string as input from the user
        Returns:
            Check whether both strings are anagrams of each other
        """
        # Sorting both the strings and comparing
        if sorted(string_1) == sorted(string_2):
            print("The strings are anagrams")
        else:
            print("The strings are not anagrams")

    def prime_numbers_range(self, lower, upper):
        """Prime numbers in a given range
        Parameters:
            lower: lower value of that range
            upper: upper value of the range
        Returns:
            A list of prime numbers in that range
        """
        print("Prime numbers between ", lower, " and ", upper, " are: ")

        my_list = []
        # Traversing though the range
        for num in range(lower, upper + 1):
            # Checking if every number is divisible by their previous all the numbers
            if num > 1:
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    my_list.append(num)
        print(my_list)

    def palindrome_prime(self, lower, upper):
        """Palindrome Prime numbers in a given range
        Parameters:
            lower: lower value of that range
            upper: upper value of the range
        Returns:
            A list of prime numbers that are also palindrome in that range
        """
        def palindrome(num):
            """Creating a function to check if the number is palindrome or not
            Parameters:
                num: integer value
            Returns:
                num if it is palindrome
            """
            rem = 0
            rev = 0
            n = int(num)
            if n > 9:
                while n > 0:
                    rem = n % 10
                    n = int(n / 10)
                    rev = rev * 10 + rem
                    if rev == num:
                        print(num)
                    else:
                        continue

        print("Palindrome Prime numbers between ", lower, " and ", upper, " are: ")
        my_list = []
        # Traversing through the range
        for num in range(lower, upper + 1):
            if num > 1:
                # Check for prime numbers
                for i in range(2, num):
                    if num % i == 0:
                        break
                else:
                    # Check whether the prime number is palindrome and then adding it to the list
                    my_list.append(palindrome(num))
        print(my_list)

    def regex_string(self):
        """Customize Message Demonstration using String Function and RegEx
        Parameters:
            Taking inputs from the user
        Returns:
            prints a message modified with the user inputs
        """
        import re
        import datetime

        print("Read the following message: ")
        message_string = "Hello <<name>>, We have your full name as <<full name>> in our system. \n" \
                         "Your contact number is 91-xxxxxxxxxx. \n" \
                         "Please,let us know in case of any clarification Thank you BridgeLabz 01/01/2016."
        print(message_string)

        first_name = (input("Enter first name: ")).capitalize()
        full_name = (input("Enter full name: ")).title()
        mobile_number = input("Enter mobile number: ")

        year = int(input('Enter a year: '))
        month = int(input('Enter a month: '))
        day = int(input('Enter a day: '))
        # Converting the year, month, day into a date format
        date_format = datetime.date(year, month, day)
        date = str(date_format)
        # Replacing the necessary values using sub function from the re module
        mod_message = re.sub("<<name>>", first_name, message_string)
        mod_message1 = re.sub("<<full name>>", full_name, mod_message)
        mod_message2 = re.sub("xxxxxxxxxx", mobile_number, mod_message1)
        mod_message3 = re.sub("01/01/2016", date, mod_message2)

        print('\n')
        print(mod_message3)



