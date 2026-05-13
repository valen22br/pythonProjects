from src.binary_search import binary_search

def test_binary_search():
    assert binary_search([1, 2, 3, 5, 9, 10], 10) == 5
    assert binary_search([1, 2, 3, 5, 9, 10], 4) == None