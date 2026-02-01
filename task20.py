def find_shortest_name_student(students: list) -> str:
    if not students:
        return ""
    short = students[0]
    for student in students:
        if len(student)< len(short):
            students.append