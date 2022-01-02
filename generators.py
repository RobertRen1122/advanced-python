import sys

def mygrenerator():
    yield 1
    yield 2
    yield 3

def countdown(num):
    print('Starting')
    while num >= 0:
        yield num
        num -= 1

def firstn(n):
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

def firstn_generator(n):
    num = 0
    while num < n:
        yield num
        num += 1

g = mygrenerator()
# for i in g:
#     print(i)

value = next(g)
print(value)
print(sum(g))

cd = countdown(4)
value = next(cd)
print(value)

print(sys.getsizeof(firstn(1000000)))
print(sys.getsizeof(firstn_generator(1000000)))



