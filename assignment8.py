# q.1 calculate area and circumference of a circle
class circle:
    def __init__(self):
        self.ra=10
    def getArea(self):
        self.area=3.14*(self.ra**2)
        print(self.area)
    def getcircumference(self):
        print(2*3.14*self.ra)
p=circle()
p.getArea()
p.getcircumference()

# q.2 make a class student and display its required info
class student:
    def __init__(self):
        self.n=input("Enter a Name")
        self.r.no=int(input("Enter a Roll.no"))
        self.age=0
        self.m=0
    def display(self):
        print(self.n,self.r.no,self.age,self.m)
    def setAge(self):
        self.age=int(input("Enter a Age"))
    def setmarks(self):
        self.m=int(input("Enter Marks"))
r=student()
r.setAge()
r.setmarks()
r.display()


# q.3 convert temperature

class temperature:
    def __init__(self):
        self.ct=0
        self.ft=0
    def convertFahrenheit(self):
        self.ct=float(input("Enter the temperature in celsius"))
        self.ft=self.ct*1.8+32
        print(self.ct,"celsius=",self.ft,"Fahrenheit")
    def convertcelsius(self):
        self.ft=float(input("Enter the temperature in celsius"))
        self.ct=(self.ft - 32) * 0.5556
        print(self.ftemp,"Fahrenheit=",self.ct,"celsius")
a=temperature()
a.convertFahrenheit()
a.convertcelsius()

# q.4 create a class moviedetails and perform the required functionalities

class MovieDetails:
    def Display(self):
        print("Required Movie Details:")
        print("Artist Name:-",self.aname,"\n Year Of Release:-",self.y,"\n Rating:-",self.ra)
    def Add(self):
        self.aname=input("Enter Artist Name:- ")
        self.y=int(input("Enter year Of release:- "))
        self.ra=float(input("Enter The Rating"))
t=MovieDetails()
t.Add()
t.Display()

# q.5 inheritance(animal)

class animal:
    def info_(self):
        print("Animal_Class")
class animal_attribute():
    def attribute(self):
        print("Animal_Attributes")
class tiger(animal,animal_attribute):
    def s(self):
        print("Tiger Class")
e=animal()
k=animal_attribute()
c=tiger()
c.info_()
c.attribute()

# q.6 determine the output
output= A B
		A B


# q.7 inheritance (shapes)
class shape:
    def method_area(self):
        self.l=int(input("Enter The length"))
        self.b=int(input("Enter the breadth"))
class rectangle(shape):
    def method_area(self):
        self.l=int(input("Enter The length of Rectangle"))
        self.b=int(input("Enter The breadth of rectangle"))
class square(shape):
    def method_area(self):
        self.l=int(input("Enter The length of sides of square"))
x=shape()
y=rectangle()
z=square()
y.method_area()
z.method_area()
