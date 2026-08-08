# constructor is the __init__ function invoke when the object is created 
class student:
    college = "ABC College" # static object or class attributes
    name = "anonymous" # class attributes 
    def __init__(self):
        print("I am default constructor")
    def __init__(self,name,marks):
       self.name = name
       self.marks = marks
       print("I am parameterized constructor ")

    #methods
    def hello(self):
        print("Hello ",self.name)


n = int(input('enter the number of instances to create : '))
i = 0
while i<n:
    s = input('enter the student name : ')
    j = int(input('enter the student marks : '))
    s1 = student(s,j)
    print(s1.name)
    print(s1.marks)
    print(s1.hello())
    i = i+1
