import sys

def fibonacci(limit):
    a, b = 0, 1
    while(a < limit):
        yield a
        a, b = b, a + b

fib = fibonacci(30)
for i in fib:
    print(i)

mylist = [i for i in range(1000000) if i % 2 == 0]
mygenerator = (i for i in range(1000000) if i % 2 == 0)
print(sys.getsizeof(mylist))
print(sys.getsizeof(mygenerator))