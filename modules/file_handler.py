import csv
import json

from modules.employee import employees


def save_csv():

    with open(
        "data/employees.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=[
                "ID",
                "Name",
                "Age",
                "Department",
                "Salary"
            ]
        )

        writer.writeheader()

        writer.writerows(employees)

    print("CSV Saved Successfully")


def save_json():

    with open(
        "data/employees.json",
        "w"
    ) as file:

        json.dump(
            employees,
            file,
            indent=4
        )

    print("JSON Saved Successfully")