a = int(input("Enter staring year : "))
b = int(input("Enter ending year : "))
print(f"Leap years btw {a} and {b} are :")
for x in range(a,b+1):
    if x%4==0 and x%1000!=0 or x%400==0:
        print(x)