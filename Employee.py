
print('This is Employee wage problem')

# Checking employee attendance
import random

def check_attendance():
    attendance = random.randint(0,1)
    if attendance == 0:
        print('Employee is absent')
    else:
        print('Employee is present')

check_attendance()
