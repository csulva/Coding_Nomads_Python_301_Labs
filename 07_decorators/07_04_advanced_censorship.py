# Build on top of the censorship exercise and change your decorator function
# so that you can pass the words it should censor when decorating a function, e.g.:
# `@censor("shoot", "crab")` would censor the words "shoot" and "crab".

def bad_words(*words):
    def censor(function):
        def wrapper_func(msg):
            sentence = str(function(msg))
            for word in words:
                asterisk = len(word) * '*'
                sentence = sentence.replace(word, asterisk)
            print(sentence)
        return wrapper_func
    return censor

@bad_words('shoot', 'crab', 'foul', 'test')
def lets_talk(msg):
    return msg

lets_talk('shoot I hate crabs and fouls and tests')