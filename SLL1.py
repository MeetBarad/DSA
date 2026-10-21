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
    
    def delete_begin(self):
        self.head=self.head.next
    
    def delete_last(self):
        if self.head.next is None:
            self.head = None
            print("Last node deleted")
            return

        temp = self.head
        while temp.next.next is not None:
            temp = temp.next

        temp.next = None
        print("Last node deleted")

    def delete_specefic(self,pos):
        temp = self.head
        for i in range(1, pos - 1):
            temp = temp.next
        temp.next = temp.next.next
        
    def display(self):
        temp=self.head

        while temp is not None:
            print(temp.data)
            temp=temp.next

    def count(self):
        c=0
        temp=self.head

        while temp is not None:
            c=c+1
            temp=temp.next
        print("Total Node: ",c)

    def search(self,data):
        temp=self.head

        while temp is not None:
            if temp.data==data:
               print("Data Found")
            else:
                print("Data Not Found")
            temp=temp.next
            
    def reverse(self):
        prev=None
        temp=self.head

        while temp is not None:
            next_node=temp.next
            temp.next=prev
            prev=temp
            temp=next_node
        self.head=prev
ob=SLL()
while True:
    print()
    print("1.Insert into Begins")
    print("2.Display")
    print("3.Insert At Last")
    print("4.Insert At Specefic")
    print("5.Delete At Begining")
    print("6.Delete At Last")
    print("7.Delete At Specefic")
    print("8.Count")
    print("9.Search")
    print("10.Reverse")
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
    elif(ch==5):
        ob.delete_begin();
    elif(ch==6):
        ob.delete_last();
    elif(ch==7):
        no1=int(input("Enter The Position"))
        ob.delete_specefic(no1);
    elif(ch==8):
        ob.count();
    elif(ch==9):
        no=int(input("Enter The Value of Specefic Point"))
        ob.search(no);
    elif(ch==10):
        ob.reverse();
