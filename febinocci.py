s1 = 0
s2 = 1

length = int(input("Enter Series Length: "))
while(length):
    print(s1, end=" ")
    s1, s2 = s2, s1+s2
    length-=1