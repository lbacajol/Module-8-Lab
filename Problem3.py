# Leslie Bacajol
# 11/19/21
# This program takes a list and prints if the value 5 is in that list

list = [5, 10, 15, 20, 25]
for item in list:
    if item == 5:
        print(item)

# or

list = [5, 10, 15, 20, 25]
n = list.count(5)
print(n)