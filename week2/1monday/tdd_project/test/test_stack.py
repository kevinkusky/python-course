import unittest
from stack import Stack


# Tests with unittest need to begin with test_
class TestStack(unittest.TestCase):
    def test_constructor_is_no_arg(self):
        # Arrange


        # Act
        Stack()

        # Assert

    def test_stack_has_zero_elements(self):
        # Arrange
        s = Stack()

        # Act
        result = len(s)

        # Assert
        self.assertEqual(result, 0)

    def test_push_increases_count_by_one(self):
        # Arrange
        s = Stack()

        # Act
        s.push(True)

        # Assert
        self.assertEqual(len(s), 1)

    def test_peek_returns_last_pushed_item(self):
        # Arrange
        s = Stack()

        # Act
        s.push(True)

        # Assert
        self.assertEqual(s.peek(), True)

    def test__pop_returns_last_pushed_item(self):
        # Arrange
        s = Stack()
        s.push(6.28)

        # Act
        result = s.pop()

        # Assert
        self.assertEqual(result, 6.28)

    def test__push_multiple_items_count(self):
        # Arrange
        s = Stack()


        # Act
        for i in range(100):
            s.push(i)

        # Assert
        self.assertEqual(len(s), 100)

    def test__popping_multiple_items_count(self):
        # Arrange
        s = Stack()


        # Act
        for i in range(100):
            s.push(i)
        for i in range(50):
            s.pop()

        # Assert
        self.assertEqual(len(s), 50)

    def test__peeking_scales_for_last_pushed_element_remaining(self):
        # Arrange
        s = Stack()


        # Act
        for i in range(100):
            s.push(i)
        for i in range(50):
            s.pop()

        # Assert
        self.assertEqual(s.peek(), 49)

