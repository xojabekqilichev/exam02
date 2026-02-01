def sort_names(students: list) -> list:

    result = sorted(students, key=lambda x: x[-1])
    return result
students = ["Ali", "Vali", "Hasan", "Husan", "Aziza"]
print(sort_names(students=students))


