# Python Inheritance

# *************************************************
# Important Notes
#    - To make code reusable, classes may inherit from a super class
#         - Original class is called parent class 
#               - parent class is also considered superclass
#               - Parent Classes DO NOT have access to any
#                 attributes or behaviors of the child class
#         - Class that inherits from parent class is called childclass
#               - child class is also considered subclass
#               - Child classes inherit all attributes and behaviors
#                 of the parent class
#                     - IMPLICATION: child class can override parent behavior
#               - to call method on parent class below syntax:
#                       super().method(parameter)
# *************************************************


class ParentClass:
    """
    This is a parent class
    """

    def __init__(self, id):
        self._id = id


# ChildClass takes in its parent class
class ChildClass(ParentClass):
    """
    This is a child class which inherits from ParentClass
    """

    # Notice super().__init__(id)
    # runs the init method of the parent class
    def __init__(self, id):
        super().__init__(id)
        self.collection = []

    def add_to_collection(self, item):
        self.collection.append(item)
