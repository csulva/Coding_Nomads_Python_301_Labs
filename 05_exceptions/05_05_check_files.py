# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

try:
    file_name = 'integers.txt'
    with open(file_name, 'r') as fin:
        data = fin.read()
    print(int(data[0]) / 4)
except ValueError:
    print('Cannot convert to int')
except IOError:
    print('Do you have the correct filename?')

