class Names:
    def __init__(self,name,age,height,car): #like a constructor in Java
        #self is instance of the Object
        self.name = name    #Self.name is a scope limited to init finction. And name on RHS is passed function. This is same for all parameters passed. We can use different parameter names.
        self.age = age
        self.height = height
        self.car = car
    
    def display(self): #Like a method in class in Java
        print(self.name,"is",self.age,"yesrs old.")
        print("Person has",self.car,"car")
    
person1 = Names("Abid",22,5.5,"i10")
person1.display() #You can also use print statement here
print(person1.name,"is",person1.height,"ft tall")

person2 = Names("Aman",20,6.2,"BMW")
person2.display()