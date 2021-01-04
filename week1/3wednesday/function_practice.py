# Write your function, here.


def get_first_value(list):
  return list[0]


print(get_first_value([1, 2, 3]))        #> 1
print(get_first_value([80, 5, 100]))     #> 80
print(get_first_value([-500, 0, 50]))    #> -500

# Write your function, here.

def get_sum(list):
  return sum(list)

print(get_sum([2, 7, 4]))     #> 13
print(get_sum([45, 3, 0]))    #> 48
print(get_sum([-2, 84, 23]))  #> 105

# Write your function, here.

def get_indices(items, item):
  indices = []
  for i in range(0, len(items)):
    if item == items[i]:
      indices.append(i)
  return indices


print(get_indices(["a", "a", "b", "a", "b", "a"], "a"))
# Prints [0, 1, 3, 5]

print(get_indices([1, 5, 5, 2, 7], 7))
# Prints [4]

print(get_indices([1, 5, 5, 2, 7], 5))
# Prints [1, 2]

print(get_indices([1, 5, 5, 2, 7], 8))
# Prints []