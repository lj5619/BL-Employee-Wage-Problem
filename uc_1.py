# Checking employee attendance
import random

def check_attendance():
    attendance = random.randint(0,2)
    if attendance == 0:
        print('Employee is absent')
    else:
        print('Employee is present')

check_attendance()