# define function
def high_and_low(numbers):
    # empty list
    new_list = []
    # convert "numbers" variable to a string of numbers--take out blank spaces
    numbers = numbers.split()
    # loop through the numbers to add to new_list -- converting them to ints along the way
    for x in numbers:
        x = int(x)
        new_list.append(x)
    # sort new_list
    new_list = sorted(new_list)
    # return high number + space + lowest number as a string
    return f'{new_list[-1]} {new_list[0]}'

# testing the function
print(high_and_low('1 5 6 -10 5 6'))

