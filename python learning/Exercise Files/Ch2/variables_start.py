# 
# Example file for variables
#

# Declare a variable and initialize it
f = 0
'''print(f)

# # re-declaring the variable works
f = "abd"
print(f)

# # ERROR: variables of different types cannot be combined
print("this is  a sring "+str(123))

# Global vs. local variables in functions'''
def somefunc():
    global f
    f = "abd"
    print(f)

somefunc()
print(f)

del f
print(f)

