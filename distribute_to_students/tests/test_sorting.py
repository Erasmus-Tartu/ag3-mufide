from sorting_algorithms import *
import pytest

# Test data can be defined as fixtures or module-level variables
l1 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
linked_list1 = convert_to_linked_list(l1)

def test_bubble_sort_list():
    assert bubble_sort(l1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]

def test_bubble_sort_linked_list():
    assert list(bubble_sort(linked_list1)) == [1, 2, 3, 4, 5, 6, 7, 8, 9]