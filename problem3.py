#Adrian Garcia
#11/14/2024
#This code will tell look for 5 in the list and it will give us two promts if it is in the list and if it's not.

def check_for_five(lst):
    if 5 in lst:
        print("The value 5 is in the list.")
    else:
        print("The value 5 is not in the list.")
my_list = [1, 2, 3, 4, 5]
check_for_five(my_list)

my_list = [1, 2, 3, 4]
check_for_five(my_list)