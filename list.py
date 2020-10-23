# #mutable
# #hetirogenous
# #type <class 'list'>

# #initialization
# todo_list = ["Milk", "workout", 20, True]

# # characteristics
# # ordered
# # indexing starts with '0'
# # can store any number of elements

# #orderedl5 = [1, "age",  True, "value"]
# l1 = [1, 2, 3, 5]
# l2 = [1, 2, 5, 3]
# print(l1 == l2)

# l3 = [1, 2, 3, 5]
# print(l1 == l3)

# #indexing 
# l4 = ["Ram", 24, True]
# print(l4[1])


# #slicing or sublist
# l5 = [1, "age",  True, "value", 5 , 6]

# print(l5)
# print(l5[1:3])
# print(l5[1: ])
# print(l5[ :4])
# print(l5[:])

#special case, step
# print(l5[1:5:2])

# #updating lists
# l6 = [ 5, "Ram", 6, 7, 9]
# print(l6)

# l6[1] = 6
# print(l6)

# l6[2:len(l6)] = [7, 8, 9]
# # l6[2:5] = [7, 8, 9]

# print(l6)

#deletion
# l7 = [1, 2, 3, 4]
# print(l7)

# del l7[2]
# print(l7)

## del l7
## print(l7)

# # remove()
# l7 = [1, 2, 3, 4]
# print(l7)
# l7.remove(3)
# print(l7)

# #list operators
# l8 = [1,2 ,3, 4]
# print(l8)

# #repetion operator
# print(l8 * 2)
# print(l8)

# #concatenation 
# l9 = [5, 6, 7, 8]
# print(l8 + l9)

# #membership operator
# print( 6 in l8 )
# print( 7 in l9 )

# iterating the list 
# for item in l9:
#     print(item) 


# #built in methods
# l10 = [ 8, 4, 6, 6, 9, 10, 12 ]     

# #length
# print(len(l10))

# #max
# print(max(l10))

# #min
# print(min(l10))

# #list, type conversion

# a = "ram"
# print(type(a))

# b = list(a)
# print(b)

# #append method
# l11 = [ 1, 2, 3, 4]
# print(l11)

# l11.append(2)
# print(l11)

# #example on removing odd elements

# numbers = [2,6,4,10,15,13,18,27,19]
# # temp = numbers
# temp = list(numbers)
# even_numbers = []

# for number in temp:
#     # print(a, a%2, (a%2)!=0)
#     if (number%2)!=0:
#        numbers.remove(number)

# print(numbers)


# numbers = [2,6,4,10,15,13,18,27,19]
# even_numbers = []

# for number in numbers:
#     if not number%2:
#        even_numbers.append(number)

# print(numbers)
# numbers = even_numbers
# print(numbers)
