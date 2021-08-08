# Built in functions

# *********************************************
# All

# Returns a bool
# Are *all* items in iterable True
# **REALLY, are any items false

# Falsy Values - 0, 0.0, '', None, [], False
# *********************************************
titles1 = ['Mr', 'Mrs', 'Ms']
titles2 = ['Mr', 'Mrs', 'Ms', '']
titles3 = []

print(all(titles1), titles1) # True
print(all(titles2), titles2) # False

# All looks for any false item in list
print(all(titles3), titles3) # True



# *********************************************
# Any

# Returns a bool
# Are *any* items in iterable True?

# Truthy Values - Strings, Numbers, Iterables that are not empty or 0
# Essentially, anything that is not falsy
# *********************************************

feedback1 = ['', '', '']
feedback2 = ['I am some words', '', '']
feedback3 = []

print(any(feedback1), feedback1) # False
print(any(feedback2), feedback2) # True

# Any looks for any item to be True
print(any(feedback3), feedback3) # False


# ***********************************************
# Filter
# ***********************************************



# ***********************************************
# Map
# ***********************************************