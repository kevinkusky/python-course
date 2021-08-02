# 2 Main Types

# Type 1 - basic

def xor(param1, param2):
    return param1 != param2



# Type 2 - Lambda
# In JS this is akin to arrow functions

xor2 = lambda p1, p2: p1 != p2


# *******************************************
# Default values and other cool function tips
# *******************************************

# default assignment of exp
def powers_of(b, exp=1):
    p_list = []
    i = 1
    while i < exp + 1:
        p_list.append(b**i)
        i += 1
    return p_list


# invoking with 1 parameter allows function to run with default exp value of 1
powers_of(15)

# Alternatively, functions can be invoked specifing parameters regardless of implicit ordering from function def
powers_of(exp=4, b=9)

# Common Python way of invoking a function known to have a defualt value for readability
powers_of(2, exp=10)