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

ob.insert(10)
ob.insert(20)
ob.insert(30)
ob.insert(40)
ob.insert(50)

ob.display()
