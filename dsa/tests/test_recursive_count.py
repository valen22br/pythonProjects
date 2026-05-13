from src.recursive_count import recursive_count

def test_recursive_count():
    assert recursive_count([]) == 0
    assert recursive_count([1, -1, 2, -2]) == 4