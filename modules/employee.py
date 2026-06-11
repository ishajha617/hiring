employees = []

def add_employee():

    try:

        emp_id = input("Enter Employee ID : ")
        name = input("Enter Name : ")
        age = int(input("Enter Age : "))
        department = input("Enter Department : ")
        salary = float(input("Enter Salary : "))

        employee = {
            "ID": emp_id,
            "Name": name,
            "Age": age,
            "Department": department,
            "Salary": salary
        }

        employees.append(employee)

        return "Employee Added Successfully"

    except ValueError:

        return "Invalid Input"


def update_employee(emp_id):

    for emp in employees:

        if emp["ID"] == emp_id:

            emp["Name"] = input("New Name : ")
            emp["Age"] = int(input("New Age : "))
            emp["Department"] = input("New Department : ")
            emp["Salary"] = float(input("New Salary : "))

            return "Employee Updated Successfully"

    return "Employee Not Found"


def delete_employee(emp_id):

    for emp in employees:

        if emp["ID"] == emp_id:

            employees.remove(emp)

            return "Employee Deleted Successfully"

    return "Employee Not Found"