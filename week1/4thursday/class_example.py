

class Invoice:
    def __init__(self, number):
        self._number = number
        self._items = []

    def add_item(self, item):
        self._items.append(item)


class FeeItem:
    def __init__(self, rate, amount, description):
        self._rate = rate
        self._amount = amount
        self._description = description

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