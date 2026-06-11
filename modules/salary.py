bonus = lambda salary: salary * 0.10

def salary_report(salary):

    tax = salary * 0.05

    bonus_amount = bonus(salary)

    final_salary = salary - tax + bonus_amount

    return final_salary