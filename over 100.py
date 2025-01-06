n = int(input("How values you want to store : "))
list1 = []
print(f"Enter {n} values : ")
for x in range(n):
    a = int(input())
    if a > 100:
        list1.append("over")
    else:
        list1.append(a)

print(list1)