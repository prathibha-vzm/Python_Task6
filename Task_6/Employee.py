#Question 2

#Base class
class Employee():
    #construcctor with 2 arguments
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #Method to calculate salary
    def calculate_salary(self):
        #calculating the PF amount
        PF = (12/100)*self.salary

        #calculating the salary
        self.salary-=PF

        #printing
        print(f"Temporary_Employee_Name: {self.name}-Salary:{self.salary}")

#Subcalss with parent
class RegularEmployee(Employee):
    # construcctor with 2 arguments
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    #Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):
        # calculating the PF amount and TAX
        PF = (12/100)*self.salary
        TAX=(5/100)*self.salary

        # calculating the salary
        self.salary=self.salary-PF-TAX

        # printing the answer
        print(f"Regular_Employee_Name: {self.name}-Salary:{self.salary}")

#Subclass with parent
class ContractEmployee(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):

        # calculating the TAX and Adding benefits
        TAX_Deducion=(20/100)*self.salary
        Additional_Benefits=1000

        # calculating the salary
        self.salary=self.salary-TAX_Deducion+Additional_Benefits

        # printing the answer
        print(f"Contractor_Name: {self.name}-Salary:{self.salary}")

#Subclass with parent
class Manager(Employee):
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary

    # Method Overriding(Run-time Polymorphism)
    def calculate_salary(self):

        # calculating the House Rent and PF
        HRS=(40/100)*self.salary
        PF = (12/100)*self.salary

        # calculating the salary
        self.salary=self.salary-PF+HRS

        # printing the answer
        print(f"Manager_Name: {self.name}-Salary:{self.salary}")

#Creating an object for each class and inputing the values
Employee_object=Employee("Dhanya",30000)
RegularEmployee_object=RegularEmployee("Prabha",50000)
ContractEmployee_object=ContractEmployee("Vino",55000)
Manager_object=Manager("Bhavani",400000)

#Using For loop to call the method calculate_salary
for employee in (Employee_object,RegularEmployee_object,ContractEmployee_object,Manager_object):
    employee.calculate_salary()
