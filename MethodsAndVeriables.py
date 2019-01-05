class Names:
    species = "human"
    def __init__(self,name,age,height,car): #like a constructor in Java
        #self is instance of the Object
        self.name = name    #Self.name is a scope limited to init finction. And name on RHS is passed function. This is same for all parameters passed. We can use different parameter names.
        self.age = age
        self.height = height
        self.car = car
    
    def display(self): #Like a method in class in Java
        print(self.name,"is",self.age,"yesrs old.")
        print("Person has",self.car,"car")
    
    #Class methods
    @classmethod
    def common(cls_mthd):
        return f"All humans are {cls_mthd.species}"

    @staticmethod
    def run(speed='10 mph'):
        return f'This human can run at {speed}'

person1 = Names("Abid",22,5.5,"i10")

#Its class level attribute
print(Names.species)
print(person1.species)

#Class methods are accessible at Class level and instance 
print(person1.common())
print(Names.run())
print(person1.run("50 mph"))