# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


#FIX this 

def symbol(symbol):
    def decorate(function):
        def wrapper(msg):
            print(symbol * 10)
            print(function(msg))
            print(symbol * 10)
        return wrapper
    return decorate

@symbol('<(^^,)>')
def write_something(msg):
    return msg

write_something('Kirby is back')