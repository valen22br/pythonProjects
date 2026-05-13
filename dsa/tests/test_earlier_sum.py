from src.earlier_sum import sum

def test_earlier_sum():
    assert sum([1, 1000]) == 1001
    assert sum([-1, -5]) == -6
