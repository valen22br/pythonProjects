from src.recursive_find_maximum import recursive_find_maximum

def test_recursive_find_maximum():
    assert recursive_find_maximum([-1, -3, -8, -500]) == -1
    assert recursive_find_maximum([90, 1, 56, 101]) == 101