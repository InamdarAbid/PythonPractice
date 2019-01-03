#Function is initialysed with def keyword 
#Function with default parameter set so no error
def display(name='Abid'):
    print("Hello",name)

#Function with and without parameter for fauction default parameter set
display()
display('Aman')

#Function without any parameter and no return value 
def area():
    print("The area of circle is 12 ")

area()

#Function with no retun value and one parameter
def area(redius):
    area = 3.14 * redius ** 2
    print("Area of circle is ", area)

area(13)

#Function with return value
def area(redius):
    area = 3.14 * redius ** 2
    return area

red = int(input("Enter radius of circle : "))
print("Area of circle is ",area(red))

def area(length,bredth):
    return(length*bredth)

#This is also a example of compile time Polymorphism. 
#The area is same mehtod name for all functions which so compiler differenciate between them by the number of parameters and type of parameters
leng,bre = int(input("Enter length of rectangle : ")),int(input("Enter bredth of rectangle : ")) 
print("Area of rectangle is", area(leng,bre))