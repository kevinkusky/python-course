# Python Classes

# *************************************************
# Important Notes
#    - Classes are upper camel case (aka: PascalCase)
#    - Best Practice - Add comment at begining of class
#          - Should summarize what the class is intended to do
#          - Other more formal ways to document
#    - Python does not have a new operator.
#          - New instances are called like normal functions
#          - i.e: instance = ExmapleClass()
#    - All instance/class methods on a class must have keyword 'self'
#       as first parameter in definition of method
#          - 'self' is not passed to method when invoked
#    - Non-Public methods and instance variables
#          - Python does not have Private variables for classes
#          - Convention is to add a prefix '_'
#          - Rule of thumb, MOST Instance variables 
#                   should be considered Non-Public
#    - Decorators can be applied to methods, classes, and parameters
#          - Always start with '@'
#          - Types:
#                - property: apply to a method to seem readable (getter)
#                           - @method.setter will allow properties with getters 
#                             defined to be writable (setters)                        
# *************************************************

class ExampleClass:
    # Slots helps python reserve memory for known instance variables
    __slots__ = ['_x', '_y']

    # Python initializers - akin to JS constructor
    # self - akin to this
    def __init__(self, x = 0, y = 0):
        """
        Construct a new class with applicable properties.
        Self - every instance method gets a reference to the object as the first parameter
        """
        self._x = x
        self._y = y
        self._moves = []

    # instance methods not called with self, but are defined with it
    # invoked below method to update y coordinate by 12
    # instance.move_up_by(12)

    def move_y_by(self, delta):
        self._y += delta

    # Defines 'getter' method for x variable
    @property
    def x(self):
        return self._x

    # Relies on 'getter method' above to define 'setter'
    @x.setter
    def x(self, value):
        if value < 0:
            value = 0
        self._x = value

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        if value < 0:
            value = 0
        self._y = value

    # repr overides default output behavior of printing out instance of class
    # i.e
        # without __repr__: <examples.ExampleClass object at 0x10a323e90>
        # with __repr__: <ExampleClass (x, y)>
    def __repr__(self):
        return f"<ExampleClass ({self._x}, {self._y})>"