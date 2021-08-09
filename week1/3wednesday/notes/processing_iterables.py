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

# filter(function, iterable)
# 
# 
# ***********************************************

scores = [90, 100, 69, 79, 85, 80, 50]

def isA(grade):
    return grade >= 90

aScores = filter(isA, scores)


# to read - must typecast
print(list(aScores))

# ***********************************************
# Map
# ***********************************************

def getGrade(grade):
    if (grade >= 90):
        return 'A'
    elif (grade < 90 and grade >= 80):
        return 'B'
    elif (grade < 80 and grade >= 70):
        return 'C'
    elif (grade < 70 and grade >= 60):
        return 'D'
    else:
        return 'F'


grades = list(map(getGrade, scores))

print(grades)

# Zipped grades and scores
combined = list(zip(scores, grades))
print(combined)

