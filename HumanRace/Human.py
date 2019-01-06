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
