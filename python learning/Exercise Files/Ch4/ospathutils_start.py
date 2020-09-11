#
# Example file for working with os.path module
#
import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
  # Print the name of the OS
  print(os.name)


  # Check for item existence and type
  '''print("Item exist :" +str(path.exists("textfilet.txt")))
  print("item is file :" +str(path.isfile("textfilet.txt")))
  print("item is a directory :"+str(path.isdir("textfilet.txt")))'''

  print("item path :" +str(path.realpath("textfilet.txt")))
  print("item path :" + str(path.split(path.realpath("textfilet.txt"))))

  t = time.ctime(path.getmtime("textfilet.txt"))
  print(t)
  print(datetime.datetime.fromtimestamp(path.getmtime("textfilet.txt")))


  td = datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfilet.txt"))
  print("it has been " +str(td) +"since the file was modified")
  print("or," +str(td.total_seconds())+"seconds")


  
  # Work with file paths

  
  # Get the modification time

  
  # Calculate how long ago the item was modified


  
if __name__ == "__main__":
  main()
