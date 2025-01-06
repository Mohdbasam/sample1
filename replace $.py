a = input("Enter a word : ")

b = a[0]

c = a[1:]

result = b

for x in c:
    if x == b:
        result +="$"
    else:
        result+=x
print(result)