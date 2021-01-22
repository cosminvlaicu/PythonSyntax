# create lists

lst = [1 for i in range(4)]
print(lst)

lst = [i for i in range(4)]
print(lst)

matrix = [[0 for i in range(4)] for i in range(3)]
print(matrix)

pairs = [(4, 5), (1, 3), (9, 2), (2, 5)]
for index, element in enumerate(pairs):
    print(index)
    print(element)

multiplications = [i * j for i in range(3) for j in range(3)]
print(multiplications)

# concatenate lists
print([1, 2, 3] + [4])

# negative
print(lst[-2])

# statistics
print(f'min: {min(lst)}')
print(f'max: {max(lst)}')
