raise Exception("warp core breach")
try:
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print(a/b)
except ZeroDivisionError:
print("You have tried to divide by zero!")
else:
print("You didn’t divide by zero. Well done!")
