class Student:

    def get_data(self):
        self.rollno = int(input("Enter The Roll no: "))
        self.name = input("Enter The Name: ")
        self.div = input("Enter The Division: ")
        self.course = input("Enter The Course: ")

    def set_data(self):
        print("Roll No:", self.rollno)
        print("Name:", self.name)
        print("Div:", self.div)
        print("Course:", self.course)


s1 = Student()

s1.get_data()
s1.set_data()



