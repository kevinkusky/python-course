from datetime import date

class Book:

    # If You do not need to override shared class variables, 
    # __slots__ will avoid accidental attribute name collisions
    __slots__ = ['_title', '_series', '_author', '_checked_out_on']


    # Class variable - defined directly within a class
    loan_duration = 14 # days

    # Can be set globally via declaration
    # **** Book.loan_duration = 7
    
    # Attempting to set via instance will instead define a 
    # new instance variable which shadows/hides the class variable of the same name
    # **** fellowship_of_the_ring.loan_duration = 3  # // Book.loan_duration is still 7

    # Instance variables defined within __init__
    def __init__(self, title, series, author):
        self._title = title
        self._series = series
        self._author = author
        self._checked_out_on = None

    def checkout(self, checked_out_on=date.today()):
        """Method to checkout a book."""
        self._checked_out_on = checked_out_on


    def is_overdue(self):
        """Method to check if a book is overdue."""
        overdue = False

        if self._checked_out_on is not None:
            elapsed_days = (date.today() - self._checked_out_on).days
            overdue = elapsed_days > self.loan_duration

        return overdue

    # Class Method
    # first argument, cls, PEP 8 convention much like the self argument
    @classmethod
    def create_series(cls, series, author, *args):
        """
        Factory class method creates a series of books.
        """
        return [ cls(title, series, author) for title in args ]

    # Static method
    @staticmethod
    def get_titles(*args):
        """
        Static method accepts a variable number of Book instances
        returning a list of their titles.
        """
        return [ book._title for book in args ]


    def __repr__(self):
        return f"{self._title} by {self._author}"


fellowship_of_the_ring = Book(
    "The Fellowship of the Ring",
    "The Lord of the Rings",
    "J.R.R. Tolkien")

grapes_of_wrath = Book(
    "The Grapes of Wrath",
    None,
    "John Steinbeck")

# Access the `loan_duration` class variable
# from the class instances.
print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(fellowship_of_the_ring.loan_duration)  # 14
print(grapes_of_wrath)  # The Grapes of Wrath by John Steinbeck
print(grapes_of_wrath.loan_duration)  # 14

# Now change the `loan_duration` class variable value
# through the `Book` class.
Book.loan_duration = 7

# The new `loan_duration` class variable value
# is available on each existing instance.
print(fellowship_of_the_ring.loan_duration)  # 7
print(grapes_of_wrath.loan_duration)  # 7

# Neither book currently has a checkout date and thus False for overdue
print(fellowship_of_the_ring.is_overdue()) # False
print(grapes_of_wrath.is_overdue()) # False

# Adds a checkout date to Fellowship
fellowship_of_the_ring.checkout(checked_out_on=date.fromisoformat("2020-04-04"))

# Now fellowship returns as overdue
print(fellowship_of_the_ring.is_overdue()) # True
print(grapes_of_wrath.is_overdue()) # False

# Utilizing class method
# Call class method to create a series of books.
lord_of_the_rings = Book.create_series(
    "The Lord of the Rings",
    "J.R.R. Tolkien",
    "The Fellowship of the Ring",
    "The Two Towers",
    "The Return of the King"
)

print(lord_of_the_rings)
# [The Fellowship of the Ring by J.R.R. Tolkien, The Two Towers by J.R.R. Tolkien, The Return of the King by J.R.R. Tolkien]

# Unpack the lord_of_the_rings list into the individual books.
fellowship_of_the_ring, two_towers, return_of_the_king = lord_of_the_rings

print(fellowship_of_the_ring)  # The Fellowship of the Ring by J.R.R. Tolkien
print(two_towers)  # The Two Towers by J.R.R. Tolkien
print(return_of_the_king)  # The Return of the King by J.R.R. Tolkien
