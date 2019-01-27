import time
poem=open("C:/HEX.DAT")

lines=poem.read()
for lines in lines:
    print(lines,end="")
    time.sleep(.15)
    
