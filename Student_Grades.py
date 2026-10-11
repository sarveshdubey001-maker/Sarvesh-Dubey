# Step 1: Create an initial dictionary
students = {
    "Amit": "A",
    "Riya": "B",
    "Karan": "C"
}

while True:
    print("\n--- Student Grades Menu ---")
    print("1. Add a new student")
    print("2. Update a student's grade")
    print("3. Print all student grades")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    # Step 2: Add a new student
    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        if name in students:
            print(f"{name} already exists.")
        else:
            students[name] = grade
            print(f"{name} added with grade {grade}.")

    # Step 3: Update an existing student's grade
    elif choice == "2":
        name = input("Enter student name to update: ")
        if name in students:
            grade = input("Enter new grade: ")
            students[name] = grade
            print(f"{name}'s grade updated to {grade}.")
        else:
            print(f"{name} not found.")

    # Step 4: Print all student grades
    elif choice == "3":
        print("\n--- All Student Grades ---")
        for name, grade in students.items():
            print(f"{name}: {grade}")

    # Step 5: Exit
    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please try again.")