# Not very pythony class - see below notes for changes

class Invoice:
    def __init__(self, number):
        self._number = number
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def total(self):
        t = 0
        # map items to totals and return sum of new list
        # with list comprehention to be more pythony
        for item in self._items:
            t += item.total()
        return t


class FeeItem:
    def __init__(self, rate, amount, description):
        self._rate = rate
        self._amount = amount
        self._description = description

    # method call rather than property of instance
    def total(self):
        return self._rate * self._amount


class ExpenseItem:
    def __init__(self, amount, description):
        self._amount = amount

    def total(self):
        return self._amount


invoice = Invoice('A1234B')
fee = FeeItem(100, 1.5, 'Phone Conversation')
expense = ExpenseItem(200, 'Copies')

invoice.add_item(fee)
invoice.add_item(expense)


# total methods called as methods
print(invoice)
print(fee.total())
print(expense.total())
print(invoice.total())