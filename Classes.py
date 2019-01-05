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
    def __init__(self): #like a constructor 
        self.name = "Abid"
        self.age = 22
        self.height = 5.5
        self.car = "i10"
    
    def display(self):
        print(self.name,"is",self.age,"yesrs old.")
        print("Person has",self.car,"car")
    
person = Names()
person.display() #You can also use print statement here
print(person.name,"is",person.height,"ft tall")

pserson_two = Names()