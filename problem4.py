#Adrian Garcia
#11/14/2024
#The code tells us if the year that we have is a leap year then it will prompt us with true and if it's not then it's false.

def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

print(is_leap_year(2020))
print(is_leap_year(1900))
print(is_leap_year(2000))
print(is_leap_year(2024))