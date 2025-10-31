import os
import json

STUDENTS_FILE = "students.json"

# ---------- LOAD STUDENTS ----------
def load_students():
    """Loads student data from file safely."""
    try:
        if os.path.exists(STUDENTS_FILE):
            with open(STUDENTS_FILE, "r") as file:
                return json.load(file)
        else:
            return []
    except json.JSONDecodeError:
        print("Error: JSON file corrupted. Starting fresh.")
        return []
    except Exception as e:
        print(f"Unexpected error while loading data: {e}")
        return []

# ---------- SAVE STUDENTS ----------
def save_students(students):
    """Saves student data safely to file."""
    try:
        with open(STUDENTS_FILE, "w") as file:
            json.dump(students, file, indent=4)
    except Exception as e:
        print(f"Error saving file: {e}")

# ---------- ADD STUDENT ----------
def add_student(students):
    try:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        course = input("Enter student course: ")

        if not name or not age or not course:
            print("All fields are required!")
            return

        # Optional: verify age is a number
        if not age.isdigit():
            print("Age must be a number.")
            return

        student = {"name": name, "age": int(age), "course": course}
        students.append(student)
        save_students(students)
        print("Student added successfully.")
    except Exception as e:
        print(f"Unexpected error adding student: {e}")

# ---------- VIEW STUDENTS ----------
def view_students(students):
    try:
        if not students:
            print("No students found.")
            return
        print("\n--- Student List ---")
        for i, s in enumerate(students, start=1):
            print(f"{i}. {s['name']} | Age: {s['age']} | Course: {s['course']}")
    except KeyError as e:
        print(f"Missing data field: {e}")
    except Exception as e:
        print(f"Unexpected error viewing students: {e}")

# ---------- SEARCH STUDENT ----------
def search_student(students):
    try:
        name = input("Enter name to search: ").lower()
        for s in students:
            if s["name"].lower() == name:
                print(f"Found: {s['name']} | Age: {s['age']} | Course: {s['course']}")
                return
        print("Student not found.")
    except Exception as e:
        print(f"Error searching student: {e}")

# ---------- REMOVE STUDENT ----------
def remove_student(students):
    try:
        name = input("Enter name to remove: ").lower()
        new_list = [s for s in students if s["name"].lower() != name]

        if len(new_list) < len(students):
            save_students(new_list)
            print("Student removed successfully!")
        else:
            print("No such student found.")
        return new_list
    except Exception as e:
        print(f"Error removing student: {e}")
        return students

# ---------- SUMMARY ----------
def show_summary(students):
    try:
        if not students:
            print("No data available.")
            return
        courses = {s["course"] for s in students}
        names = tuple(s["name"] for s in students)
        print("Unique Courses:", courses)
        print("All Names:", names)
    except KeyError as e:
        print(f"Missing data field: {e}")
    except Exception as e:
        print(f"Error showing summary: {e}")

# ---------- MAIN ----------
def main():
    while True:
        students = load_students()

        print("\n========== STUDENT MANAGEMENT ==========")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Remove Student")
        print("5. Summary")
        print("6. Exit")

        try:
            choice = input("Enter your choice: ")

            if choice == "1":
                add_student(students)
            elif choice == "2":
                view_students(students)
            elif choice == "3":
                search_student(students)
            elif choice == "4":
                students = remove_student(students)
            elif choice == "5":
                show_summary(students)
            elif choice == "6":
                print("👋 Exiting...")
                break
            else:
                print("Invalid choice. Try again.")
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting safely...")
            break
        except Exception as e:
            print(f"Unexpected error in menu: {e}")

if __name__ == "__main__":
    main()
