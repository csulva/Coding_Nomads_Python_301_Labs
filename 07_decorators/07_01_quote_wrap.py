# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def add_quotes(func):
    def wrapper_func():
        return f'"{func()}"'
    return wrapper_func

@add_quotes
def lets_print():
    return 'test'

def add_quotes_again(func):
    def wrapper_function():
        return '"'+func+'"'
    return wrapper_function

print(lets_print())
print(add_quotes_again('let\'s try this again')())