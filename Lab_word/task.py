#1 Write a function to print "Hello, World!".
def helloworld():
    print("Hello,World!")
helloworld()

#2 Write a function that takes a name and prints a greeting.

def greet():
    name="MCA"
    print("My Name is: ",name)
greet()


#3 Write a function to add two numbers.

def add(no1,no2):
    print("Addition :",no1+no2)
add(10,20)

#4 Write a function to find the square of a number.

def square(no):
    print("Square :",no*no)
square(10)

#5Write a function to check whether a number is even or odd.

def oddeven(no3):
    if(no3%2==0):
        print("Even Number ",no3)
    else:
        print("Odd Number ",no3)
oddeven(10)

#6 Write a function to find the maximum of two numbers.

def max(no4,no5):
    if(no4>no5):
        print("Max ",no4)
    if(no5>no4):
        print("Max ",no5)
max(100,20)


#7 Write a function to convert Celsius to Fahrenheit.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit
print(celsius_to_fahrenheit(25))

#8 Write a function to calculate the area of a circle.

def area_of_circle(radius):
    area = 3.14 * radius * radius
    return area
print(area_of_circle(5))

#9 Write a function to calculate the factorial of a number.

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
print(factorial(5))

#10 Write a function to check whether a number is positive, negative, or zero.
def pnz(no6):
    if(no6>0):
        print("Postivie Number")
    elif(0>no6):
        print("Negetive Number")        
    else:
        print("Zero Number")
pnz(0)


