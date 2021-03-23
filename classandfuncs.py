print("A Simple Function")
def add(a,b):
    print("Parameter 1:",a)
    print("Parameter 2:",b)
    return a + b

print(add(10,20))
print(add("abc",str(10)))

print("Classes & Functions")
class pyclass:
    name='inceptez class';
    def Addnums(self,x, y):  #The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
        return x + y

obj1=pyclass()
print(obj1.name)
print("calling Addnums function " + str(obj1.Addnums(10, 20)))

print("Duck typing")
#Duck type Language, When you use duck typing, you do not check (class) types at all. Instead, you check for the presence of a supporting methods, in the below + supports both types
def calc(a,b,c):return a+b+c
print(calc(10,20,30))
calcout=calc("inceptez ","tech","pvt ltd")
print(calcout)


print("OOPS in Python:")
print("Polymorphism")
print(len("Python"))
print(len(["Python", "Java", "Scala"]))
print(len({"Name": "Inceptez", "City": "Chennai"}))

lst = [5,4,2,3,1]
def func1() :
    if lst.count(6) == 1:
        print("method if block")
    elif lst.count(5)==1:
        print("method elif block")
    else:
        print("method else block")

func1()

def func1(arg1:str):
  print (arg1)

returnval=func1('hello method')
print(returnval)



print("Inheritance")
print("Single Inheritance")

# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")


# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")


# Driver's code
object = Child()
object.func1()
object.func2()


# multiple inheritance
print("Multiple Inheritance")
# Base class1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)

# Driver's code
s1 = Son()
s1.fathername = "x"
s1.mothername = "y"
s1.parents()


# multilevel inheritance
print("Multilevel Inheritance")
# Base class
class Grandfather:

    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername

        # invoking constructor of Grandfather class
        Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname

        # invoking constructor of Father class
        Father.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print("Father name :", self.fathername)
        print("Son name :", self.sonname)


#  Driver code
s1 = Son('Z is the son of Y', 'Y is the son of X', 'X')
print(s1.grandfathername)
s1.print_name()