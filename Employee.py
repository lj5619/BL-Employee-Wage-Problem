import random

def check_attendance():
    return random.randint(0,2)

def daily_wage():

    attendance = check_attendance()
    salary = hours = 0
    if attendance == 1:
        hours = 8
        print('Employee is full time and is present today')
    elif attendance == 2:
        hours = 4
        print('Employee is part time and is present today')
    else:
        print('Employee is absent ')
    salary = hours * 20

    
    print(f'The daily wage of employee is {salary}')

daily_wage()

