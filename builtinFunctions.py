# # Readily Available Functions

# # abs() => gives magnitude
# value = -10
# print(value, abs(value))

# value = 10+2j
# print(value, abs(value))

# # boo() => converts to bool
# value = 0
# print(value, bool(value))
# value = 'hello'
# print(value, bool(value))


# def x():
#   pass

# print(x, callable(x))
# print(value, callable(value))

# # compile(), exec()
# code_str = 'x=5\ny=10\nprint("sum =",x+y)'  
# code = compile(code_str, 'sum.py', 'exec')  
# print(code, type(code))  

# # exec() with code Object
# exec(code)  

# # exec() with code string 
# exec(code_str)  

# # sum()
# valueList = [1, 2, 4, 5, 20]
# print(valueList, sum(valueList))

# # len()
# print(valueList, len(valueList))

# # map()
# def double(number):
#     value = number*2
#     return value

# resultList = map(double, valueList)
# print(valueList, list(resultList))

# # divmod() => gives remainder and quotient
# result = divmod(11,2)  
# print(result) 

# numberList = [2, 3, 4, 6, 60, 9, 11, 12]

# def isEven(number):
#     return number % 2 == 0

# resultList = filter(isEven, numberList)
# print(numberList, list(resultList))   

# # min()
# print(min(2, -1, 19))

# # sorted()
# print(numberList, sorted(numberList))
# print(numberList, sorted(numberList, reverse=True))

# # pow()
# number = 2
# print(number, pow(number, 2))
# print(number, pow(number, -2))

# # reversed
# print(numberList, list(reversed(numberList)))

# # round()
# number = 20.5
# print(number, round(number))
# number = 20.8
# print(number, round(number))