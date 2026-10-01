class operation:

    def add(self):
        data1=int(input("Enter The First Value :"))
        data2=int(input("Enter The Seconde Value :"))
        print("Addition is :",data1+data2)
    def sub(self):
        data1=int(input("Enter The First Value :"))
        data2=int(input("Enter The Seconde Value :"))
        print("Substraction is :",data1-data2)
    def mul(self):
        data1=int(input("Enter The First Value :"))
        data2=int(input("Enter The Seconde Value :"))
        print("Multiplication is :",data*data2)
    def div(self):
        data1=int(input("Enter The First Value :"))
        data2=int(input("Enter The Seconde Value :"))
        print("Divsion is :",data1/data2)
    def sq(self):
        data1=int(input("Enter The First Value :"))
        print("Square is :",data1*data1)
    def cb(self):
        data1=int(input("Enter The Value :"))
        print("Cube is :",data1*data1*data1)
    def sqrt(self):
        data1=int(input("Enter The Value :"))
        print("Square Root is :",data1**0.5)
ob=operation();
print("1.Addiition\n2.Substraction\n3.Multiplication\n4.Divsion\n5.Square\n6.Cube\n7.Square Root")
ch=int(input("Enter The Your Choice"))
match(ch):
    case 1:
        ob.add()
    case 2:
        ob.sub()
    case 3:
        ob.mul()
    case 4:
        ob.div()
    case 5:
        ob.sq()
    case 6:
        ob.cb()
    case 7:
        ob.sqrt() 
    case _:
        print("Invalid Choice")
    
