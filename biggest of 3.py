a = int(input("Enter 3 numbers : "))
b = int(input())
c = int(input())

if a>b and a>c:
    print(f"{a} is the largest number : ")
elif b>a and b>c:
    print(f"{b} is the largest number : ")
elif c>a and c>b:
    print(f"{c} is the largest number : ")

else:
    print("Three numbers are same")