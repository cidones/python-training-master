
# a class has always Capital letter - 
#you can create a class and different objects
class Student:
    #a constructor is a special type of method ( function ) which is used to initialize the instance members of the class. __init__ is a constructor method
    def __init__(self): # constructor or initializer automatically called when you create a new instance of a class.
        self.name = 'cidones'
        self.age = 38
        self.marks = 95


    def talk(self):
        print("Name - ", self.name)
        print("Age - ", self.age)
        print("Marks - ", self.marks)

#s1 is an object and is creating an instance of class
s1 = Student()
#object created 
print(s1.name)

s2 = Student()
print(s2.name, s2.age)

s1.talk() # instance method

#self variable contains the memory of an instance 
# each object has its own memory allocation 
# self example
#s1.name = "Sarda" - has your own id
#s1.name - will print cidones - has your own id
