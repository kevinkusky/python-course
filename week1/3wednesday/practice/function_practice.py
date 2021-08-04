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


def can_nest(L1, L2):
  return min(L1) > min(L2) and max(L1) < max(L2)


print(can_nest([1, 2, 3, 4], [0, 6]))  #> True
print(can_nest([3, 1], [4, 0]))        #> True
print(can_nest([9, 9, 8], [8, 9]))     #> False
print(can_nest([1, 2, 3, 4], [2, 3]))  #> False


GUEST_LIST = {
  "Kurt": "Germany",
  "Julia": "France",
  "Ito": "Japan",
  "Katherine": "England",
  "Sam": "Argentina"
}

# Write your function, here.


def greeting(name):
  if name in GUEST_LIST:
    return f'Hi! I\'m {name} from {GUEST_LIST[name]}.'
  else:
    return "Hi! I'm a guest."

print(greeting("Kurt"))   #> "Hi! I'm Kurt from Germany."
print(greeting("Sam"))    #> "Hi! I'm Sam from Argentina."
print(greeting("Monty"))  #> "Hi! I'm a guest."


# Write your function, here.

def track_robot(directions):
  coords = {'left': 0, 'right': 0, 'up': 0, 'down': 0}
  
  for step in directions:
    step = step.split()
    coords[step[0]] += int(step[1])
  
  return [coords['right'] - coords['left'], coords['up'] - coords['down']]
    

print(track_robot(["right 10", "up 50", "left 30", "down 10"]))
# Prints [-20, 40]

print(track_robot([]))
# Prints [0, 0]
# If there are no instructions, the robot doesn't move.

print(track_robot(["right 100", "right 100", "up 500", "up 10000"]))
# Prints [200, 10500]