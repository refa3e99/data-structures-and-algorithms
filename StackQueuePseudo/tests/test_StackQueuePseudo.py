import pytest

from StackQueuePseudo.Stack_Queue_Pseudo import *

pq = PseudoQueue()


def test_enqueue():
    pq.enqueue(1)
    actual = pq.dequeue()
    expected = 1
    assert actual == expected


def test_multi_enqueue():
    pq.enqueue(2)
    pq.enqueue(3)
    pq.enqueue(4)
    actual = pq.dequeue()
    expected = 2
    assert actual == expected


def test_dequeue():
    pq.dequeue()
    actual = pq.dequeue()
    expected = 4
    assert actual == expected
