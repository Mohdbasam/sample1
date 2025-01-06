list1 = [10,12]
list2 = [4,5,6,7]
if len(list1) == len(list2):
    print("Both are same length")
else :
    print("Both are not same length")

if sum(list1) == sum(list2):
    print("Both sum are same")
else:
    print("Both sum are not same")
print("The common numbers : ")
for i in list1:
    for j in list2:
        if i == j:
            print(i)