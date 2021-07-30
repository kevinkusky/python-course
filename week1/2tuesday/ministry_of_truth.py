a = 1
b = 1.0
c = '1'

print(a == b) # True
print(a == c) # False
print(b == c) # False

# Note '=='
# JavaScript strict equality '===' DOES NOT WORK with Python

# if ( a == c):
#     print("a matches c")
# elif ( a == b):
#     print("a matches b")
# else:
#     print('not a match')


# ***********
# Identity
# ***********

# print(a == b) # True
# print(a is b) # False

# print(b == 1) # True
# print(b is 1) # Evaluated to False BUT produces a warning - 'is with a literal'

# print(c == '1') # True
# print(c is '1') # Evaluates to True BUT produces a warning - 'is with a literal'


# If type matters - isinstance
print(b == 1 and isinstance(b, int)) # False
print(a == 1 and isinstance(a, int)) # True


# With TypeCasting
print(int(b) == 1 and isinstance(b, int)) # Converts b to an int and then checks value

# More TypeCasting examples

print(a)
print(float(a))
print(str(a))

# IMPORTANT
# is looks for 'the same copy' or the same item
print(str(a) is c) # False
print(str(a) == c) # True

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