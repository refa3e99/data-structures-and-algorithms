import pytest
from hashtable.hashtable import HashTable
from hashmap_left_join.hashmap_left_join import left_join



def test_one():
    h1 = HashTable()
    h1.set('abdulrahman', 22)
    h1.set('ahmed', 29)
    h1.set('asaad', 19)
    h1.set('malik', 23)

    h2 = HashTable()
    h2.set('abdulrahman', 'python')
    h2.set('ahmed', 'JAVA')
    h2.set('asaad', 'JavaScript')
    h2.set('Roaa', 'PHP')

    actual = left_join(h1, h2)
    expected = [['abdulrahman', '22', 'python'], ['ahmed', '29', 'JAVA'], ['asaad', '19', 'JavaScript'], ['malik', '23', None]]

    assert actual == expected


def test_two():
    h1 = HashTable()
    h1.set('mohammed', 22)
    h1.set('khalid', 29)
    h1.set('yusra', 19)
    h1.set('raghad', 23)

    h2 = HashTable()
    h2.set('mohammed', 'python')
    h2.set('ahmed', 'JAVA')
    h2.set('yusra', 'JavaScript')
    h2.set('Roaa', 'PHP')

    actual = left_join(h1, h2)
    expected = [['mohammed', '22', 'python'], ['khalid', '29', None], ['yusra', '19', 'JavaScript'], ['raghad', '23', None]]

    assert actual == expected