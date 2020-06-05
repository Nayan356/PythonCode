# Write a program in Python to perform the following operation:
# ●	If a number is divisible by 3 it should print “Consultadd” as a string
# ●	If a number is divisible by 5 it should print “c” as a string
# ●	If a number is divisible by both 3 and 5 it should print “Consultadd Python Training” as a string.
x=int(input("Enter a number: "))
if x%3==0 and x%5==0 :
    print("Consultadd Python training")
elif x%3 == 0:
    print("Consultadd")
elif x%5 == 0:
        print("c")
else :
    pass