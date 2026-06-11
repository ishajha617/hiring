from modules.login import login
from modules.employee import (
    add_employee,
    update_employee,
    delete_employee
)

from modules.report import display_employees
from modules.search import search_employee

from modules.file_handler import (
    save_csv,
    save_json
)

from modules.attendance import (
    mark_attendance,
    view_attendance
)

from modules.salary import salary_report


if login():

    while True:

        print("\n")
        print("=" * 50)
        print(" CYBERYAAN HRMS ")
        print("=" * 50)

        print("1. Add Employee")
        print("2. View Employees")
        print("3. Search Employee")
        print("4. Export CSV")
        print("5. Export JSON")
        print("6. Update Employee")
        print("7. Delete Employee")
        print("8. Mark Attendance")
        print("9. View Attendance")
        print("10. Salary Report")
        print("11. Exit")

        choice = input("Enter Choice : ")

        if choice == "1":

            print(add_employee())

        elif choice == "2":

            display_employees()

        elif choice == "3":

            emp_id = input(
                "Enter Employee ID : "
            )

            print(
                search_employee(
                    0,
                    emp_id
                )
            )

        elif choice == "4":

            save_csv()

        elif choice == "5":

            save_json()

        elif choice == "6":

            emp_id = input(
                "Enter Employee ID : "
            )

            print(
                update_employee(
                    emp_id
                )
            )

        elif choice == "7":

            emp_id = input(
                "Enter Employee ID : "
            )

            print(
                delete_employee(
                    emp_id
                )
            )

        elif choice == "8":

            mark_attendance()

        elif choice == "9":

            view_attendance()

        elif choice == "10":

            salary = float(
                input("Enter Salary : ")
            )

            print(
                "Final Salary :",
                salary_report(salary)
            )

        elif choice == "11":

            print("Thank You")
            break

        else:

            print("Invalid Choice")

else:

    print("Invalid Login")