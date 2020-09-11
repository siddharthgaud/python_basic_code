#f = open("textfilet.txt","w+")
#f = open("textfilet.txt","a")
'''for i in range(10):
    f.write("this is line " +str(i) +"\r\n")
f.close()'''

f = open("textfilet.txt","r")
if f.mode =="r":
    #contents = f.read()
    #print(contents)

    fl = f.readline()
    for x in fl:
         print(x)