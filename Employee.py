import random

def check_attendance():
    return random.randint(0,2)

def daily_wage():
    attendance = check_attendance()
    hours = salary = 0
    match attendance:
        case 1:
            hours = 8
            print('Employee is full time and is present today')
        case 2:
            hours = 4
            print('Employee is part time and is present today')
        case _:
            print('Employee is absent today')
    salary = 20 * hours
    print(f'The daily wage of employee is {salary}')
    return salary

def monthly_wage():
    daily_salary = daily_wage()
    monthly_salary = daily_salary * 20
    print(f'The monthly salary of the employee is {monthly_salary}')
   

monthly_wage()
