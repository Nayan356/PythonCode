# Write a program in Python to perform the following operator based task:
# ●	Ask user to choose the following option first:
# ○	If User Enter 1 - Addition 
# ○	If User Enter 2 - Subtraction
# ○	If User Enter 3 - Division
# ○	If USer Enter 4 - Multiplication
# ○	If User Enter 5 - Average
# ●	Ask user to enter the 2 numbers in a variable for first and second for the first 4 options mentioned above.
# ●	Ask user to enter two more numbers as first1 and second2 for calculating the average as soon as user choose an option 5.
# ●	At the end if the answer of any operation is Negative print a statement saying “zsa”
# ●	NOTE: At a time user can perform one action at a time.
x=int(input("Enter any number between1-5 Enter 1 - Addition.. Enter 2 - Subtraction..Enter 3 - Division.. Enter 4 - Multiplication..Enter 5 - Average:"))

var1=int(input("Enter the 1st number: "))

var2=int(input("Enter the 2nd number: "))
if x==1:
    res = var1+var2
    print(res)
if x==2:
    print(var1-var2)
if x==4:
    print(var1*var2)
if x==3:
    print(var1/var2)
if x==5:
    first1=int(input("Enter one more number "))
    second2=int(input("Enter one last number "))
    print((var1+var2+first1+second2)/4)

