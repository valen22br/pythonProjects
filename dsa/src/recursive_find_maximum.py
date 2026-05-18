def recursive_find_maximum(list):
    if len(list) == 2:
        return list[0] if list[0] > list[1] else list[1]
    sub_max = recursive_find_maximum(list[1:])
    return list[0] if list[0] > sub_max else sub_max


print(recursive_find_maximum([1, 5, 500, 99, 501]))

print(recursive_find_maximum([90, 1, 56, 101, 102]))