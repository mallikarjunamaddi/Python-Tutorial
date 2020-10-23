# Functions are reusable code.
# Modularity, (to organize the code.)
# in built functions
# User defined functions.
# type <class 'function'>

# Creating a function
# def add():
#     a = 10
#     b = 12
#     c = a + b
#     print(c)

# invoking/calling a function 
# print("line 15")   
# add()
# print("line 16")

# return stmt
# def addWithReturn():
#     a = 10
#     b = 12
#     c = a + b
#     return c

# result = addWithReturn()
# result = result / 2
# print(result)

# Defualt return value when 
# return statment doesn't exsist.
# res = add()
# print(res) 

# With Arguments.
# Required Arguments.
# def addWithArguments(a, b):
#     c = a + b
#     return c

# print(addWithArguments(1, 2))

#call by value
# def manipulate(a, b):
#     print("id(a) in func:",id(a))
#     print("In the function, before updating", a, b)
#     a = 100
#     b = 200
#     print("In the function, after updating", a, b)
#     print("id(a) in func after manipulation:",id(a))


# a = 10
# b = 20
# print("Inital a, b", a, b)
# print("id(a) outside the func:", id(a))
# manipulate(a, b)
# print("final a, b", a, b)

# call by reference
# def replace(items):
#     print("Inside the func, before updating", items)
#     items[0] = 100
#     items[1] = 200
#     print("Inside the func, after updating", items)


# lis = [10, 20]
# print("Initial values", lis)
# replace(lis)
# print("Final values", lis)

# a = 10
# b = a
# print(id(a), id(b))
# b = 20
# print(id(a), id(b))


# # Types of Arguments.

# Default Arguments
# def addWithDefaultArgs(a, b=10):
#     print(a+b)

# addWithDefaultArgs(22, 22)
# addWithDefaultArgs(22)

# # Variable length Arguments
# def addVaribleArgs(*items): 
#     sum = 0
#     for i in items:
#         sum = sum + i
#     print(sum)

# addVaribleArgs(22, 22)
# addVaribleArgs(22, 12, 2)
# addVaribleArgs(22)
# addVaribleArgs()

# Keyword arguments or named arguments.
# def divideKeywordArgs(a, b):
#     print(a/b)

# divideKeywordArgs(1, 2)
# divideKeywordArgs(b = 1, a = 2)


# # Scope of a variable.
# # Global variables
# x = 10
# def globalVar():
#     # x = 2
#     global x
#     x = 2
#     print(x)

# globalVar()
# print(x)

# #locla variables
# def localVar():
#     y = 20
#     print(y)

# localVar()
# print(y)




