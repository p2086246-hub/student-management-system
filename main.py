from student import Student

students = []

def add_student():
    roll = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = float(input("Enter Marks: "))
    students.append(Student(roll, name, marks))
    print("Student Added Successfully!\n")

def view_students():
    if not students:
        print("No students found\n")
    for s in students:
        s.display()

def search_student():
    roll = int(input("Enter Roll No to Search: "))
    for s in students:
        if s.roll == roll:
            s.display()
            return
    print("Student Not Found\n")

while True:
    print("\n1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == '1':
        add_student()
    elif choice == '2':
        view_students()
    elif choice == '3':
        search_student()
    elif choice == '4':
        break
    else:
        print("Invalid choice")
