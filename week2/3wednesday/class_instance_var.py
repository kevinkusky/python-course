from datetime import date

class Book:
    # Class variable - defined directly within a class
    loan_duration = 14 # days

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