import random

class Employee:
    hourly_wage = 20
    max_hours = 100
    max_days = 20

    def check_attendance(self):
        """
        Description: 
            Function to check attendance
        Parameters: 
            self
        Return: 
            Random integer between 0 and 2
        """
        return random.randint(0,2)

    def daily_wage(self):
        """
        Description: 
            Function to calculate daily wage
        Parameters: 
            self
        Return: 
            salary, hours
        """
        attendance = self.check_attendance()
        hours = 0
        match attendance:
            case 1:
                hours = 8
            case 2:
                hours = 4
        salary = hours * Employee.hourly_wage
        return salary, hours

    def monthly_wage(self):
        """
        Description: 
            Function to calculate monthly wage
        Parameters: 
            self
        Return: 
            None
        """
        total_hours = 0
        total_days = 0
        total_salary = 0
        
        while total_hours < Employee.max_hours and total_days < Employee.max_days:
            daily_salary, hours = self.daily_wage()
            total_salary += daily_salary
            total_hours += hours
            total_days += 1
        
        print(f'Total working days: {total_days}')
        print(f'Total working hours: {total_hours}')
        print(f'The total monthly salary of the employee is {total_salary}')

if __name__ == "__main__":
    emp1= Employee()
    emp1.monthly_wage()
