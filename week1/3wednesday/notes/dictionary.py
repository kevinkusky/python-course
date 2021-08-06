# Dictionaries

# created via {} or dict()


book = {
    'title':'Manufacturing Consent',
    'ratings': 4629,
    'stars': 4.9,
    'author': {'fname': 'Noam', 'lname': 'Chomsky'},
    'images': ['author.png', 'cover.png'],
}

print(book)

# Returns the number of keys
print(len(book))

# Delete key value pair by indexing the key with the 
# 'del' keyword
del book['stars']
print('book without stars: %s' %book)

# Set a key value pair via declaration
book['stars'] = 4.99
print('book with stars: %s' %book)


# Iterate through a dictionary
for key in book:
    print(key, book[key])


# *****************************************
# Other ways of declaring dictionaries
# *****************************************

# Via dict() constructor.

# key value setting
pond = dict(
    depth = 10,
    area = 500,
    fish = ['Harold', 'Bean', 'Frankie', 'Bongo']
)

print(pond)


# with a list of tuples
alligator = dict([
    ('length', 3.4),
    ('species', ['American Alligator', 'Chinese Alligator']),
    ('paragraph','I know very little about Alligators. '
                +'So take what you see here with a healthy '
                +'grain of salt.  They have 3,000 teeth, maybe?'),
])

print(alligator)


# *****************************************
# Data in seperate peices
# *****************************************

# Header row from a table
keys = ['name', 'hr', 'rbi', '.avg']

# Row from data set
values = ['Babe Ruth', 7214, 10000, 0.313]

# zip() function pairs key and values to help form dictionary
player = dict(zip(keys, values))

print(player)

# dir() function - inspect meta data about object
# print(dir(player))