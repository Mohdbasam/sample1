from heapq import merge

my_dict = {'apple':5,'orange':10,'banana':25}
my_dict2 = {'kiwi':8,'mango':19,'papaya':21}

merged_dict = my_dict.copy()
merged_dict.update(my_dict2)
print(merged_dict)