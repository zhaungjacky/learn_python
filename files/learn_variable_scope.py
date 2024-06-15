'''
LEGB
Local Enlosing Global,Built-in
'''
x='global x'
def outer(): # Enclosing
    x = "outer x"

    def inner():
        # nonlocal x # x-> point to the outer x
        x = "inner x"
        print(x)
    
    inner()
    print(x)

outer()
print(x)


# import builtins

# print(dir(builtins))


# x='global x'

# def test(z):
#     # global x # without global x the x variable below is local
#     # x="local x"

#     # print(y)
#     print(z)

# test("local z")
# print(x)