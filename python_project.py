import os

FILE_NAME = "students.txt"

# ---------------- FILE HANDLING ---------------- #

def load_students():
    students = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as f:
            for line in f:
                data = line.strip().split("|")
                if len(data) == 5:
                    students.append({
                        "id": data[0],
                        "name": data[1],
                        "branch": data[2],
                        "email": data[3],
                        "score": int(data[4])
                    })
    return students


def save_students(students):
    with open(FILE_NAME, "w") as f:
        for s in students:
            f.write(f"{s['id']}|{s['name']}|{s['branch']}|{s['email']}|{s['score']}\n")


# ---------------- MODULES ---------------- #

def add_student(students):
    print("\n--- Add Student ---")
    sid = input("Enter ID: ")
    name = input("Enter Name: ")
    branch = input("Enter Branch: ")
    email = input("Enter Email: ")

    student = {
        "id": sid,
        "name": name,
        "branch": branch,
        "email": email,
        "score": 0
    }

    students.append(student)
    save_students(students)
    print("Student added successfully!")


def view_students(students):
    print("\n--- Student List ---")
    if not students:
        print("No records found!")
        return

    for s in students:
        print(f"\nID: {s['id']}")
        print(f"Name: {s['name']}")
        print(f"Branch: {s['branch']}")
        print(f"Email: {s['email']}")
        print(f"Security Score: {s['score']}")


def search_student(students):
    key = input("Enter Name or ID to search: ")

    for s in students:
        if s["id"] == key or s["name"].lower() == key.lower():
            print("\nFound Student:")
            print(s)
            return

    print("Student not found!")


def delete_student(students):
    sid = input("Enter Student ID to delete: ")

    for s in students:
        if s["id"] == sid:
            students.remove(s)
            save_students(students)
            print("Student deleted successfully!")
            return

    print("Student not found!")


# ---------------- SECURITY MODULE ---------------- #

def security_assessment(students):
    sid = input("Enter Student ID: ")

    for s in students:
        if s["id"] == sid:
            print("\n--- Security Questions ---")

            mfa = input("MFA Enabled (yes/no): ").lower()
            password = int(input("Password Length: "))
            updated = input("System Updated (yes/no): ").lower()
            antivirus = input("Antivirus Installed (yes/no): ").lower()

            score = 0

            if mfa == "yes":
                score += 25
            if password >= 8:
                score += 25
            if updated == "yes":
                score += 25
            if antivirus == "yes":
                score += 25

            s["score"] = score
            save_students(students)

            print(f"\nSecurity Score: {score}/100")

            if score >= 75:
                print("Status: Good Security")
            elif score >= 50:
                print("Status: Moderate")
            else:
                print("Status: Poor")

            return

    print("Student not found!")


# ---------------- REPORT ---------------- #

def generate_report(students):
    if not students:
        print("No data available!")
        return

    total = len(students)
    total_score = sum(s["score"] for s in students)
    avg = total_score / total

    poor = [s for s in students if s["score"] < 50]

    print("\n--- REPORT ---")
    print(f"Total Students: {total}")
    print(f"Average Score: {avg:.2f}")
    print(f"Students with Poor Security: {len(poor)}")


# ---------------- CYBER FEATURES ---------------- #

def password_checker():
    pwd = input("Enter Password: ")
    if len(pwd) < 6:
        print("Weak Password")
    elif len(pwd) < 10:
        print("Moderate Password")
    else:
        print("Strong Password")


def username_generator():
    name = input("Enter Name: ")
    print("Generated Username:", name.lower() + "123")


def login_validation():
    user = input("Username: ")
    pwd = input("Password: ")

    if user == "admin" and pwd == "1234":
        print("Login Successful")
    else:
        print("Login Failed")


# ---------------- MAIN MENU ---------------- #

def main():
    students = load_students()

    while True:
        print("\n==========================")
        print("Student Security Manager")
        print("==========================")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Security Assessment")
        print("6. Generate Report")
        print("7. Password Checker")
        print("8. Username Generator")
        print("9. Login Validation")
        print("10. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_student(students)
        elif choice == "2":
            view_students(students)
        elif choice == "3":
            search_student(students)
        elif choice == "4":
            delete_student(students)
        elif choice == "5":
            security_assessment(students)
        elif choice == "6":
            generate_report(students)
        elif choice == "7":
            password_checker()
        elif choice == "8":
            username_generator()
        elif choice == "9":
            login_validation()
        elif choice == "10":
            print("Exiting...")
            break
        else:
            print("Invalid choice!")

# Run
main()