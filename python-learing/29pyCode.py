try:
    txt = open("D:/textfile1.txt", "r")
    try:
        txt.write("This is a test. Normal service will shortly resume!")
    finally:
        print ("Content written to file successfully.Have a nice day.")
        txt.close()
except IOError:
    print ("Error: unable to write the file. Check permissions")
