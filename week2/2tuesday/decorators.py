# ***************************************************
# Decorators - what they are, how to roll your own

# Functions which accept a callback function as an argument
# These functions wrap an inner function forming a closure
# and can be used to modify behavior dynamically

def myDecorator(f):
    def wrapperFunction():
        print('I am a wrapper')
        return f()
    return wrapperFunction


# With syntactic sugar
@myDecorator
def functionDecorated():
    print('I am a decorated function')


# Without syntactic sugar
def notDecoratedFunction():
    print('Assigned as a decorated function')


nowDecoratedFunction = myDecorator(notDecoratedFunction)


# More Realistic Example
def exponentDecorator(f):
    def wrapper(base, exp):
        return base ** f(exp)
    return wrapper

@exponentDecorator
def parseExponent(exp):
    return int(exp)

# With Args and Kwargs
def expFunctionDecorator(f):
    def wrapper(*args, **kwargs):
        # mult assign with args
        # base, exp = args
        # return base ** f(exp)
        
        # key into dict with kwargs
        return kwargs['base'] ** f(kwargs['exp'])
    return wrapper

# ***************************************************
