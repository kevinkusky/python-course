import pytest
from stack import Stack


def test_constructor_in_no_arg():
    Stack()


def test_new_stack_empty():
    if True:
        pytest.skip()
    assert len(Stack()) == 0


def test_push_increases_len_by_1():
    s = Stack()
    s.push(None)
    assert len(s) == 1


def test_peek_returns_most_recent_pushed_item():
    s = Stack()
    s.push(2.22)
    assert s.peek() == 2.22
    assert len(s) == 1


def test_pop_returns_last_item_and_removes_from_stack():
    s = Stack()
    s.push(2.22)
    assert s.pop() == 2.22
    assert len(s) == 0


def test_mult_push_adjust_len_correctly():
    s = Stack()
    for i in range(1000):
        s.push(i)
    assert len(s) == 1000


def test_mult_pop_adjust_len_correctly():
    s = Stack()
    for i in range(1000):
        s.push(i)
    for i in range(100):
        s.pop()
    assert len(s) == 900


def test_peek_still_works_at_scale():
    s = Stack()
    for i in range(1000):
        s.push(i)
    for i in range(100):
        s.pop()
    assert s.peek() == 899
