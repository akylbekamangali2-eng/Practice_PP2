#if_statement the basic
a=111
b=222
if (a>b):
    print("a is more than b")
if(b>a):
    print("b is more than a")
if(a==b):
    print("a is equal to b")
#basic example
age=int(input("Enter your age "))
if age>=18:
    print("adult")
if age<18:
    print("child")

#finding the abs value
number=int(input())
if number<0:
    number=(-number)
print(number)
