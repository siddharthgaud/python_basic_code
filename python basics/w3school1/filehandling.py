"""f = open("myfile2.txt","w")
f.write("hey! this is new file called myfile2 and this file is overwrite")
f.close()

f = open("myfile2.txt","r")
f.read()"""

import os
if os.path.exists("myfile3.txt"):
    os.remove("myfile3.txt")
else:
    print("file does not exist")