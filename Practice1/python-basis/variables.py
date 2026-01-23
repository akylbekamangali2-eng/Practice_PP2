# variables.py
# Practice1 - Python Variables examples

# 1) Simple variables
x = 5
y = "John"
print(x)
print(y)

print("-----")

# 2) Changing variable type
x = 4
x = "Sally"
print(x)

print("-----")

# 3) Casting (convert types)
x = str(3)
y = int(3)
z = float(3)
print(x, y, z)

print("-----")

# 4) Checking types
x = 5
y = "John"
print(type(x))
print(type(y))

print("-----")

# 5) Strings can use ' or "
x = "John"
x = 'John'
print(x)

print("-----")

# 6) Case-sensitive variables
a = 4
A = "Sally"
print(a)
print(A)

print("-----")

# 7) Valid variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"
print(myvar, my_var, _my_var, myVar, MYVAR, myvar2)

print("-----")

# 8) Multiple assignment
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

print("-----")

# 9) One value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

print("-----")

# 10) Unpacking a list
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

print("-----")

# 11) Global variable (read)
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

print("-----")

# 12) Local variable inside function
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()
print("Python is " + x)

print("-----")

# 13) global keyword (change global variable)
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()
print("Python is " + x)