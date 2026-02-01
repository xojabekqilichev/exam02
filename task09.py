def find_min_max(numbers: list) -> dict:
    num = {}
    result = max(numbers)
    res = min(numbers)
    num['max'] = result
    num['min'] = res
    return num
numbers = [3, 7, 10, -5, -8, 15, 22]
print(find_min_max(numbers= numbers))