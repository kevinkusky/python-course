class Invoice:
    # slots property optimization
    # list of instance variables as strings
    __slots__ = ['_numbers', '_items']
    def __init__(self, number):
        # underscore treats property as private
        self._number = number
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    # property decorator makes method callable as property of instance
    # i.e - kevins_invoice.total
    @property
    def number(self):
        return self._number

    # @propertyName refers to the above named property
    # .setter allows same method name for getter and setter
    @number.setter
    def number(self, value):
        if value is not None:
            self._number = value

    @property
    def total(self):
        return sum([item.total for item in self._items])

    def __repr__(self):
        # python formatting 
        # :.2f - float and sig figs
        return f"<Invoice {self._number} ${self.total:.2f}>"


# new class for inheritence - classes share amount and description
class LineItem:
    __slots__ = ['_amount', '_description']
    def __init__(self, amount, description):
        self._amount =  amount
        self._description =  description


class FeeItem(LineItem):
    __slots__ = ['_rate']
    def __init__(self, rate, amount, description):
        # super with init to inerhit
        # super binds 'self' to methods of inherited class
        super().__init__(amount, description)
        self._rate = rate

    @property
    def total(self):
        return self._rate * self._amount


class ExpenseItem(LineItem):
    def __init__(self, amount, description):
        super().__init__(amount, description)

    @property
    def total(self):
        return self._amount


invoice = Invoice('A1234B')
fee = FeeItem(100, 1.5, 'Phone Conversation')
expense = ExpenseItem(200, 'Copies')

invoice.add_item(fee)
invoice.add_item(expense)

print(invoice.total)

print(invoice.number)
invoice.number ='banana5'
print(invoice.number)

print(invoice)  