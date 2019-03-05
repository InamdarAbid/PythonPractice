'''
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

#You can return function as a return type
#This is very useful in Pandas and sklearn libraries

def area_square():
    def volume(side):
        return side ** 3
    return volume

side = input("Enter side of square : ")
result = area_square()
print('Volume of square is',result(int(side)))
'''
#Recursive functions
def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

print(fibo(6))
# Fibonacii series : 1 1 2 3 5 8 13 ...

def funct2():
    print("Inside funct2")
    return 25,5

x,y = funct2()

print(x,"",y)

def list_to_par(a,b,c,d):
    return a+b+c+d

l1 = [7,8,6,11]
# list_to_par(li) #Gives error
print(list_to_par(*l1)) #list unpacking

def updation(*arg):
    arg[0][0] = 15
    arg[0][3] = 77
    print(list_to_par(*arg[0]))
    print(arg)

updation(l1)

def list_com(a,c,*b):
    print(a,c,b)

list_com(10,"Abid","Aman","Ram",14,19)