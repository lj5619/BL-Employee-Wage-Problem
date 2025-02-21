
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
        
    salary = hours * 20
    monthly_salary = salary * 20
    print(f'The daily wage of employee is {salary}')
    print(f'The monthly wage of the employee is {monthly_salary}')

daily_wage()

