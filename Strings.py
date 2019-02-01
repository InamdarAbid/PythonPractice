print("Hello World")
print('Hello')
print("He's a stupid")

#print('he's a stupid' ) Gives error
print('he\'s a stupid person.') #Escape character

a1 = 'Hello'
#Important for competative where new line output not required
print('hello',end=' ')
print("World I am back")
#Remember arrays are zero based
print(a1[0])
print(a1[3])
print(a1[-1]) #You can traverse backword also
print(a1[0:3]) #3rd index element is not included 
print(a1[-4:-1]) #ell
print(a1[-1:3]) #empty string
print(a1[-1:-3]) #empty string
print(a1[2:-1])
print(a1) #It's unchanged until reassigned
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
string = "goodmorning"
print(string.capitalize()) #Capitalize first lettor of string
print(string.center(1)) #Returns a centered string
print(string.count("hello")) #Returns the number of times a specified value occurs in a string
print(string.encode())  #Returns an encoded version of the string
print(string.endswith("ld")) 
print(string.find("orn")) #Searches the string for a specified value and returns the position of where it was found
print(string.isalnum()) #Returns True if all characters in the string are alphanumeric
print(string.isalpha()) #Returns True if all characters in the string are alphabet
print(string.isdecimal()) #Returns True if all characters in the string are decimals
print(string.isdigit()) #Returns True if all characters in the string are digits
print(string.isidentifier()) #Returns True if the string is an identifier

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)
my_string = "Welcome To My Wolrd"
print(my_string.istitle())
print(my_string.isprintable())