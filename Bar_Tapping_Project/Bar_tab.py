class Tab:
    #Menu will be fixed for all tables of bar
    menu ={
        'Wine':5,
        'Beer':3,
        'Soft drink':2,
        'Chicken':10,
        'Mutton':15,
        'Veg':8,
        'Desert':6
    }

    def __init__(self):
        self.total = 0 
        self.items= []
    
    def add_item(self,item):
        self.items.append(item)
        self.total = self.total + self.menu[item]
    
    def print_bill(self,gst):
        gst = self.total * gst /100
        total = self.total + gst
        for item in self.items:
            print(f'{item:15} Rs. {self.menu[item]}')
        
        print(f'{"Amount payble":15} Rs. {total:.2f}')
