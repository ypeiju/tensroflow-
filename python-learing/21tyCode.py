name=input("What’s your name? ")
print("Hello {}.".format(name))
lname=list(name)
print("The first letter of your name is a {0}".format(*lname))

names=["Conan", "Belit", "Valeria"]
ages=[25, 21, 22]

print("{0[0]} is {1[0]} years old. Whereas {0[1]} is {1[1]} years old.".format(names, ages))
