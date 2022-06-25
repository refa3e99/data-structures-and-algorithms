import pytest

from stack_and_queue.stack_queue import *

s = Stack()
q = Queue()


def test_push_onto_stack():
    s.push(1)
    actual = s.peek()
    expected = 1
    assert actual == expected


def test_push_multi_onto_stack():
    s.push(2)
    s.push(3)
    s.push(4)
    actual = s.peek()
    expected = 4
    assert actual == expected


def test_pop_from_stack():
    actual = s.pop()
    expected = 4
    assert actual == expected


def test_pop_to_empty_a_stack():
    for i in range(3):
        s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


def test_peek_stack():
    s.push(3)
    actual = s.peek()
    expected = 3
    assert actual == expected


def test_enqueue_into_queue():
    q.enqueue(1)
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_enqueue_multi_onto_queue():
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    actual = q.peek()
    expected = 1
    assert actual == expected


def test_dequeue_from_queue():
    actual = q.dequeue()
    expected = 1
    assert actual == expected


def test_dequeue_to_empty_a_queue():
    for i in range(3):
        q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


def test_peek_queue():
    q.enqueue(1)
    actual = q.peek()
    expected = 1
    assert actual == expected
