#Simple Calculator
#define the functions of operations
#addition of 2 numbers
def add(x,y):
    return (x+y)
#subtraction of 2 numbers
def subtract(x,y):
    return(x-y)
#multiplication of 2 numbers
def multiply(x,y):
    return(x*y)
#division of 2 numbers
def divide(x,y):
    return(x/y)
print("Select Operation")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
#take input from the user
choice = input("select operation:1 , 2 , 3 , 4")
#prompt the user to input 2 numbers
a = float(input("Enter the first number:"))
b = float(input("Enter the second number:"))
if choice == "1":
    print(a,"+",b,"=",add(a,b))
elif choice == "2":
    print(a,"-",b,"=",subtract(a,b))    
elif choice == "3" :
    print(a,"*",b,"=",multiply(a,b))
elif choice == "4":
    print(a,"/",b,"=",divide(a,b))   
else:
    print("Invalid Choice")    
       
