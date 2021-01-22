# range
s = "string"
for i in range(len(s) - 1, -1, -1):
    print(s[i])

# concatenate tuples
print((1, 1) + (2, 2))

# binary search
# left
from bisect import bisect_left


def BinarySearch(array, x):
    index = bisect_left(array, x)
    if index != len(array) and array[index] == x:
        return index
    else:
        return -1


# right
from bisect import bisect_right


def BinarySearchRight(array, x):
    index = bisect_right(array, x)
    if index - 1 != len(array) and array[index - 1] == x:
        return index - 1
    else:
        return -1


a = [1, 2, 4, 4, 4, 8, 8]
print(f'binary search index:  {BinarySearch(a, 4)}')
print(f'binary search index right:  {BinarySearchRight(a, 10)}')

# random
import random

random.seed(1)
ri = random.randint(0, 10)
rf = random.uniform(0, 1)

print(ri)
print(rf)


# class

class TestClass:
    def __init__(self, a):
        self.attribute = a

    def modify(self, number):
        self.attribute = number


t = TestClass(4)
t.modify(3)
print(t.attribute)

# tuples
print("\ntuples")
a = (1, 2)
b = (3, 4, 5)
print(a)
print(a + b)
print(b[0:2])
