#
# Example file for working with date information
#
from datetime import date
from datetime import time
from datetime import datetime


def main():
  ## DATE OBJECTS
  # Get today's date from the simple today() method from the date class
 """"today = date.today()
  print("today date is ",today)

  # print out the date's individual components
  print("date components",today.day,today.month,today.year)

  # retrieve today's weekday (0=Monday, 6=Sunday)
  print("today week day number:" ,today.weekday())
  days =['mon','tue','wednesday','thu','fri','sat','sun']
  print("which is a:" ,days[today.weekday()])"""
  
  ## DATETIME OBJECTS
  # Get today's date from the datetime class
today = datetime.time(datetime.now())
print(today)

today = datetime.time
print(today)


  # Get the current time


  
if __name__ == "__main__":
  main();
  