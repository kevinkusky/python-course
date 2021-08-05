# Range
# Iterable - counting numbers

# Declared with function range()

# *******************************************
# Important!! 
# - Must be passed at least 1 value
#      - value = int count until

# i.e Count until 10
print(range(10)) # range(0,10)

# Ranges can be type-casted to return more readable output

# i.e seeing the range displayed as a list
# Note: start is 0 and last number is 9
print(list(range(10))) # [0,1,2,3,4,5,6,7,8,9]

# i.e count down from 10
countDown = sorted(range(1,11), reverse = True)
print('Count Down in %s' %countDown) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# May Pass in a step value
# i.e 0 to 50
# Note: stop value is above 50
byFive = range(0,51,5)
print(list(byFive)) # [0,5,10,15,20,25,30,35,40,45,50]

# IMPORTANT
# with steps, you MUST have a start value

# if step is smaller than end value
print(list(range(51,5))) # []

# if step is larger than end value
# Normal range call from 3 until 6
print(list(range(3,6)))


# Loops with Range
items = ['a', 'b', 'c', 'd']

for i in range(len(items)):
    print('index: %s' %i, 'item: %s' %items[i])

# *******************************************