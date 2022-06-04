from my_classes.school import School

school = School('Ridgemont High')

while True:
    mode = input(
        "\nWhat would you like to do?\nOptions:\n1. List All Students\n2. View Individual Student <student_id>\n3. Add "
        "a Student\n4. Remove a Student <student_id>\n5. Quit\n")
    if mode == "1":
        school.list_students()
    if mode == "2":
        student_id = input('Enter student id:\n')
        school.find_student_by_id(student_id)
    if mode == "3":
        pass
    if mode == "4":
        pass
    if mode == "5":
        print("Logging out...\n")
        exit()
