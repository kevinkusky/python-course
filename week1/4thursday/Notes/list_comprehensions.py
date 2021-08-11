# Review - For Loops and Mapping

# Loop Review
# creates empty list and appends value while iterating through iterable (range in this case)
forSquares = []
for i in range(10):
    forSquares.append(i**2)


# Mapping - creates a map object via function and iterable (range in this case)
# Type casted to list to be printable
mapSquares = list(map(lambda x: x**2, range(10)))

# ********************************************
# List Comprehensions

# WHEN NOT TO USE
# May make code run slowly or take up more memory 


# new_list = [expression for item in iterable (if condition)]

# Note - conditional logic is not necissary for a list comprehension
# i.e - new_list = [expression for item in iterable]

compSquares = [i**2 for i in range(10)]
# ********************************************
# i**2 - expression
# i - item
# range(10) - iterable
# n/a - condition
# ********************************************


sentence = 'the rocket came back from mars with no marsbars'
vowels = [char for char in sentence if char in 'aeiou']

# Note: An expression can also just be the item
#       if no opperation needs to be proformed on it
# ********************************************
# char - expression
# char - item
# sentence - iterable
# char in 'aeiou' - condition
# ********************************************


def is_consonant(char):
    vowelChars = 'aeiou'
    return char.isalpha() and char.lower() not in vowelChars


s2 = 'Mary, Mary, quite contrary, how does your garden grow? Diva Cup?'

consts = [c for c in s2 if is_consonant(c)]

# ** In this exampe, the conditional is the bool
#    returned from the is_constant method
# ********************************************
# c - expression
# c - item
# s2 - iterable
# is_constant(c) - condition
# ********************************************


# What if you want to change values rather than filter
# with your conditional logic?

# new_list [expression (if condition) for item in iterable]

# Since we don't want a negative price, lets try...
startPrice = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]

# Essentially: p unless it is less than 0, otherwise replace with 0
newPrice = [p if p > 0 else 0 for p in startPrice]

# ********************************************
# p - expression
# p > 0 - condition
#       - else statement
# p - item
# startPrice - iterable
# ********************************************

# Same as above but seperating into seperate method
def get_price(p):
    return p if p > 0 else 0

altPrice = [get_price(p) for p in startPrice]


# Nesting comprehensions
# Outter - [... for _ in range(6)] # creates 6 rows
# Inner - [m for m in range(5)] # populates row with values

matrix =[[m for m in range(5)] for _ in range(6)]


m2 = [
    [0,0,0],
    [1,1,1],
    [2,2,2],
]

# Sometimes not the most readable!!! - use wisely 
flat = [n for row in m2 for n in row]