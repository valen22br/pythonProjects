def recursive_count(list):
    if list == []:
        return 0
    return 1 + recursive_count(list[1:])

print(recursive_count([1,2,3,4,5]))