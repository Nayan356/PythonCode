# Write a program that accepts a string as an input from user and calculate the number of digits and letters.
#      Expected output: consul12
#      Letters 6
#      Digits 2

x = input("Enter a string: ")
letters=0
digits=0
for c in x:
    if c.isdigit():
        digits=digits+1
    elif c.isalpha():
        letters=letters+1
    else:
        pass
print("Number of Letters", letters)
print("Number of Digits", digits) 
