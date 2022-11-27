# type of function: 1. built-in function 2. user-defined function
# built-in function: print,len,range,abs,round,sorted,zip,enumerate,filter,map,reduce

# what is function? function is a block of code which only runs when it is called.
# you can pass data,
# known as parameters, into a function.
# a function can return data as a result.

# define a function
# def my_function():
#     # function body
#     print("Hello from a function")
#
#
# # call a function
# my_function()

# function with parameter


# def my_function(full_name, address):
#     # print("Hello " + full_name)
#     # print("your name is {} {}".format(full_name,address))
#     print(f"My name is: {address} City: {address}")
#
#
# my_function("John Doe", "Dhaka","Test")

# function with default parameter or optional parameter
# def my_function(full_name, address="Dhaka"):
#     print(f"My name is: {full_name} City: {address}")
#
#
# my_function("John Doe", "Kathmandu")


# function with return value

# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))


# def my_function(name,age):
#     return f"Hello {name} your age is {age}"
#     # return f"Hello {age}"
#
# print(my_function("John Doe",20))


# a =12,3,4,5
# print(a)


# def add_sub(x, y):
#     c = x + y
#     d = x - y
#     return [c, d]
#
# result = add_sub(5, 4)
# # list
# print(result[0])
# print(result[1])

# def user():
#     print("Hello from user function")
#
#
# def result():
#     user()
#
#
# result()

#
# def take_value():
#     p = int(input("Enter the value of p: "))
#     t = int(input("Enter the value of t: "))
#     r = int(input("Enter the value of r: "))
#     return [p, t, r]
#
#
# def calculate():
#     sp = take_value()
#     return sp[0] * sp[1] * sp[2] / 100
#
#
# def display():
#     print(f"Simple interest is: {calculate()}")
#
#
# display()

# function scope
# local scope
# global scope


# x = 10
#
#
# def my_function():
#     global x
#     x = x + 50
#     print(x)
#
#
# my_function()
#
# print(x)
# args

# def users(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# users('ram', 'sita', 'gita', 'hari', name='sophia', age=30)


# def info():
#     return "Hello"
#
#
# print(info())


# def add(x, y, z):
#     return x + y + z
#
#
# print(add(10, 20, 30))

#  name,email,address,phone

def user_info():
    name = input("Enter your name: ")
    email = input("Enter your email: ")
    address = input("Enter your address: ")
    phone = input("Enter your phone: ")
    return f"Name: {name} \n Email: {email} Address: {address} Phone: {phone}"


print(user_info())