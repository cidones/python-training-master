class Student:
    def __init__(self):
        self.name = 'cidones'
        self.age = 38
        self.marks = 95

    def talk(self):
        print("Name - ", self.name)
        print("Age - ", self.age)
        print("Marks - ", self.marks)


s1 = Student()
s1.name = 'Cidop'

print(s1.name)
