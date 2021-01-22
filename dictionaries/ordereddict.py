# remembers the order in which keys were INSERTED not modified

from collections import OrderedDict

d = OrderedDict()
d[1] = 1
d[2] = 2
d[3] = 3

print(d)

d[1] = 5
print(d)

del d[1]
d[1] = 3
print(d)
