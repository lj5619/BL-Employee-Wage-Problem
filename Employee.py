# function to print the salary
import random

def check_attendance():
    return random.randint(0,1)

def daily_wage():
    attendance = check_attendance()
    salary = hours = 0
    if attendance == 1:
        hours = 8
        print('Employee is present')
    else:
        print('Employee is absent')
    salary = hours * 20
    
    print(f'The daily wage of employee is {salary}')

daily_wage()
