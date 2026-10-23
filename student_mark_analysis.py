# Student Mark Analysis
# This program accepts marks for three subjects, then calculates the total,
# average, and grade for the student.


def calculate_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def analyze_marks(subject_marks):
    total_marks = sum(subject_marks.values())
    average_marks = total_marks / len(subject_marks)
    grade = calculate_grade(average_marks)

    return total_marks, average_marks, grade


if __name__ == "__main__":
    subjects = ["Math", "Science", "English"]
    marks = {}

    print("Student Mark Analysis")
    print("=" * 25)

    for subject in subjects:
        while True:
            try:
                value = float(input(f"Enter marks for {subject}: "))
                if 0 <= value <= 100:
                    marks[subject] = value
                    break
                else:
                    print("Please enter marks between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    total, average, grade = analyze_marks(marks)

    print("\nResults")
    print("-" * 25)
    print(f"Math: {marks['Math']}")
    print(f"Science: {marks['Science']}")
    print(f"English: {marks['English']}")
    print(f"Total Marks: {total}")
    print(f"Average Marks: {average:.2f}")
    print(f"Grade: {grade}")
