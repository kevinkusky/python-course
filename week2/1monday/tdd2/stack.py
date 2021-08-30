class Stack:
    def __init__(self):
        self._stack = []

    def __len__(self):
        return len(self._stack)

    def peek(self):
        return self._stack[-1]

    def pop(self):
        return self._stack.pop()

    def push(self, item):
        self._stack.append(item)
