
# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))




# Combine Positional-Only and Keyword-Only
# You can combine the two argument types in the same function.

# Any argument before the / , are positional-only, and any argument after the *, are keyword-only.


# def my_function(a, b, /, *, c, d):
#   print(a + b + c + d)

# my_function(5, 6, c=7, d = 8)


# Arbitrary Keyword Arguments, **kwargs
# If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.

# This way the function will receive a dictionary of arguments, and can access the items accordingly:


# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# The phrase Keyword Arguments are often shortened to kwargs in Python documentations.
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)

# Arbitrary Arguments, *args
# If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition.

# This way the function will receive a tuple of arguments, and can access the items accordingly:

# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def my_function(**kid):
#   print("His last name is " + kid['fname'])
#   print("His first name is " + kid['lname'])

# my_function(fname="tom",lname="smith")
# def my_function(**kid):
#   print("His last name is " + kid["lname"])
#   print("His first name is " + kid["fname"])

# my_function(fname = "Tobias", lname = "Refsnes")


# def my_function(*, x):
#   print(x)

# my_function(x=3)

# adj = ["red", "big", "tasty"]
# fruits = ["apple", "banana", "cherry"]

# for x in adj:
#   for y in fruits:
#     print(x, y)

# for x in range(6):
#   if x == 3: break
#   print(x)
# else:
#   print("Finally finished!")

# for x in range(2, 9,2):
#   print(x)

# for x in range(6):
#   print(x)

# i = 1
# while i < 6:
#   i += 1
#   if i == 3:
#     break
#   print(i)
# else:
#   print("random")

# a = 330
# b = 330
# print("A") if a > b else print("=") if a == b else print("B")


# a=30
# b=20
# c = a if a < b else b
# print(c)
# myLists=[1,2,3,6,8,2]
# # newLists = [x if x > 1 else x - 1 for x in myLists ]
# newLists = [x if x > 4 else x - 1 for x in myLists if x > 1]
# print(newLists)


# child1 = {
#   "name" : "Emil",
#   "year" : 2004
# }
# child2 = {
#   "name" : "Tobias",
#   "year" : 2007
# }
# child3 = {
#   "name" : "Linus",
#   "year" : 2011
# }

# myfamily = {
#   "child1" : child1,
#   "child2" : child2,
#   "child3" : child3
# }

# print(myfamily.values())


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# mydict = thisdict.copy()
# mydict["brand"]="cool"
# anotherDict=dict(mydict)
# print(thisdict)
# print(mydict)
# print(anotherDict)


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# # thisdict.pop("model")
# del thisdict["year"]
# if "model" in thisdict:
#   print("Yes, 'model' is one of the keys in the thisdict dictionary")
# else:
#   print("no item")



# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }

# x = car.items()

# print(x) #before the change

# car["year"] = 2020

# print(x) #after the change


# thisdict = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# y=thisdict.values()
# print(type(y))
# for x in thisdict.keys():
#     print(thisdict.get(x))



# myset={"hello","world"}
# myList=["hello","world","you"]
# newSet = set(("hello",True,1,25))
# for x in newSet:
#     print(x)