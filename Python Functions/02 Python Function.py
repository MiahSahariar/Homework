# input() is a function which allows for user input

empName = input("Employee Name: ")
empID = input("Employee Salary: ")
empSalary = (input("Employee Salary: "))
fullTimeEmployee = input("Full Time Employee? Ans:")

print("------------------------")
def empInfo(empName, empID, empSalary, fullTimeEmployee):
    x = f"Employee Name: {empName.upper()} \nEmployee ID: {empID} \nEmployee Salary: {empSalary:,.4f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)

# We define the variables when the function is called
def empInfo():
    print(empName)
    print(empID)
    print(empSalary)
    print(fullTimeEmployee)
    

empInfo()

num1 = 23
num2 = 32

def numFunction():
    print(num1+num2)
    
numFunction()

num3 = input("Number 3: ")
num4 = input("Number 4: ")

def addition():
    print(num3+num4)

addition()

# We have to use type casting
num5 = int(input("Number 5: "))
num6 = int(input("Number 6: "))

def sum():
    print(num5+num6)
    
sum()

