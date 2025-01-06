my_dict = {'apple':5,'orange':10,'banana':25}
ascending_dict = dict(sorted(my_dict.items()))
print("asending dict is : ",ascending_dict)
descending_dict = dict(sorted(my_dict.items(),reverse=True))
print("descending dict is : ",descending_dict)