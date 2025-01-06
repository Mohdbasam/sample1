words = ["apple","banana","papaya","kiwi"]

lw = ""

for word in words:
    if len(word) > len(lw):
        lw = word
ll = len(lw)

print(lw)
print(ll)