s1 = {"a", "b", "c"}
print(s1)
print(len(s1))

# set is implemented as a hashtable => O(1) find, insert, delete

if "a" in s1:
    print("a is in s1")

# sets can contain different data types

s2 = {"a", 1, True, 40}

print(s2)

# list to set
lst = [1, 1, 2, 3, 4, 5]
s3 = set(lst)
print(lst)
print(s3)
