number = int(input("Enter a number: "))
factor = 2
while(factor < number):
    if(not number % factor):
       print(number, "is not a Prime")
       break
    factor+=1
else: print(number, "is a Prime")
