print("Number 1:", end=" ")
num = 1
for i in range(7):
    print(num, end=", " if i < 6 else "\n")
    num += 2  


print("Number 2:", end=" ")
num = 13
for i in range(7):
    print(num, end=", " if i < 6 else "\n")
    num -= 3  


print("Number 3:", end=" ")
num = 0
increment = 0
for i in range(7):
    print(num, end=", " if i < 6 else "\n")
    increment += 1
    num += increment
