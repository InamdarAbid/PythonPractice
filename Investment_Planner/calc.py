class Calculations:
    @staticmethod
    def tax_cal(ctc,invest):
        ten = 0
        twinty = 0
        thirty = 0
        ctc -= invest
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

    # @staticmethod
    # def add_invest(self,index,amt):
        