
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


class DLL:
    def __init__(self):
        self.head = None

    # Insert at beginning
    def insert_begin(self, data):
        new = Node(data)

        if self.head is not None:
            new.next = self.head
            self.head.prev = new

        self.head = new
        print("Inserted at beginning")

    # Insert at last
    def insert_last(self, data):
        new = Node(data)

        if self.head is None:
            self.head = new
            print("Inserted at last")
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new
        new.prev = temp
        print("Inserted at last")

    # Insert at specific position
    def insert_specific(self, data, pos):
        if pos < 1:
            print("Invalid position")
            return

        if pos == 1:
            self.insert_begin(data)
            return

        temp = self.head

        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        new = Node(data)
        new.next = temp.next
        new.prev = temp

        if temp.next:
            temp.next.prev = new

        temp.next = new
        print("Inserted at position", pos)

    # Delete at beginning
    def delete_begin(self):
        if self.head is None:
            print("List is empty")
            return

        self.head = self.head.next

        if self.head:
            self.head.prev = None

        print("Deleted from beginning")

    # Delete at last
    def delete_last(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head

        if temp.next is None:
            self.head = None
            print("Deleted from last")
            return

        while temp.next:
            temp = temp.next

        temp.prev.next = None
        print("Deleted from last")

    # Delete at specific position
    def delete_specific(self, pos):
        if pos < 1 or self.head is None:
            print("Invalid position or empty list")
            return

        if pos == 1:
            self.delete_begin()
            return

        temp = self.head

        for i in range(pos - 1):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next

        if temp is None:
            print("Invalid position")
            return

        temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev

        print("Deleted from position", pos)

    # Display list
    def display(self):
        if self.head is None:
            print("List is empty")
            return

        temp = self.head
        print("None <-> ", end="")

        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next

        print("None")

    # Count nodes
    def count(self):
        temp = self.head
        c = 0

        while temp:
            c += 1
            temp = temp.next

        print("Total nodes:", c)

    # Reverse list
    def reverse(self):
        temp = self.head
        prev_node = None

        while temp:
            prev_node = temp.prev
            temp.prev = temp.next
            temp.next = prev_node
            temp = temp.prev

        if prev_node:
            self.head = prev_node.prev

        print("List reversed")

    # Search element
    def search(self, key):
        temp = self.head
        pos = 1

        while temp:
            if temp.data == key:
                print("Element found at position", pos)
                return

            temp = temp.next
            pos += 1

        print("Element not found")


dll = DLL()

while True:
    print("1. Insert at Beginning")
    print("2. Insert at Last")
    print("3. Insert at Specific Position")
    print("4. Delete at Beginning")
    print("5. Delete at Last")
    print("6. Delete at Specific Position")
    print("7. Display")
    print("8. Count")
    print("9. Reverse")
    print("10. Search")
    print("11. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        data = int(input("Enter data: "))
        dll.insert_begin(data)

    elif ch == 2:
        data = int(input("Enter data: "))
        dll.insert_last(data)

    elif ch == 3:
        data = int(input("Enter data: "))
        pos = int(input("Enter position: "))
        dll.insert_specific(data, pos)

    elif ch == 4:
        dll.delete_begin()

    elif ch == 5:
        dll.delete_last()

    elif ch == 6:
        pos = int(input("Enter position: "))
        dll.delete_specific(pos)

    elif ch == 7:
        dll.display()

    elif ch == 8:
        dll.count()

    elif ch == 9:
        dll.reverse()

    elif ch == 10:
        key = int(input("Enter element to search: "))
        dll.search(key)

    elif ch == 11:
        print("Program ended")
        break

    else:
        print("Invalid choice")
