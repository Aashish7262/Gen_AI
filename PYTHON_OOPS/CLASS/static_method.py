# static methods are the methods that donot use the self parameter

class student:
    @staticmethod
    def hello():
        print("Hello how are you")

s1 =  student()
s1.hello()