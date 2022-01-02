from itertools import product, permutations, combinations
from itertools import combinations_with_replacement
from itertools import accumulate, groupby
import operator

a = [1, 2]
b = [3, 4]
c = [3]
d = [1, 2, 3]
e = [1, 2, 3, 4]
f = [1, 2, 5, 3, 4]

prod1 = product(a, b)
print('Product:')
print(f'Original lists: {a} and {b}')
print(f'Cartesian product of the list: {list(prod1)}\n')
prod2 = product(a, c, repeat=2)
print('Product with repeat:')
print(f'Original lists: {a} and {c}')
print(f'Cartesian product of the list with repeat = 2: {list(prod2)}\n')
perm1 = permutations(d)
print('Permutations')
print(f'Original list: {d}')
print(f'Permutation of the list: {list(perm1)}\n')
perm2 = permutations(e, 2)
print('Permutations with specified length')
print(f'Original list: {e}')
print(f'Permutation of the list with given length = 2: {list(perm2)}\n')
comb1 = combinations(e, 2)
print('Combinations with specified length')
print(f'Original list: {e}')
print(f'Combination of the list with given length = 2: {list(comb1)}\n')
comb_wr = combinations_with_replacement(e, 2)
print('Combinations with replacement')
print(f'Original list: {e}')
print(f'Combination with replacement of the list with given length = 2: {list(comb_wr)}\n')
acc1 = accumulate(e)
acc2 = accumulate(e, func=operator.mul)
acc3 = accumulate(f, func=max)
print('Accumulate')
print(f"Original list: {e}")
print(f"Accumulated sum: {list(acc1)}\n")
print('Accumulate with operator mul')
print(f"Original list: {e}")
print(f"Accumulated sum: {list(acc2)}\n")
print('Accumulate with operator max')
print(f"Original list: {f}")
print(f"Accumulated sum: {list(acc3)}\n")
print('Groupby')
print(f'Original list: {e}')
def smaller_than_3(x):
    return x < 3
group_obj1 = groupby(e, key=lambda x: x < 3)
for key, value in group_obj1:
    print(key, list(value))
print('\nAnother groupby example')
persons = [{'name': 'Tim', 'age': 25}, {'name': 'Dan', 'age': 25},
           {'name': 'Lisa', 'age': 27}, {'name': 'Claire', 'age': 28}]
print(f'Original list: {persons}')
group_obj2 = groupby(persons, key=lambda x: x['age'])
for key, value in group_obj2:
    print(key, list(value))