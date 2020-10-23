alphabet = ["A", "B", "C", "D"]

#To iterate a list
for letter in alphabet:
    print(letter, end = " ")
print("\n")

#With len() of list
for i in range(len(alphabet)):
    print("At index", i, "letter is", alphabet[i])
print("\n")

#With 3 parameters range(start, stop, size)
#Starts from second letter.
for i in range(1, len(alphabet), 1):
    print(alphabet[i], end = " ")
print("\n")

#Alternate letters from first letter
for i in range(0, len(alphabet), 2):
    print(alphabet[i], end = " ")
else: print("\nDone..\n")
      

#nested loops
rows = 5
for i in range(1, rows+1):  
    for j in range(rows-i+1):
        print(i, end = ' ')  
    print()  



for i in range(5):
    for j in range(3):
        print(i,"=>", i*j)

