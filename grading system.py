def calculate_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

def main():
    num_students = int(input("Enter the number of students: "))
    student_grades = {}

    for i in range(1, num_students + 1):
        student_name = input(f"Enter the name of student {i}: ")
        student_score = float(input(f"Enter the score of {student_name}: "))
        student_grades[student_name] = calculate_grade(student_score)

    print("\nGrading Results:")
    for student, grade in student_grades.items():
        print(f"{student}: {grade}")

if _name_ == "_main_":
    main()