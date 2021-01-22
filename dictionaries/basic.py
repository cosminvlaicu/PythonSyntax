d = {}

d[1] = 2

print(d)

d[1] = 3
print(d)

d[2] = 2
print(d)
del d[2]
print(d)

d[3] = 3
print(d)

# delete
if 3 in d:
    del d[3]

if 4 in d:
    del d[4]

print(d)

# combine
d1 = {1: 2}
d2 = {1: 1, 2: 3}

d3 = {**d1, **d2}
print(d3)

# useful methods
d[2] = 3
for key, value in d.items():
    print(key, value)
