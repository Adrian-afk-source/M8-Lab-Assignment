#Adrian Garcia
#11/13/2024
#This allows the user the pick any number and will prompt us a message if it's equal to, less than, or greater than 10.

x = int(input("Pick a number!: "))
y = int(input("Pick a number!: "))
if x + y == 10:
    print("x plus y is equal to 10!")

elif x + y < 10:
    print("x and y are leass than 10!: ")
else:
    print("x + y are greater than 10!: ")
