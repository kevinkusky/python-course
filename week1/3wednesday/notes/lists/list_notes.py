# About
# Mutable, Ordered, Iterable

# created via [] or list()

# ********************************************
# Indexing
# ********************************************
friends = ['Kevin', 'Morgan', 'James', 'Anthony', 'Carly', 'Cassidy']

# 0 indexed from start
print(friends[2]) # 3rd from start name - James

# Look back via negative indicies (-1 = last item)
print(friends[-2]) # Second to last listed name - Carly

# Pull a range of listed items via : indicies
# *********************************************
# Important Notes
#  - second index value is not included in return
#  - do not need to enter values 
#      if you want to inclue everything
#  - optional 3rd index value for step considerations
# *********************************************

# All but first and last
print(friends[1:-1]) # ['Morgan', 'James', 'Anthony', 'Carly']

# All but last
print(friends[:-1]) # ['Kevin', 'Morgan', 'James', 'Anthony', 'Carly']

# Every other entry starting from the first and up until the last
# Step value is 2, start and stop are not entered implying all
print(friends[::2]) # ['Kevin', 'James', 'Carly']

# With the same step and different start, the return alters
print(friends[1::2]) # ['Morgan', 'Anthony', 'Cassidy']

# *********************************************
# Opperations
# *********************************************
supplies = ['lighter', 'Water', 'Guitar', 'steel drum', 'pocket knife', 'compass']

# *********************************************
# Determine length
# *********************************************
print(len(supplies)) 

# *********************************************
# Add list item/ Remove list item
# *********************************************
# List as is
print(supplies)

# Adds new supply - can opener
supplies.append('can opener')
print(supplies)

# Remove specific supply - steel drum
supplies.remove('steel drum')
print(supplies)

# **********************************************
# Sort List
# **********************************************

# Note!!!
# Python treats capital and lower case as different values when sorting
supplies.sort()
print(supplies)

# To solve - pass a key for sort to sort by
supplies.sort(key=str.lower)

# Function in key DOES NOT perminately alter items in list
# i.e Water and Guitar stil titalized
print(supplies)


# Make sorted copies without altering original - sorted() function
colors = ['red', 'yellow', 'green', 'blue', 'orange']
alpha_colors = sorted(colors)

# reverse flag to return sort in reverse
reverse_alpha = sorted(colors, reverse=True)

print(colors)
print(alpha_colors)
print(reverse_alpha)

# Reversed Creates different type of iterator which is not print friendly
reverse_standard = reversed(colors)
reverse_alpha_2 = reversed(alpha_colors)

# Solve by type-casting

print(list(reverse_standard))
print(list(reverse_alpha_2))


# *********************************************
# Math with Lists
# *********************************************

scores = [100, 90, 50, 70, 88, 93]

# sum() function to add list items
totalScore = sum(scores)

# max() function pulls highest value
highScore = max(scores)

# min() function pulls smallest value
highScore = min(scores)

# no function for average - utilize len and sum
avgScore = sum(scores)/len(scores)

# Alternatively you can roll your own avg() function
# def avg(scores):
#     return sum(scores) / len(scores) 