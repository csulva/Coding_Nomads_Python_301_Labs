# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normally return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"

def censor(function):
    def wrapper_func():
        new_func = str(function()).replace('hoot', '****')
        print(new_func)
    return wrapper_func

@censor
def curse():
    return "I stubbed my toe, shoot!"

curse()
