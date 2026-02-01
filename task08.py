def calculate_stats(numbers: list) -> dict:
    if not numbers:
        print("error")
    
    son = {}
    sum_num = sum(numbers)
    average = sum_num/len(numbers)

    son['sum'] = sum_num
    son['average'] = average
    return son

numbers = [3, 7, 10, -5, -8, 15, 22]
print(calculate_stats(numbers=numbers))