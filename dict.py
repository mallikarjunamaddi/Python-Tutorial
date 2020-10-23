#Dictionary
#items are key-value pairs
#Mutable
#type <class 'dict'>
#keys: must be immutable objects
#values: can be anything

# # Creating a dict
# d1 = { 1: "Hello", "1": 2, (1,2): "2"}
# print(d1)

# #creating dictonary with dict()
# d2 = dict([(1, "hello"), (2, "world")])
# print(d2)

# # Creating Empty dict
# d3 = {}
# print(d3)

# #Accessing elements
# d4 = { 1: "Hello", "1": 2, (1,2): "2"}
# print(d4[1])
# print(d4["1"])
# print(d4[(1, 2)])

# #using get()
# print(d4.get(1))

# #Adding or updating a dict
# d5 = { "hello": 2, 0: "hi"}

# #Updating
# print(d5["hello"])
# d5["hello"] = "Welcome"
# print(d5["hello"])

# #Adding
# # print(d5[9])
# d5[9] = "nine"
# print(d5[9])
# print(d5)

# #Deleting
# d6 = { 0: "Ram", "age": 23, "gender": "M"}
# print(d6)
# del d6["gender"]
# print(d6)
# del d6[1]
# print(d6)
# del d6
# print(d6)

# #pop
# d7 = { 0: "Ram", "age": 23, "gender": "M"}
# print(d7)
# d7.pop(0)
# print(d7)

# #popitem()
# d7.popitem()
# print(d7)

# #clear()
# d7[1] = "texture"
# print(d7)
# d7.clear()
# print(d7)

# #Iterating, prints all keys
# d8 = {1: "hello", 0: "hii", 5: "hola", "hey": 2}

# for k in d8:
#     print(k)   

# #To print all values
# for k in d8:
#     print(d8[k])

# #using values()
# for v in d8.values():
#     print(v)    

# print(d8.values())

# # To print items of dic
# print(d8.items())
# for item in d8.items():
#     print(item)

# for k, v in d8.items():
#     print(k, v)

# # Builting methods
# d9 = {0: "And", 1 : "or"}
# print(d9)

# # len
# print(len(d9))    

# # str
# d10 = str(d9)
# print(d10, type(d10))
# print(d10[0])

# copy
# d11 = { 0 : "hii", "hii": 2}
# print(id(d11))

# d12 = d11
# print(id(d12))

# d13 = d11.copy()
# print(id(d13))

# # update
# print(d11)

# d14 = { 0 : "hi", 1: "hello"}
# print(d14)

# d11.update(d14)
# print(d11)