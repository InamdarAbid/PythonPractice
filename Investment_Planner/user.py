from calc import Calculations as cal
class Inputs:
    
    global menu
    global mapping
    menu = {
        'PPF':0,
        'EPF':0,
        'SSY':0,
        'ELSS':0,
        'NPS':0
    }

    mapping = {
        1:'PPF',
        2:'EPF',
        3:'SSY',
        4:'ELSS',
        5:'NPS'
    }
    
    def __init__(self):
        self.ctc = 0
        self.base_sal = 0
        self.total_tax = 0
        self.invest = 0
    
    def take_inputs(self):
        self.ctc += int(input("Enter your CTC (in numbers): "))
        pf_opt = input("Have you taken PF facility? (y/n) : ")
        if pf_opt == 'Y' or pf_opt == 'y':
            self.base_sal = int(input("Enter your basic salary : "))
            pf = (12 * 0.125 * self.base_sal)
            if pf > 150000:
                temp = pf - 150000
                self.ctc += temp
                self.invest += 150000
            else:
                self.invest = pf 
            menu['EPF'] = pf
            # print("pf",menu['EPF'])
        else:
            self.base_sal = 0
        self.total_tax = cal.tax_cal(self.ctc,self.invest)
    
    def display_invest(self):
        print("Your current investment is ")
        for key,val in menu.items():
            print(f"{key:10} : Rs. {val}")
    
    @staticmethod
    def display_menu():
        keys = list(menu.keys())
        for i in range(0,5):
            print(f"{(i+1)}. {keys[i]}")
    
    def add_item(self,ch,amt):
        temp = mapping[ch]
        # print(menu[temp])
        if ch == 2:
            print("You cannot add to EPF just opt-in for PF in your company")
            return
        if (ch == 1 or ch == 3) and amt > 150000:
            print("You cannot invest more then 150000 in PPF or SSY")
            return
        if (self.invest + amt) > 150000:
            temp2 = amt + self.invest - 150000
            menu[temp] = amt - temp2
            self.invest = 150000
        else:
            self.invest = amt + self.invest
            menu[temp] = amt