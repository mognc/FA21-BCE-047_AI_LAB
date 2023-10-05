class student:
    count = 0
    marks_total =0
    def __init__(self, name,roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks
        student.count +=1
    def add_marks(self):
        student.marks_total += self.marks
    def calculate_average(self):
        avg = sum(self.marks)/student.count
        return avg 

student1 = student("ali","Fa21-bce-047",{1,2,3,5})

print("The name of student is: ", student1.name)
print("Total marks of student: ", student1.add_marks())
print("Average of marks: ", student1.calculate_average())
