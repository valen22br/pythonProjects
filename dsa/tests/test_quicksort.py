from src.quicksort import quicksort

def test_quicksort():
    assert quicksort([1000, 1, 5000, 8000]) == [1, 1000, 5000, 8000]
    assert quicksort([-5, -3, -8, -1]) == [-8, -5, -3, -1]
    assert quicksort([-1, -8]) == [-8, -1]
    assert quicksort([5]) == [5]
    assert quicksort([]) == []
    
