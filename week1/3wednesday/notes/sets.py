# Sets

# Unordered, Group of Unique elements
# Lists or values inside {}

# Opporators explained below:
# |, &, -, ^

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

# *********************************
# Comparison Operators
# *********************************

# Union - Combine sets via | operator

# Note: how the return only has One entry of 3 and 4
# Set values must be unique
print(a | b) # {1, 2, 3, 4, 5, 6}


# Intersection - Return set of all items in Both Sets via & operator
print(a & b) # {3, 4}


# Difference - Return set of all items different between Two Sets
# **********************************************
# IMPORTANT - difference opporator computes left from right
#           - what is in left that is not in right
# ***********************************************
print(a - b) # {1, 2}
print(b - a) # {5, 6}

# Symetric difference - total difference with ^ opporator
print(a ^ b) # {1, 2, 5, 6}


a = set('apple')
b = set('banana')

# Notice: the duplicate chars fall off and return order is unordered

print(a) # {'a', 'p', 'l', 'e'}
print(b) # {'b', 'n', 'a'}

# Union of the two leaves only 1 a when apple and banana have 4
# Sets will always be unique
print(a | b) #{"p", "l", "e", "b", "n", "a"}

# ***************************************************
# .chain opporators

print(a.union(b))
print(a.intersection(b))
print(a.symmetric_difference(b))
print(b.difference(a))
# ***************************************************


basket = ['apple', 'banana', 'orange', 'apple', 'apple', 'cheese', 'meat']

# Flattens list as set
print(set(basket)) # {'apple', 'banana', 'orange', 'meat', 'cheese'}

# ***************************************************
# Real world examples
# Combining different Data Structures
# ***************************************************
purchaseEmails = ('bob101@aol.com', 'yojo1231@yahoo.com', 'morganstushy@aim.com', 'sam@yahoo.com')
helpEmails = ('kevinsky@gmail.com', 'bob101@aol.com', 'sam@yahoo.com')

# Utilizing Intercection
print('Users making a purchase and also calling help desk')
print(set(purchaseEmails) & set(helpEmails)) # {'bob101@aol.com', 'sam@yahoo.com'}


posts = [
    {'title': 'all about lists', 'tags': ('fun', 'informative', 'lists')},
    {'title': 'Tuple Trouble', 'tags': ('fun', 'tuples')},
    {'title': 'Sparkling Sets', 'tags': ('informative', 'numbers')},
]


# extend method adds multible items to a list
allTags = []
for i in range(len(posts)):
    allTags.extend(posts[i]['tags'])

# Typecast as set & removes duplicates
# Since Sets are unsorted
# Typecast as list again to sort data
allTags = list(set(allTags))
allTags.sort()

# allTags now sorted and unique
print(allTags)

