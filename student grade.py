GRADES_FILE = "grades.txt"

def input_grades():
    grades = {}
    subjects = int(input("Enter the number of subjects: "))
    
    for i in range(1, subjects + 1):
        while True:
            try:
                grade = float(input(f"Enter grade for Subject {i}: "))
                if grade < 0 or grade > 100:
                    raise ValueError("Grade must be between 0 and 100.")
                grades[f"Subject {i}"] = grade
                break
            except ValueError as e:
                print("Invalid input. Please enter a numeric value between 0 and 100.")

    return grades

def calculate_average(grades):
    if not grades:
        return 0
    
    total_grades = sum(grades.values())
    return total_grades / len(grades)

def display_average(average):
    print(f"Average grade: {average:.2f}")

def save_grades_to_file(grades):
    with open(GRADES_FILE, 'w') as file:
        for subject, grade in grades.items():
            file.write(f"{subject}: {grade}\n")
    print("Grades saved to file.")

def main():
    try:
        grades = input_grades()
        average = calculate_average(grades)
        display_average(average)
        save_grades_to_file(grades)
    except KeyboardInterrupt:
        print("\nOperation interrupted.")
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
