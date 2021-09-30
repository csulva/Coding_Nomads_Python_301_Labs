# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.

import datetime


def time_executor(func):
    def wrapper_func(*args):
        return f'Target heart rate: {func(*args)}' + f' executed at: {datetime.datetime.now()}'
    return wrapper_func

@time_executor
def target_heart_rate(max_heart_rate, age):
    return max_heart_rate - age

print(target_heart_rate(180, 28))