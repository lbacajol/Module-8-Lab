# Leslie Bacajol
# 11/20/21
# This program takes a year as a parameter and returns True if the year is a leap year, False if it is otherwise

def is_leap(year):
    leap = False
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return not leap
    else:
        return leap


year = int(input("Enter year to check: "))
print(is_leap(year))
