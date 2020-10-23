#string
# collection of characters
# how to define strings
# type of string is <class 'str'>
# how to access individual charactes in string
# how to acccess substrings
# string operations
# string methods

#intializing
name = 'Ram'
occupation = "Software Engineer"
description = """We are meant to 
                   something innovative"""



# print(occupation)

# occupation = "Software Engineer fdjslfkjslajflsjfsd\
#                      helleo "
# print(occupation)  

# occupation = "Software Engineer fdjslfkjslajflsjfsd\nhelleo "
# print(occupation)                     

#indexing

# R a m m a l l i
# 0 1 2 3 4 5 6 7

      
# print(name[2])

# #substring

# print(occupation[0:5])

# print(occupation[2:7])

#special cases
# print(occupation[1:])
# print(occupation[:7])
# print(occupation[:]) 

# #negative indexing 
# print(occupation[-2])

# #negative slicing
# print(occupation[-7: -2])

# print(occupation[-8:])

# print(occupation[:-4])

# #reversing the string
# print(occupation[: : -1])



# #Re-assigning Strings
# nationality = "Indian"
# nationality = "american"
# print(nationality)

# nationality[0] = 'A'

# nationality = "American"
# print(nationality)


# #deleteing a String

# religion = "Hindhu"
# print(religion)
# del religion

# print(religion)

# religion = "christianity"
# print(religion)
# del religion[0]

# #concatination +
# firstName = "Maddi"
# name = "Ram"
# completeName = firstName + name

# print(completeName)

#repetition *
# print(name*3)   
# print(name)

# #membership in / not in

# print('R' in name)
# print('A' not in name)

# #Raw strings expressions r/R
# print('C:\\python37')  
# print(r'C:\\python37')  


#string formatting %
# print("My name is %s, age is %d"%(name, 10))



# format method
# print("{} and {} both are the best friend".format("Devansh","Abhishek")) 
 
  
# #Positional Argument  
# print("{1} and {0} best players ".format("Virat","Rohit"))  
  
# #Keyword Argument  
# print("{a},{b},{c}".format(a = "James", b = "Peter", c = "Ricky"))  


# #escape characters
# str1 = "They said, \"Hello what's going on?\""
# print(str1)

# print("Ram \
# raj")


# #string methods

# name = "ram"
# print(name.capitalize())
# print(name)

# name = "rAm"

# print(name.casefold())

# print(name.upper())

# print(len(name))

