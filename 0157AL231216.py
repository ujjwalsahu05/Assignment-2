"""                                             NOTE       
                                        Name : Ujjwal Sahu
                                        Enrollment : 0157AL231216 
                                        Year : 3RD  Section : c
                                        BATCH - 5 (MTF) - 10:30 AM
                                        COLLEGE :  LNCTS - AIML
                                    



"""

    
students = []

current_student = None
is_logged_in = False

def register():
    print("\n--- Student Registration ---")
    username = input(" Enter the Username: ")
    for student in students:
        if student['username'] == username:
            print("Username already exists. Please choose a different one.")
            return
    password = input("Enter the Password: ")
    name = input("Enter the Full Name: ")
    roll_no = input("Enter your Roll No: ")
    email = input("Enter your Email: ")
    phone = input("Enter your Phone No. : ")
    address = input("Enter your Address: ")
    dob = input("DOB (DD-MM-YYYY): ")
    gender = input("Enter your Gender (M/F): ")
    department = input("Enter your Department: ")
    year = input("Enter Year: ")

    student_profile = {
        'username': username,
        'password': password,
        'name': name,
        'roll_no': roll_no,
        'email': email,
        'phone': phone,
        'address': address,
        'dob': dob,
        'gender': gender,
        'department': department,
        'year': year
    }

    students.append(student_profile)
    print("Registration successful!")

def login():
    global current_student, is_logged_in
    print("\n--- Login ---")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    for student in students:
        if student['username'] == username and student['password'] == password:
            current_student = student
            is_logged_in = True
            print("Login successful!")
            return
    print("Invalid credentials. Please try again.")

def show_profile():
    if is_logged_in and current_student:
        print("\n--- Student Profile ---")
        for key, value in current_student.items():
            print(f"{key.capitalize()}: {value}")
    else:
        print("Please login first.")

def update_profile():
    if is_logged_in and current_student:
        print("\n--- Update Profile ---")
        for key in ['name', 'roll_no', 'email', 'phone', 'address', 'dob', 'gender', 'department', 'year']:
            new_value = input(f"Update {key.replace('_', ' ').title()} (current: {current_student[key]}): ")
            if new_value.strip():
                current_student[key] = new_value
        print("Profile updated successfully!")
    else:
        print("Please login first.")

def logout():
    global current_student, is_logged_in
    if is_logged_in:
        is_logged_in = False
        current_student = None
        print("Logout successful.")
    else:
        print("No user is currently logged in.")


def main():
    registration_done = False
    while True:
        if not registration_done:
            print("\n1. Register\n2. Exit")
            choice = input("Enter your choice: ")
            if choice == '1':
                register()
                registration_done = True
            elif choice == '2':
                print("Exiting system. Goodbye!")
                break
            else:
                print("Invalid choice.")
        else:
            if not is_logged_in:
                print("\n1. Login\n2. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    login()
                elif choice == '2':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid choice.")
            else:
                print("\n1. Show Profile\n2. Update Profile\n3. Logout\n4. Exit")
                choice = input("Enter your choice: ")
                if choice == '1':
                    show_profile()
                elif choice == '2':
                    update_profile()
                elif choice == '3':
                    logout()
                elif choice == '4':
                    print("Exiting system. Goodbye!")
                    break
                else:
                    print("Invalid choice.")

if __name__ == "__main__":
    main()


