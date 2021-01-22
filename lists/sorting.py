# basic
numbers = [4, 6, 2, 1, 6, 3, 2, 6]
names = ["ksda", "sadsa", "asdsa", "aa", "zz"]

numbers.sort()
names.sort()
print(numbers)
print(names)

# reverse
numbers = [4, 6, 2, 1, 6, 3, 2, 6]
names = ["ksda", "sadsa", "asdsa", "aa", "zz"]

numbers.sort(reverse=True)
names.sort(reverse=True)
print(numbers)
print(names)

pairs = [(4,5), (1,3), (9,2), (2,5)]
pairs.sort()
print(pairs)


#custom sorting

def custom_sort(element):
    return element[1]

pairs = [(4,5), (1,3), (9,2), (2,5)]
pairs.sort(reverse=False, key=custom_sort)
print(pairs)
