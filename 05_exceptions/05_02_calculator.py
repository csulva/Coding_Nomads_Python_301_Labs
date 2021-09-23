# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

while True:
    dividend = input('Enter a number as your dividend: ')
    divisor = input('Enter a number as your divisor: ')
    try:
        print(int(dividend) / int(divisor))
    except ZeroDivisionError:
        print('You cannot divide by zero friend.')
    except ValueError:
        print('Please enter an integer')
