# while
# break
# continue
# pass

# while condition :
#     block


# 1 to 10 even digits

# i = 1

# while(i<11 and i>=0):
#     if not i%2 :
#        print(i, end = " ")
#     i+=1


# i = 1
# sum = 0
# while i<=100:
#     sum = sum + i
#     i = i+1
# else: print(sum)


# i = 1
# sum = 0
# while i<=100:
#     sum = sum + i
#     if sum > 500:
#         break
#     i = i+1
# else: print(sum)
# print(sum, " done")

# i = 1
# j = 1
# a = 3
# while i < 2:
#     print(i)
#     while j< 3:
#         print(j)
#         j = j + 1
#         if a>2 :
#             print("came out from inner loop")
#             break
#     print("hello")
#     i = i + 1

# i = 1
# j = 1
# a = 3
# while i < 2:
#     print(i)
#     while j< 3:
#         print(j)
#         j = j + 1
#         if a>2 :
#             continue
#             print("code is neglected")
#     print("hello")
#     i = i + 1

# def add(a, b):
#     pass

# for i in range(10):
#     pass


# prime numbers: number 1 and itself
# 2 5 7
# 6 8 12

# number = int(input("Enter a number: "))
# factor = 2

# while factor < number:
#     if not number % factor:
#         break
#     factor+=1
# else: print(number, "is a Prime Number.")

# if factor!=number:
#    print(number, "is a composite number.")

# 0 1 1 2 3 5....
length = int(input("Enter Length of the series: "))
s1, s2 = 0, 1
while length>0:
    print(s1, end = " ")
    s1, s2 = s2, s1+s2
    length-=1


# s1 = 0
# s2 = 1 
# s3 = s1 + s2

# s4:
# s1 = s2
# s2 = s3

# s4 = s1+s2

# s4 = s2 + s3

# s5 = s3 + s4

# calculator

# a,b operation 

