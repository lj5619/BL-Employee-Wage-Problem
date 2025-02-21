import random

def check_attendance():
    return random.randint(0,2)

def daily_wage():
    attendance = check_attendance()
    hours = 0
    match attendance:
        case 1:
            hours = 8
        case 2:
            hours = 4
    salary = hours * 20
    return salary, hours

def monthly_wage():
    total_hours = 0
    total_days = 0
    total_salary = 0
    
    while total_hours < 100 and total_days < 20:
        daily_salary, hours = daily_wage()
        total_salary += daily_salary
        total_hours += hours
        total_days += 1
    
    print(f'Total working days: {total_days}')
    print(f'Total working hours: {total_hours}')
    print(f'The total monthly salary of the employee is {total_salary}')
   
monthly_wage()
