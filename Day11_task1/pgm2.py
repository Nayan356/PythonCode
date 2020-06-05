# Create a variable of value type complex and swap it with another variable whose value is an integer.
x = 10 #integer variable
y = 20+5j #complex variable
print(type(x))
print(type(y))
x,y=y,x
print(type(x))
print(type(y))
print("x was an integer before but after swap the value is ", x)
print("y was a complex number before but after swap the value is ",y)