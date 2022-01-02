import functools


def start_end_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@start_end_decorator
def print_name():
    print('Robert')

# print_name = start_end_decorator(print_name)
# The above line is equivalent to @start_end_decorator

@start_end_decorator
def add5(x):
    return x+5

print_name()
result = add5(5)
print(result)
print(help(add5))
print(add5.__name__)