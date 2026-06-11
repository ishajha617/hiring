attendance = {}

def mark_attendance():

    emp_id = input("Enter Employee ID : ")

    status = input(
        "Enter Status (Present/Absent/Half Day) : "
    )

    attendance[emp_id] = status

    print("Attendance Marked Successfully")


def view_attendance():

    if len(attendance) == 0:

        print("No Attendance Records Found")
        return

    print("\nATTENDANCE RECORDS")

    for emp_id, status in attendance.items():

        print("-" * 40)

        print("Employee ID :", emp_id)
        print("Status :", status)