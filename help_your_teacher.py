from dataclasses import dataclass

@dataclass
class Student:
    name: str
    english: float
    math: float


def get_grade(subject):
    while True:
        try:
            grade = float(input(f"Enter grade for {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("Grade must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric grade.")


def get_student_info():
    name = input("Enter student's name: ")
    english = get_grade("English")
    math = get_grade("Math")
    return Student(name, english, math)


def print_student_info(students):
    print("\nStudent Summary:\n" + "-" * 20)
    for student in students:
        grades = [student.english, student.math]
        best = max(grades)
        average = sum(grades) / len(grades)

        print(
            f"Name: {student.name}\n"
            f"Best Grade: {best}\n"
            f"Average Grade: {average:.2f}\n"
            + "-" * 20
        )


def main():
    while True:
        try:
            count = int(input("Enter number of students: "))
            if count > 0:
                break
            print("Please enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    students = [get_student_info() for _ in range(count)]
    print_student_info(students)


if __name__ == "__main__":
    main()
