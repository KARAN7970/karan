#first challenge

class Point:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        return self.x**2 + self.y**2 + self.z**2


point = Point(1, 3, 5)


sum_of_squares = point.sqSum()
print(sum_of_squares)  


#second challenge

class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num2 - self.num1

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num1 != 0:
            return self.num2 / self.num1
        else:
            raise ValueError("Division by zero is not allowed")


obj = Calculator(10, 94)


print(obj.add())       
print(obj.subtract())  
print(obj.multiply())  
print(obj.divide())   



# challenge - 3


class Student:

    def __init__(self):
        self.__name = None
        self.__rollNumber = None

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setRollNumber(self, rollNumber):
        self.__rollNumber = rollNumber

    def getRollNumber(self):
        return self.__rollNumber


student = Student()


student.setName("John Doe")
student.setRollNumber(12345)


print(student.getName())        
print(student.getRollNumber())  


#challenge - 4

class Account:
    def __init__(self, title=None, balance=0):
        self.title = title
        self.balance = balance
    
    def withdrawal(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient balance")

    def deposit(self, amount):
        self.balance += amount

    def getBalance(self):
        return self.balance

class SavingsAccount(Account):
    def __init__(self, title=None, balance=0, interestRate=0):
        super().__init__(title, balance)
        self.interestRate = interestRate
    
    def interestAmount(self):
        return (self.balance * self.interestRate) / 100


demo1 = SavingsAccount("Ashish", 2000, 5)
demo1.deposit(500)
print(demo1.getBalance())     
print(demo1.getBalance())     
print(demo1.interestAmount()) 



