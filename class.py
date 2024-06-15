import datetime

x = datetime.datetime.now()
print(x.year)
# Directive	Description	Example	Try it
# %a	Weekday, short version	Wed	
# %A	Weekday, full version	Wednesday	
# %w	Weekday as a number 0-6, 0 is Sunday	3	
# %d	Day of month 01-31	31	
# %b	Month name, short version	Dec	
# %B	Month name, full version	December	
# %m	Month as a number 01-12	12	
# %y	Year, short version, without century	18	
# %Y	Year, full version	2018	
# %H	Hour 00-23	17	
# %I	Hour 00-12	05	
# %p	AM/PM	PM	
# %M	Minute 00-59	41	
# %S	Second 00-59	08	
# %f	Microsecond 000000-999999	548513	
# %z	UTC offset	+0100	
# %Z	Timezone	CST	
# %j	Day number of year 001-366	365	
# %U	Week number of year, Sunday as the first day of week, 00-53	52	
# %W	Week number of year, Monday as the first day of week, 00-53	52	
# %c	Local version of date and time	Mon Dec 31 17:41:00 2018	
# %C	Century	20	
# %x	Local version of date	12/31/18	
# %X	Local version of time	17:41:00	
# %%	A % character	%	
# %G	ISO 8601 year	2018	
# %u	ISO 8601 weekday (1-7)	1	
# %V	ISO 8601 weeknumber (01-53)	01
print(x.strftime("%C"))

y = datetime.datetime(2020, 5, 17)

print(y)

# def myfunc1():
#   x = "Jane"
#   def myfunc2():
#     nonlocal x
#     x = "hello"
#   myfunc2()
#   return x

# print(myfunc1())


# x = 300

# x = 300

# def myfunc():
#   global x
#   x = 200

# myfunc()

# print(x)


# Inheritance Class Polymorphism
# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def size(self):
#     print("small!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def size(self):
#     print("medium!")

# class Plane(Vehicle):
#   def size(self):
#     print("Large!")

# car1 = Car("Ford", "Mustang") #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747") #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   print("_________")
#   x.size()
#   print("_________")



# To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.

# class MyNumbers:
#   def __iter__(self):
#     self.a = 18
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration
  

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))


# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# All these objects have a iter() method which is used to get an iterator:


# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))


# class Person:
#   def __init__(self, fname, lname):
#     self.firstname = fname
#     self.lastname = lname

#   def printname(self):
#     print(self.firstname, self.lastname)


# class Child(Person):
#     def __init__(self, fname, lname, hobby):
#        super().__init__(fname,lname)
#        self.hobby=hobby
# alen = Child(fname="alen",lname="smith",hobby="dota2")
# alen.printname()
# print(alen.hobby)


#Use the Person class to create an object, and then execute the printname method:

# x = Person("John", "Doe")
# x.printname()



# class MyClass:
#     def __init__(self,name,age) -> None:
#         self.name= name
#         self.age= age
#     def __str__(self):
#         return f"{self.name}({self.age})"
    
#     def myfunc(self):
#         print("Hello my name is " + self.name)
# myClass= MyClass("alen",25)

# myClass.myfunc()
