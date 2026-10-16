class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None
    def insert_begin(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        print("Insert into Begins")

    def insert_last(self,data):
        new_node=Node(data)

        if self.head is None:
            self.head=new_node
            return
        temp=self.head
        while temp.next is not None:
            temp=temp.next
        temp.next=new_node
        
    def insert_specefic(self,data,pos):
        new_node=Node(data)
        temp=self.head
        for i in range(1,pos-1):
            temp=temp.next
            
        new_node.next=temp.next
        temp.next=new_node
        
    def display(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next
ob=SLL()
while True:
    print("1.Insert into Begins")
    print("2.Display")
    print("3.Insert At Last")
    print("4.Insert At Specefic")
    ch=int(input("Enter Your Choice "))
    if(ch==0):
        print("Invalid Choice")
        break
    elif(ch==1):
        no=int(input("Enter The Value of Begining Point"))
        ob.insert_begin(no)
    elif(ch==2):
        ob.display()
    elif(ch==3):
        no=int(input("Enter The Value of Last Point"))
        ob.insert_last(no)
    elif(ch==4):
        no1=int(input("Enter The Position"))
        no=int(input("Enter The Value of Specefic Point"))
        ob.insert_specefic(no,no1)
