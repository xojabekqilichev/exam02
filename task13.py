def filter_long_names(students: list, min_length: int = 5) -> list:
    return max(students, key=len)

students = ["Ali", "Vali", "Hasan", "Husan", "Aziza"]
print(filter_long_names(students=students))