# Tuples
# Immutable, Ordered, Iterable

# created via () or tuple()

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)
tuple2 = ('a', 'b', 'c', 'd')

# can be declared without () as long as multible items exist
tuple3 = 10, 20, 30


# ********************************************
# Edge Case!!
# Declaring a tuple of a single item
# ********************************************

# Empty tuple
empty = ()

# Prints as just the integer 1
single = (1)
print('No trailing comma: %s' %single)

# Prints tuple with single entry, the integer 1
single = (1,)
print('With trailing comma: %s' %single)

# *****************************************
# Immutable and will throw errors
# attempting to sort or add/ remove
# *****************************************
# tuple1.append(10)
# tuple2.sort()

# Solution to dealing with tuples

shoppingTuple = ('apples', 'milk', 'eggs', 'bacon')

# Below code will sort tuple BUT returns as a list
# alphaShopping = sorted(shoppingTuple)

# *******************************************
# To Solve - wrap in tuple() constructor
# *******************************************

alphaShopping = tuple(sorted(shoppingTuple))

# *******************************************
# Tuples of Lists
#   - cannot add more lists to tuple
#   - CAN add items to each list
# *******************************************

shoppingStops = (
    ['apples', 'milk', 'eggs', 'bacon'],
    ['shoes', 'shirts', 'socks'],
    ['basketball', 'shorts', 'punching bag'],
)

print(shoppingStops)
shoppingStops[1].append('ties')

# Now prints out with 'ties' as the last entry of the second list
print(shoppingStops)


# *******************************************
# Lists of Tuples
#   - cannot add any items to each tuple
#   - CAN add tuples to the list
# *******************************************

users = [
    (1, 'user1'),
    (2, 'cardyB'),
    (3, 'bobby'),
]

print(users)
users.append(tuple(4, 'user4'))

print(users)


# *********************************************
# Assigning Variables with Tuples
# *********************************************

nums = 1, -1, 20, 100, -40, 33, 0

def minmax(numbers):
    # Below return value as tuple
    # comma deliniated list implies ()
    return min(numbers), max(numbers)


# Variable Assignment
# Relies on tuple return from minmax function above
(lowestN, highestN) = minmax(nums)

print(highestN)
print(lowestN)