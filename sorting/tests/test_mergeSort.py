from merge.mergeSort import mergeSort

import pytest

def test_reverse_sorted():
    arr = [20,18,12,8,5,-2]
    actual = mergeSort(arr)
    expected = [-2,5,8,12,18,20]
    assert actual == expected

def test_few_uniques():
    arr = [5,12,7,5,5,7]
    actual = mergeSort(arr)
    expected = [5,5,5,7,7,12]
    assert actual == expected

def test_nearly_sorted():
    arr = [2,3,5,7,13,11]
    actual = mergeSort(arr)
    expected = [2,3,5,7,11,13]
    assert actual == expected