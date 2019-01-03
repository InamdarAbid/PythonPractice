name = "Abid"

# def display():
#     name = "Aman"
#     print("Name inside function is",name)

def display():
    global name 
    name = "Aman"
    print("Name inside function is",name)

display()
print("Name outside function is",name)