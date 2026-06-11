from modules.employee import employees

def search_employee(index, emp_id):

    if index >= len(employees):
        return "Employee Not Found"

    if employees[index]["ID"] == emp_id:
        return employees[index]

    return search_employee(
        index + 1,
        emp_id
    )