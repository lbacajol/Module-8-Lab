# Leslie Bacajol
# 11/19/21
# This program takes two inputs from a user and prints whether the sum is greater than 10, less than 10, or equal to 10

first = int(input("Enter first number: "))
second = int(input("Enter another number: "))
comparison = 10
if first + second > comparison:
    print("The total is greater than 10")
if first + second < comparison:
    print("The total is less than 10")
if first + second == comparison:
    print("The total equals to 10")
