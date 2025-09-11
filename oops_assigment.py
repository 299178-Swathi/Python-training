# Q1) Write a Python program to implement the following:
# Class: Person
# Attributes: Age, Name, Gender, Address
# Methods:
# Constructor to initialize attributes
# Display() to print details

class Person:
    def __init__(self,Name,Age,Gender,Address):
        self.name=Name
        self.age=Age
        self.gender=Gender
        self.address=Address
    def display(self):
        print('Name:',self.name)
        print('Age:',self.age)
        print('Gender:',self.gender)
        print('Address:',self.address)

#Class: Student (inherits from Person)Attributes: Roll, Marks, CollegeMethods:
#Constructor to initialize both Person and Student attributesDisplay() to print all details
class Student(Person):
    def __init__(self,Name,Age,Gender,Address,Roll,Marks,College):
        Person.__init__(self,Name,Age,Gender,Address)
        self.roll=Roll
        self.marks=Marks
        self.college=College
    def display(self):
        print('\n----Student Details----')
        Person.display(self)
        print('RollNo:',self.roll)
        print('Marks:',self.marks)
        print('CollegeName:',self.college)

# Class: Intern (inherits from Person)Attributes: InternId, Company, Duration
# Methods:Constructor to initialize both Person and Intern attributes
# Display() to print all details

class Intern(Person):
    def __init__(self,Name,Age,Gender,Address,InternId,Company,Duration):
        Person.__init__(self,Name, Age, Gender, Address)
        self.internid=InternId
        self.company=Company
        self.duration=Duration
    def display(self):
        print('\n----Intern Details----')
        Person.display(self)
        print('InterId:',self.internid)
        print('Company:',self.company)
        print('Duration:',self.duration)

# Class: Employee (inherits from Student and Intern)Represents a diamond inheritance problem.Attributes: EmpId, Salary
# Methods:Constructor to initialize attributes of all parent classes (Person, Student, Intern) and Employee.
# Display() to print complete details (Person + Student + Intern + Employee).

class Employee(Student,Intern):
    def __init__(self,Name,Age,Gender,Address,Roll,Marks,College,Internid,Company,Duration,
                 EmployeeId,Salary):
        Student.__init__(self,Name,Age,Gender,Address,Roll,Marks,College)
        Intern.__init__(self,Name,Age,Gender,Address,Internid,Company,Duration)
        self.employeeid=EmployeeId
        self.salary=Salary
    def display(self):
        print('\n----Employee Details----')
        Person.display(self)
        print('RollNo:', self.roll)
        print('Marks:', self.marks)
        print('CollegeName:', self.college)
        print('Internid:',self.internid)
        print('Company:',self.company)
        print('Duration:',self.duration)
        print('EmployeeId:',self.employeeid)
        print('Salary:',self.salary)
        print('---------------------')

p1=Person('Sita',21,'Female','Bangalore')
s1=Student('Zayn',23,'Male','Bangalore',24,78.9,'CMR')
i1=Intern('Abhinav',25,'Male','Bangalore',26145,'UST','6 Months')
e1=Employee('Swathi',30,'Female','Bangalore',23,72.3,'WPT',2673,
            'UST','6 Months',21143,35000)
p1.display()
s1.display()
i1.display()
e1.display()

# Q2) Create a Python program to demonstrate polymorphism using the following classes:
# Class: Account
# Method: interest_rate() → (no implementation, just a placeholder).
# Class: SavingsAccount (inherits from Account)
# Method: interest_rate() → prints "Savings Account Interest Rate: 4%".
# Class: CurrentAccount (inherits from Account)
# Method: interest_rate() → prints "Current Account Interest Rate: 0%".
# Class: FixedDeposit (inherits from Account)
# Method: interest_rate() → prints "Fixed Deposit Interest Rate: 7%".
# Create a function show_interest(account_obj) that accepts an Account object and calls its interest_rate() method.
# Pass objects of SavingsAccount, CurrentAccount, and FixedDeposit to demonstrate polymorphism.
class Account:
    def Interest(self):
        pass
class SavingAccount(Account):
    def Interest(self):
        print("Savings Account Interest Rate: 4%")
class CurrentAccount(Account):
    def Interest(self):
        print("Current Account Interest Rate:0%")
class FixedDeposite(Account):
    def Interest(self):
        print("Fixed Deposite Interest Rate: 7%")
def Show_Interest(Account_obj):
    Account_obj.interest()
savings=SavingAccount()
savings.Interest()
current=CurrentAccount()
current.Interest()
fixed=FixedDeposite()
fixed.Interest()

# Q3) Write a Python program to implement encapsulation using the following:
# Class: BankAccount
# Private Attributes:
# __account_number
# __balance
# Public Methods:
# Constructor to initialize account number and balance.
# deposit(amount) → increases balance.
# withdraw(amount) → decreases balance if sufficient funds exist.
# get_balance() → returns current balance.
# get_account_number() → safely access account number.
class Bank_Account:
    def __init__(self,AccountNo,Balance):
        self.__accountNo = AccountNo
        self.__balance = Balance
    def Deposit(self,amount):
        self.__balance += amount
        print("Deposit Successful")
    def withdraw(self,amount):
        self.__balance -= amount
        print("Withdraw Successful")
    def get_balance(self):
        return self.__balance
    def get_accountNo(self):
        return self.__accountNo
account=Bank_Account(22164231,50000)
account.Deposit(50000)
account.withdraw(10000)

accountNo=getattr(account,"get_accountNo")()
balance=getattr(account,"get_balance")()
print(accountNo)
print(balance)

# Q4) Write a Python program to implement abstraction using the following:
# Abstract Class: Shape (use ABC from abc module)
# Abstract Methods:
# area() → calculates the area of the shape
# perimeter() → calculates the perimeter of the shape
# Class: Circle (inherits from Shape)
# Attribute: radius
# Implements area() → returns π × radius²
# Implements perimeter() → returns 2 × π × radius
# Class: Rectangle (inherits from Shape)
# Attributes: length, width
# Implements area() → returns length × width
# Implements perimeter() → returns 2 × (length + width)
# Create objects of Circle, Rectangle and print their area and perimeter.


from abc import ABC,abstractmethod
class shape:
    def __init__(self):
        print("this is shape constructor")
    @abstractmethod
    def area(self):
        pass
    def perimeter(self):
        pass
class circle(shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * (self.radius ** 2)
    def perimeter(self):
        return 3.14 * 2 * self.radius
class rectangle(shape):
    def __init__(self, length, width):
        # shape().__init__()
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width
    def perimeter(self):
        return 2 * (self.length + self.width)

c=circle(6)
print("area of the circle:",c.area())
print("perimeter of the circle:",c.perimeter())
r=rectangle(5,6)
print("area of the rectangle:",r.area())
print("perimeter of the rectangle:",r.perimeter())
