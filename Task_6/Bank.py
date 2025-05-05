#Question 1

#Base Class
class BankAccount:
    def __init__(self): #constuctor
        print("Enter your Account Number:")

        #getting input as integer
        self.accountnumber=int(input())

        #declaring balance with minimum balance
        self.balance=500

    #Method Deposit
    def deposit(self):
        print("Enter the Amount to deposit")
        deposit=int(input())

        #adding the deposit amount to the balance
        self.balance+=deposit

    #Method Withdraw
    def withdraw(self):
        print("Enter the Amount to withdraw")
        withdraw= int(input())

        #subtracting the withdrawal amount from balance
        self.balance -= withdraw

        #Checking for minimum balance
        if withdraw>self.balance:
              print("Insufficient Balance")
              #restricting to withdraw the amount
              self.balance+=withdraw
        elif self.balance<500:
              print("Maintain Sufficient balance")
        else:
              self.balance-=withdraw


class SavingsAccount(BankAccount):
    #constructor
    def __init__(self):
        super().__init__()

        #Getting loan amount
        print("Enter the Loan Amount")
        self.loan=int(input())

        #getting time period for loan
        print("Choose the number of years to pay the loan\n1\t5\t10")
        self.interest_time=int(input())

        #calaculating the interest rate according the time
        if self.interest_time==1:
            self.interest_rate=(2/100)*self.loan
        elif self.interest_time==5:
            self.interest_rate=(3/100)*self.loan
        elif self.interest_time==10:
            self.interest_rate=(5/100)*self.loan

    #Method to calculate interest
    def calculate_interest(self):
        # calculating the interest rate
        self.interest_rate=(self.loan*self.interest_rate*self.interest_time)/100

        print("Interest Rate for 5 years",self.interest_rate)

#subcalss with parent BankAccount class
class CurrentAccount(BankAccount):
    def __init__(self):
        super().__init__()
        self.minimum_balance=500#declaring the minimum balance value

    #Private method to chcek balance(encapsulation)
    def __check_balance(self):
        #Printing the balance
        print("Account Balance :",self.balance)

        #if the balance is less than minimum balance then this statement will execute
        if self.balance <self.minimum_balance:
            print("Maintain Minimum Balance")

    #method to do actions according to the input
    def action(self):
        print("Choose the operation")

        while True:
            print("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Interest Rate\n5. Exit")
            option=int(input())

            #Execute the methods according to the input
            if option==1:
                # calling the method from parent class
                self.deposit()
            elif option==2:
                # calling the method from parent class
                self.withdraw()
            elif option==3:
                #since it is private class(encapsulation) calling it using the object name
                CurrentAccount_object.__check_balance()
            elif option==4:
                #this calculate interest is a method from another subclass
                #creating the object for the class and calling here
                SavingsAccount_object = SavingsAccount()
                SavingsAccount_object.calculate_interest()
            elif option==5:
                #to exit
                break
            else:
                print("Please Enter Valid option")


#crating object for the subclass and calling action method
CurrentAccount_object=CurrentAccount()
CurrentAccount_object.action()

