#1 program to compute area and perimeter of circle.
'''a=int(input("enter radious::"))
def AreaAndPer(r):
     area=3.14*r*r
     perimeter=2*3.14*r
     print("area of circle is",area,)
     print("and perimeter of circle is",perimeter)
AreaAndPer(a)


# 2program to compute simple interest and amount
r=float(input("enter the interest rate:"))
p=float(input("enter principle amount:"))
t=float(input("enter time in year:"))
def SI(r,p,t):
     SimIn=(p*t*r)/100
     amt=SimIn+p
     print("simple interest is:",SimIn,"and amount is:",amt)
SI(r,p,t)

#3 program that reada an integer between 1 and 12 and prints the month 
#of the year in english using math case statement.
def get_month():
        month_number = int(input("Enter an integer between 1 and 12: "))

        match month_number:
            case 1:
                print("January")
            case 2:
                print("February")
            case 3:
                print("March")
            case 4:
                print("April")
            case 5:
                print("May")
            case 6:
                print("June")
            case 7:
                print("July")
            case 8:
                print("August")
            case 9:
                print("September")
            case 10:
                print("October")
            case 11:
                print("November")
            case 12:
                print("December")
            case _:
                print("Invalid input. Please enter a number between 1 and 12.")
    
# Call the function
get_month()


#4 program to compute specific days into year week and day.
def ywd(total_days):
     years = total_days//365
     Reamining_days=total_days % 365
     weeks = Reamining_days // 7
     days = Reamining_days % 7
     return years,weeks, days
total_days = int(input("Enter the number of days: "))
years, weeks, days = ywd(total_days)
print(f"{total_days} days is equal to {years} years, {weeks} weeks and {days} days.")

#5 program that convert specific second into hours minutes and second.

#6 program to convert the tempeture in celsius to fahrenheit
def cTOf(c):
     fr= (c * 9/5) + 32
     return fr
c = float(input("Enter the temperature in Celsius: "))
fr= cTOf(c)
print(f"{c} degrees Celsius is equal to {fr} degrees Fahrenheit.")

#7 program to find given number is plaindrom or not.

def palindrome(n):
     temp = n
     reverse = 0
    
     while temp > 0:
         digit = temp % 10
         reverse = reverse * 10 + digit
         temp //= 10
     return n== reverse
n= int(input("Enter a number: "))
if palindrome(n):  
     print(n,"is a palindrome.")
else:
     print(n,"is not a palindrome.")

#8 program to find factorial of a number
def factt(n):
     if ( n==1 or n==0):
         return 1
     else:
         return n * factt(n-1)
n=int(input("enter a number: "))
result=factt(n)
print("the factorial of given number is::",result)

#9 program to find fbboniccii series.
def fib(i):
  
     if i<=1:
         return 1
     else:
         return (fib(i-1)+fib(i-2))
num=int(input("enter a range upto you want to display fabbbonicciL::"))
for i in range(num):
     print(fib(i))

#10 write a program to access each character of string in forward abd backward
#direction by by using while loop(indexing and slicing ).

def access_indexing(s):
     print("\nForward direction Indexing:")
     i = 0
     while i < len(s):
         print(s[i],end='')
         i += 1
     print("\nBackward direction Indexing:")
     i = len(s) - 1
     while i >= 0:
         print(s[i],end='')
         i -= 1
def access_slicing(s):
     print("\nForward direction Slicing:")
     i = 0
     while i < len(s):
         print(s[i:i+1],end='')
         i += 1
     print("\nBackward direction (Slicing):")
     i = len(s) - 1
     while i >= 0:
         print(s[i:i-1],end='')
s=str(input("enter a string:"))
access_indexing(s)
access_slicing(s)

#11 writw a program to find all prime number from 1 to 100 

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Prime numbers from 1 to 100 are:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")


# 16 Create a class called "BankAccount" that has two attributes:"balance" and"account_number". 
# The class should have methods called "deposit" and "withdraw" that allow a user to deposit 
# or withdraw money from the account.the balance should be updated accordingly.

class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance+amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")

account = BankAccount("12345678")
amt=int(input("enter a amount for deposit:"))
account.deposit(amt)
cash=int(input("enter a amount for withdraw:"))
account.withdraw(cash)

#19 wap to handle multiple exception when reading a file and converting its 
# content to an integer.
def fileRead(filename):
    try:
        # Attempt to open the file
        with open(filename, 'r') as file:
            content = file.read()
        
        # Attempt to convert the content to an integer
        number = int(content)
        
        print(f"The number in the file is: {number}")
        
    except FileNotFoundError:
        print("Error: The file was not found.")
        
    except PermissionError:
        print("Error: You do not have permission to read the file.")
        
    except ValueError:
        print("Error: The content of the file is not a valid integer.")
    except Exception as e:
        # Generic exception handler for any other exceptions
        print(f"An unexpected error occurred: {e}")
    finally:
        print("execution completed.")
        
filename = input("enter the file name::")
fileRead(filename)   
'''
#18 create a class savingAccount that inherets from bankaccount 
# and ADD an interest rate
class BankAccount:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance = self.balance+amount
            print(f"Deposited {amount}. New balance: {self.balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance = self.balance - amount
                print(f"Withdrew {amount}. New balance: {self.balance}")
            else:
                print("Insufficient funds.")
        else:
            print("Withdrawal amount must be positive.")
class SavingAcount(BankAccount):  
    def __init__(self,account_number, balance,time,rate):
        super().__init__(account_number, balance)
        self.rate=rate
        self.time=time
    def Interest(self):
        interest=(self.balance*self.time*self.rate)/100
        amount=interest+self.balance
        print("the total amount after interest is::",amount)
          

account = BankAccount("12345678")
amt=int(input("enter a amount for deposit:"))
account.deposit(amt)
cash=int(input("enter a amount for withdraw:"))
account.withdraw(cash)
T=int(input("enter time:"))
R=int(input("enter rate:"))
sa=SavingAcount(account.account_number,account.balance,T,R)
sa.Interest()



