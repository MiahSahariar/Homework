# print() is a function that came from Python Library
# len() is to know the length of string
# type()
print("Hello!")
print(len("Hello!"))

# User define function
def myFunction():
    print("This is my first Function")
    
myFunction()

empName = "James John"
empID = 352
empSalary = 456753.45
fullTimeEmployee = True


def empInfo():
    print(empName)
    print(empSalary)
    print(empID)
    print(fullTimeEmployee)
empInfo()

# another way
def empInfo():
    x = f"Employee Name: {empName.upper()}, Employee ID: {empID}, Employee Salary: {empSalary:,.2f} \nFull Time Employee: {fullTimeEmployee}"
    print(x)
    
empInfo()