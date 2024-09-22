x="Awesome"     #Global variable
def myfunc():
    global x     # global variable name
    x="Fantastic"    # changed the value of the global variable
myfunc()
print("Python is "+x)