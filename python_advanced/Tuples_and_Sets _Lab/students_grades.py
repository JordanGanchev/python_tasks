def avf(values):
    return sum(values) / len(values)

# n = 7
# student_strings = [
#         'Peter 5.20',
#          'Mark 5.50',
#          'Peter 3.20',
#          'Mark 2.50',
#          'Alex 2.00',
#          'Mark 3.46',
#          'Alex 3.00',
# ]

n = int(input())
students_strings = [input() for _ in range(n)]
student_grades = {}

for student_string in students_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in student_grades:
        student_grades[student] = []
    student_grades[student].append(grade)

for student, grades in student_grades.items():
    grades_avg = avf(grades)
    grades_formatted = ' '. join(f'{grade:.2f}' for grade in grades)
    grades_avg_formatted = f'{grades_avg:.2f}'
    print(f'{student} -> {grades_formatted} (avg: {grades_avg_formatted})')