import time
start_time=time.time()
name=input("Enter login name: ")
endtime=time.time()-start_time
print("Welcome", name, "\d")
print("User:", name, "logged in at", time.strftime("%H:%M"))
print("it took",name,endtime,"to login to their account")
