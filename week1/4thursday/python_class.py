# More Python-y class

class Invoice:
    def __init__(self, number):
        self._number = number
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    # property decorator makes method callable as property of instance
    # i.e - kevins_invoice.total
    @property
    def number(self):
        return self._number

    # @propertyName referse to the above named property
    # .setter allows same method name for getter and setter
    @number.setter
    def number(self, value):
        if value is not None:
            self._number = value

    @property
    def total(self):
        return sum([item.total for item in self._items])


# new class for inheritence - classes share amount and description
class LineItem:
    def __init__(self, amount, description):
        self._amount =  amount
        self._description =  description


class FeeItem(LineItem):
    def __init__(self, rate, amount, description):
        # super with init to inerhit
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