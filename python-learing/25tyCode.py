t=open("D:/HEX1.txt","w")

t.write("You awake in a small, square room. A single table stands to one side, there is a locked door in front of you.")
t.close()
t=open("D:/HEX1.txt","a")
t.write("\n")
t.write("You stand and survey your surroundings. On top of the table is some meat, and a cup of water.\n")
t.write("The door is made of solid oak with iron strips. It’s bolted from the outside, locking you in. You are a prisoner!.\n")
t.close()
import math
print("Value of Pi is :",math.pi)
print("\nWriting t a file now...")
Pi=math.pi
t=open("D:/pi.txt","w")
t.write("Value of Pi is:{}".format(Pi))
t.close()
