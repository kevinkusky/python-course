a = 1
b = 1.0
c = '1'

print(a == b)
print(a == c)
print(b == c)

# Note '=='
# JavaScript strict equality '===' DOES NOT WORK with Python

# if ( a == c):
#     print("a matches c")
# elif ( a == b):
#     print("a matches b")
# else:
#     print('not a match')

# truthy values
a = 'dart'
a = ['a', 'b', 'c']

# falsey values
a = 0
a = 0.0
a = ''
a = None
a = []
a = False


if (a):
    print(f'{a} is truthy')
else:
    print(f'{a} is falsey')