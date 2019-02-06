# Type method for type
name = "Abid"
age = 22
print(type(name))
print(type(age))
#See the class before type in output
'''
If you know java it is simialr as classes and objects of classes.
If you don't know java don't worry you can still understnad it.
'''
class Names:
    def __init__(self): #like a constructor in Java
        #self is instance of the Object
        self.name = "Abid"
        self.age = 22
        self.height = 5.5
        self.car = "i10"
    
    def display(self): #Like a method in class in Java
        print(self.name,"is",self.age,"yesrs old.")
        print("Person has",self.car,"car")
    
person = Names()
person.display() #You can also use print statement here
print(person.name,"is",person.height,"ft tall")

pserson_two = Names()


class Calculator:
    def addition(x,y):
        print(x+y)
    
    def sub(x,y):
        print(x-y)

    def mul(x,y):
        print(x*y)
    
    def div(x,y):
        print(x/y)

Calculator.addition(75,65) #If the 
Calculator.sub(7,65)    