number_of_students = int(input())

students = {}

for i in range(number_of_students):
    student_name = input()
    grade = float(input())

    if student_name not in students:
        students[student_name] = []
    students[student_name].append(grade)

passed_students = {}
for key in students:
    average = sum(students[key]) / len(students[key])
    if average >= 4.5:
        passed_students[key] = average

for key, value in passed_students.items():
    print(f"{key} -> {value:.2f}")