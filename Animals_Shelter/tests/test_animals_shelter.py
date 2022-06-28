import pytest

from Animals_Shelter.AnimalsShelter import *

AS = AnimalShelter()

def test_enqueue_dog():
    dog1 = Dog('Luna')
    AS.enqueue(dog1)
    actual = AS.dequeue('Dog')
    expected = 'Luna'
    assert actual == expected


def test_enqueue_cat():
    cat1 = Cat('stinky')
    AS.enqueue(cat1)
    actual = AS.dequeue('Cat')
    expected = 'stinky'
    assert actual == expected


def test_enqueue_dog2():
    dog2 = Dog('dragon')
    dog3 = Dog('petty')
    AS.enqueue(dog2)
    AS.enqueue(dog3)
    actual = AS.dequeue('Dog')
    expected = 'dragon'
    assert actual == expected


def test_enqueue_cat2():
    cat2 = Cat('koko')
    cat3 = Cat('zeus')
    AS.enqueue(cat2)
    AS.enqueue(cat3)
    actual = AS.dequeue('Cat')
    expected = 'koko'
    assert actual == expected


def test_enqueue_other_pref():
    cat2 = Cat('koko')
    AS.enqueue(cat2)
    actual = AS.dequeue('Rat')
    expected = None
    assert actual == expected