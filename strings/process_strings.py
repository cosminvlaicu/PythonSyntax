test_string = "a.b.c.d.e.f.g.b"

list_of_segments = test_string.split(".")

for segment in list_of_segments:
    print(segment)

index = test_string.find("b")
print(f'index: {index}')

last_index = test_string.rfind("b")
print(f'last_index: {last_index}')

# substring

test_string = "123456789"
print(f'\n0-2: {test_string[0:2]}')
print(f'1-4: {test_string[1:4]}')
print(f'3-: {test_string[3:]}')

# replace
test_string = "abcdefghijkl"
print(f'\nreplace abc ->  xyz: {test_string.replace("abc", "xyz")}')

# properties
print(f'\nlength: {len(test_string)}')

# regex
