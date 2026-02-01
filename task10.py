def sort_numbers(numbers: list, reverse: bool = False) -> list:
    result = sorted(numbers, reverse=reverse)
    return result
numbers = [3, 7, 10, -5, -8, 15, 22, 0]
print(sort_numbers(numbers=numbers))
print(sort_numbers(numbers, reverse=True))