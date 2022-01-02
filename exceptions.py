# Errors and exceptions
x = 5
y = -5
if x < 0:
    raise Exception('x should be positive')
assert (y >= 0), 'y is not positive'
try:
    a = 5 / 0
except ZeroDivisionError:
    print('Division by zero')