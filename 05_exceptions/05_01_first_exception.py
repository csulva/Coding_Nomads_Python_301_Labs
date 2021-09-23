# Write a script that generates an exception.
# Handle this exception with a try/except block.
# This raises and exception that needs to be handled.

list_1 = ['hello world!']
try:
    print(list_1[1])
except IndexError:
    print('It\'s not going to wooork!')
