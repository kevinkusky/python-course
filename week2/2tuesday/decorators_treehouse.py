# **************************************************
# Decorators are essentially functions which accept another function as an argument
# typically with an inner function which preforms some action before returnning the accepted function

# *************************************
# Function Review with Closure
# *************************************
# Functions are first class objects
# Functions may be nested within functions - Closure

def outer():
    number = 5

    def inner():
        print(number)

    inner()


# outer()

def apply(func, x, y):
    return func(x,y)


def add(x,y):
    return x + y


def subtract(x,y):
    return x - y


# print(apply(add(10,5)))
# print(apply(subtract(10,5)))


def closureFunction():
    x = 5

    def inner():
        print(x)
    
    return inner

# closureFunction returns pointer to the defined inner function
# variableForInnerFunction = closureFunction()

# When called as a function, variable prints 5 as expected
# variableForInnerFunction()


def add_to_five(num):
    def inner():
        print(num + 5)
    return inner

# More grounded example of closure example from above
fifteen = add_to_five(10)
fifteen()

# *************************************
# Decorators
# *************************************


def logMe(f):
    import logging
    logging.basicConfig(level=logging.DEBUG)

    def inner():
        logging.debug("Called {}".format(f.__name__))
        return f()
    return inner

# Without syntactic sugar
def print_2():
    print(2)

printTwo = logMe(print_2)
# With Logging message
printTwo()

# Still without logging message
print_2()


# With syntactic sugar

@logMe
def print_4():
    print(4)

# Now with logging message and not having to define in seperate variable
print_4()


def logMePart2(f):
    import logging
    from functools import wraps
    logging.basicConfig(level=logging.DEBUG)

    # wraps decorator from functools cleans up things like doc and name rather than self assigning
    @wraps(f)
    def inner(*args, **kwargs):
        # without stars in format to print out tuple and dict respectively
        logging.debug("Called {} with args {} and kwargs {}".format(f.__name__, args, kwargs))
        return f(*args, **kwargs)

    # Manually cleans up docs and names
    # inner.__doc__ = f.__doc__
    # inner.__name__ = f.__name__

    return inner

@logMePart2
def sub(x, y, switch=False):
    return x - y if not switch else y -x

sub(5,2)
sub(5,2, switch=True)

# **************************************************
