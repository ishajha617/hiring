from modules.employee import employees

def display_employees():

    if len(employees) == 0:

        print("\nNo Employee Records Found")
        return

    print("\nEMPLOYEE RECORDS")

    for emp in employees:

        print("-" * 50)

        print("ID :", emp["ID"])
        print("Name :", emp["Name"])
        print("Age :", emp["Age"])
        print("Department :", emp["Department"])
        print("Salary :", emp["Salary"])