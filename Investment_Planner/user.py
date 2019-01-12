class Inputs:    

    def __init__(self):
        self.ctc = 0
        self.base_sal = 0
        self.total_tax = 0
        self.invest = 0
    
    @staticmethod
    def tax_cal(ctc):
        ten = 0
        twinty = 0
        thirty = 0
        if ctc <= 250000:
            print("Your earning is completly TAX FREE ! Just file the income tax return annuly.")
        elif ctc <= 500000:
            ten = ctc - 250000
        elif ctc <= 1000000:
            ten = 250000
            twinty = ctc - 250000
        else:
            ten = 250000
            twinty = 500000
            thirty = ctc - 1000000 
        total_tax = (ten * 0.1) + (twinty * 0.2) + (thirty * 0.3)
        return total_tax
    
    def take_inputs(self):
        self.ctc += int(input("Enter your CTC (in numbers): "))
        pf_opt = input("Have you taken PF facility? (y/n) : ")
        if pf_opt == 'Y' or pf_opt == 'y':
            self.base_sal = int(input("Enter your basic salary : "))
            pf = (12 * 0.125 * self.base_sal)
            if pf > 150000:
                temp = pf - 150000
                pf = 150000
                self.ctc += temp
            self.invest += pf
            self.ctc -= self.invest
        else:
            self.base_sal = 0
        total_tax = Inputs.tax_cal(self.ctc)
        print(f"Your annual due tax is : {total_tax}")
    
    