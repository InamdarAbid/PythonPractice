print("Hello World")
print('Hello')
print("He's a stupid")

#print('he's a stupid' ) Gives error
print('he\'s a stupid') #Escape character

a1 = 'Hello'
#Remember arrays are zero based
print(a1[0])
print(a1[3])
print(a1[-1]) #You can traverse backword also
print(a1[0:3]) #3rd index element is not included 
print(a1[-4:-1]) #ell
print(a1[-1:3]) #empty string
print(a1[-1:-3]) #empty string
print(a1[2:-1])
print(a1) #Its unchanged untill reassigned
a2 = 'world'
a3 = a1 + a2 #String concatination
print(a3)
print(a3 * 2) #If you want to print sting multiple times
a4 = a1 + ' ' + a2
print(a4)

#Some string methods
print(a3.upper())
print(a3.lower())
friends = "Aman,Vishal,Sagar"
print(friends.split(","))
print(len(a3))