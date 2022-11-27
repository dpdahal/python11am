# print("hello python")

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# for x in data:
#     print(x)

# a=data[0]
# b=data[1]


# for a in range(1, 6):
#     print("Hello Sophia")

# x = 1
# total_env = 0
# total_odd = 0
#
# while x <= 10:
#     if x % 2 == 0:
#         total_env += 1
#     else:
#         total_odd += 1
#
#     x += 1
#
# print("Total even numbers: ", total_env)
# print("Total odd numbers: ", total_odd)


# x = 1
# names = []
# while x <= 5:
#     name = input("Enter your name: ")
#     names.append(name)
#     x += 1
#
# for name in names:
#     print(f"Hello {name}")

# data = [1, 2, 3, 4, 5]
# for a in data:
#     print(a)

# data = [
#     [12, 13, 14, 15],
#     [16, 17, 18, 19],
#     [20, 21, 22, 23],
# ]
# for a in data:
#     for b in a:
#         print(b)
#     print("==================")


# num_of_times = int(input("Enter number of times: "))
# increment = 1
# data = []
#
# while increment <= num_of_times:
#     num = int(input("Enter number: "))
#     data.append(num)
#     increment += 1
#
# rep_num = []
# # data=[1,2,3,4,2,3]
# for x in data:
#     if data.count(x) > 1 and x not in rep_num:
#         rep_num.append(x)
#
# for y in rep_num:
#     print(f"{y} is repeated {data.count(y)} times")

# x = int(input("Enter x: "))
# y = int(input("Enter y: "))
# z = int(input("Enter z: "))
# if x > y and x > z:
#     if y > z:
#         x, y, z = x, y, z
#     else:
#         x, y, z = x, z, y
# elif y > x and y > z:
#     if x > z:
#         x, y, z = y, x, z
#     else:
#         x, y, z = y, z, x
# elif z > x and z > y:
#     if x > y:
#         x, y, z = z, x, y
#     else:
#         x, y, z = z, y, x
# else:
#     x, y, z = x, y, z
# print(f"Sorted numbers: {x}, {y}, {z}")


# data = ['ram', 'sita', 'hari', 'gita', 'ram', 'hari']
# ram
# ram,ram


# x = 10
# print(f"Number is {x}")
# print("Number {}".format(x))
# print("Number is", x)
# print(x)

# name,age,phone,address


# list
list1 = ['shashank', 12, 912123123, 89.98]
print(list1)

# append
list1.append('sujana')
print(list1)

list1.insert(2, 'rithik')
print(list1)

# delete

list1.pop()
print(list1)

list1.pop(0)
print(list1)

list1.remove('rithik')
print(list1)

# list1.clear()
# print(list1)

# del list1
# print(list1)

# update
# list1[0] = 'shashank'
# print(list1)
#
# list1[1] = 'pravidhi'
# print(list1)
#
# print(list1.count('shashank'))
# print(len(list1))
#
#
# # tuple
#
# tuple1 = ('shashank',12,912123123,89.98)
# # print(tuple1.append(12))
#
# # sets
# # order is not fixed
# set2 = {'shashank',12,912123123,89.98,12}
# print(set2)
#
#
# # dictionary
#
# dict1 = {'name':'shashank','age':12,'phone':912123123,'marks':89.98}
# print(dict1)
#
# # dictionary methods
# print(dict1['name'])
# print(dict1.get('name'))
#
# print(dict1['age'])

# print
# types conversion
# Data types
# variable, rule
# numbers, strings, list, tuple, sets, dictionary
# condition statements: if elif else nested if else
# loops: for while, nested loop
# functions: introduction
# modules: introduction

# def add(x, y):
#     return x + y
#
#
# print(add(10, 20))
# print(add(100, 200))

# import tkinter as tk
#
# window = tk.Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.mainloop()

# data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#
# data = ['ram', 'sita', 'gita', 'hari']
#
# res = ", ".join(data)
# print(res)
#
# data = {
#     'name': "sophia",
#     'age': 12,
#     'phone': 912123123,
#     "address": "kathmandu",
#     "town": {
#         "name": "putalisadak",
#         "tole": {
#             "name": "kamaladi",
#             "ward": [
#                 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
#             ]
#         },
#     },
#     "students": [
#         {
#             "name": "shashank",
#         }
#     ]
#
# }


# students = [
#     ['rita', 'gita', 'sita', 'binita', 'nita'],
#     ['ram', 'hari', 'shyam', 'gopal', 'suresh'],
#     ['laxmi', 'radha', 'nabina', 'kalpana', 'sophia']
# ]

# x = 0
#
# while x < len(students):
#     y = 0
#     while y < len(students[x]):
#         print(students[x][y])
#         y += 1
#     x += 1

# for use
# for student in students:
#     for name in student:
#         print(name)

# while use


# num = int(input("Enter number: "))
# total even number
# total odd number

#
# def dell():
#     print("dell")
#
#
# def hp():
#     pass
#
#
# def lenovo():
#     pass


# my_rep(data,times)


# data = []
# data.append('ram')
# data.append('sita')
# data.append('ram')
