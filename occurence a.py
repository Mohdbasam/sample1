a = int(input("Enter how many names you want store : "))
list1 = []
count = 0
print(f"Enter {a} names, only first name ")
for x in range(a):
    b = input()
    list1.append(b)

for i in list1:
    for j in i:
        if "a" in j:
            count+=1
print("The occurence of a are : ",count)