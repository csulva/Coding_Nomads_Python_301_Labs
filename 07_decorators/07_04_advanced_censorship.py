# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def bad_words(*words):
    def censor(function):
        def wrapper_func(msg):
            new_words = str(words)
            new_func = str(function(msg)).replace(new_words, '*')
            print(new_func)
        return wrapper_func
    return censor

@bad_words('shoot', 'crab', 'foul')
def lets_talk(msg):
    return msg

lets_talk('shoot I hate crabs and fouls')