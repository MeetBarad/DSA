class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SLL:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_Node = Node(data)

        if self.head is None:
            self.head = new_Node
            return

        temp = self.head

        while temp.next is not None:
            temp = temp.next

        temp.next = new_Node

    def display(self):
        temp = self.head

        while temp is not None:
            print(temp.data)
            temp = temp.next

ob = SLL()
while True:
    print("1.Insert\n2.Display\n3.Exit")
    ch=int(input("Enter Your Choice"))

    match ch:
        case 1:
            dt=int(input("Enter The Value"))
            ob.insert(dt)
        case 2:
            ob.display()
        case 3:
            exit();
        case _:
            print("Invalid Choice")
