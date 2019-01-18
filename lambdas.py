nums = [1,2,3,4,5,6]
#Treditional method of map
# def square(n):
#     return n **2

print(list(map(lambda n:n**2,nums)))

funct = lambda r:3.14* r **2

rad = int(input("Enter the radius of circle : "))
print(funct(rad))

funct = lambda x,y:x*y

x = int(input("Enter length of rectangle : "))
y = int(input("Enter length of rectangle : "))
print(funct(x,y))

#Return a lambda function
def function1(a):
    return lambda b,c:b**a / c

#Here temp is a lambda function which takes two arguments and return a value
temp = function1(3)
print(temp(5,10))
#In the above example a = 3, b = 5 and c = 10 so it will be executed as 5 ^ 3 / 10 = 125/10 = 12.5