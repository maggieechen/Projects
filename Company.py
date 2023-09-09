#  File: employee.py
#  Description: This program includes several class constructors to represent a company. Each class returns certain attributes related
# to each constructor.

import sys

class Employee:
    def __init__(self, **kwargs):
        self.name = kwargs.get('name')
        self.id = kwargs.get('id')
        self.salary = kwargs.get('salary')
    def __str__(self):
        return('Name: ' + self.name + 'ID: ' + self.id + 'Salary: ' + self.salary)

############################################################
############################################################
############################################################

class Permanent_Employee :
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.benefits = kwargs.get('benefits')
    
    def cal_salary(self):
        #implement a method called cal_salary() to calculate the actual salary based on selected benefits
        #if benefit = health_insurance, return salary * 0.9
        #if benefit = retirement, return salary * 0.8
        #if benefit = both, return salary * 0.7

        
    def __str__(self):
        return('Name: ' + self.name + 'ID: ' + self.id + 'Salary: ' + self.salary + 'Benefits: ' + self.benefits)

############################################################
############################################################
############################################################

class Manager:
    def cal_salary(self):


    def __str__(self):



############################################################
############################################################
############################################################
class Temporary_Employee :
    def __init__(self, **kwargs):
        self.hours = kwargs.get('hours')
        
    def cal_salary(self):
        self.salary 

    def __str__(self):



############################################################
############################################################
############################################################


class Consultant:


    def cal_salary(self):


    def __str__(self):

############################################################
############################################################
############################################################


class Consultant_Manage:
    def __init__(self,  **kwargs):


    def cal_salary(self):

    def __str__(self):



############################################################
############################################################
############################################################



###### DO NOT CHANGE THE MAIN FUNCTION ########

def main():

    chris = Employee(name="Chris", id="UT1")
    print(chris, "\n")

    emma = Permanent_Employee(name="Emma", id="UT2", salary=100000, benefits=["health_insurance"])
    print(emma, "\n")

    sam = Temporary_Employee(name="Sam", id="UT3", salary=100,  hours=40)
    print(sam, "\n")

    john = Consultant(name="John", id="UT4", salary=100, hours=40, travel=10)
    print(john, "\n")

    charlotte = Manager(name="Charlotte", id="UT5", salary=1000000, bonus=100000)
    print(charlotte, "\n")

    matt = Consultant_Manager(name="Matt", id="UT6", salary=1000, hours=40, travel=4, bonus=10000)
    print(matt, "\n")

    ###################################
    print("Check Salaries")

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")
    emma.benefits = ["retirement", "health_insurance"]

    print("Emma's Salary is:", emma.cal_salary(), "\n")

    print("Sam's Salary is:", sam.cal_salary(), "\n")

    print("John's Salary is:", john.cal_salary(), "\n")

    print("Charlotte's Salary is:", charlotte.cal_salary(), "\n")

    print("Matt's Salary is:",  matt.cal_salary(), "\n")


if __name__ == "__main__":
  main()
