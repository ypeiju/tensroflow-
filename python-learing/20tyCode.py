text1="Daniel Hannah Emma"
names=text1.split(" ")
text2="January,February,March,April,May,June"
months=text2.split(",")

name=list("David")
name=list(name)

alphabet="".join(["a","b","c","d","e"])

name="".join(name)

list=["Conan", "raised", "his", "mighty", "sword","and", "struck", "the", "demon"]
text=" ".join(list)


colours=["Red", "Green", "Blue"]
col=",".join(colours)

title="conan the cimmerian"
title.capitalize()
title.title()

message="Have a nice day"

name="Conan"
print("The barbarian hero of the Hyborian Age is:{}".format(name))
name="Conan"
place="Cimmeria"
print("{} hailed from the North, in a cold land known as {}".format(name, place))

number=10000
print("{} of {} was a skilled mercenary,and thief too. He once stole {} gold from a merchant.".format(name, place, number))

numbers=1, 3, 45, 567546, 3425346345
print("Some numbers: {}, {}, {}, {}, {}".format(*numbers))


numbers=1, 4, 7, 9
print("More numbers: {3}, {0}, {2},{1}.".format(*numbers))

characters=["Conan", "Belit", "Valeria",19, 27, 20]
print ("{0} is {3} years old. Whereas {1} is {4}years old.".format(*characters))

name=input("What’s your name? ")
print("Hello {}.".format(name))
lname=list(name)
print("The first letter of your name is a {0}".format(*lname))
