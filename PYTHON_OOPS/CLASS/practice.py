class student:
    def __init__(self,marks_s1,marks_s2,marks_s3):
        self.marks_s1 = marks_s1
        self.marks_s2 = marks_s2
        self.marks_s3 = marks_s3
    
    def average(self):
        return (self.marks_s1+self.marks_s2+self.marks_s3) / 3.0

       