import numpy as np

# from list
arr = np.array([1, 2, 3, 4, 5])
arr2d = np.array([[1, 2, 3, 4], [3, 4, 5, 6], [5, 6, 7, 8]])
arrf = np.array([1, 2, 3, 4, 5], dtype=float)
print(arr)
print(arr2d)
print(arrf)

# change type
print(arr.astype(dtype=float))

# dimensions
print(arr.ndim)
print(arr2d.ndim)

print(arr.shape)
print(arr2d.shape)

# get type
print(arr.dtype)

# other useful attributes
print(arr.itemsize)
print(arr.size)
print(arr.nbytes)

# indexing
print(arr2d[1, 1])
print(arr2d[0, :])
print(f'Advanced indexing:\n{arr2d[arr2d >2]}')
print(f'Advanced indexing:\n{arr[[1,2]]}')


print(f'start:end:stepsize: {arr[1:4:2]}')
print(f'start:end:stepsize:\n {arr2d[0:3:2, 0:3:2]}')

# fast create
z = np.zeros((1, 2, 3))
o = np.ones((1, 2, 3), dtype=int)
r = np.random.rand(2, 3)
ri = np.random.randint(0, 10, (10, 10))
iden = np.identity(5)
a = np.ones((2, 3))

print(z)
print(o)
print(r)
print(ri)
print(iden)

# axes
# think of axis as a jump index to find the next value for applying the function
# for example min: min(a, a+index, a+2*index...)
#   if axis = 0, index=#cols  (you skip the cols)
#   if axis = 1, you are on the innermost dimension and don't skip anything
arr2d = np.array([[1, 2, 3]])
rep = np.repeat(arr2d, 3, axis=0)
print(rep)

# copy
original = np.ones((2, 2))
copy_matrix = original.copy()
print(copy_matrix)

# Linear Algebra
a = np.ones((2, 3))
b = np.full((3, 2), 3)
print(np.matmul(a, b))

# statistics
r = np.random.rand(2, 3)
print(f'global min: {np.min(r)}\n from:\n{r}')
print(f'cols min: {np.min(r, axis=0)}\n from:\n{r}')
print(f'rows min: {np.min(r, axis=1)}\n from:\n{r}')

print(f'sum: {np.min(r)}\n from:\n{r}')

# reshape
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(a.reshape((2, 2, 2,)))

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack((v1, v2)))


