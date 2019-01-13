from user import Inputs
from calc import Calculations as cal
print(3*"<$>","Welcome to the Investment plnner",3*"<$>")
print("Let's start")
usr = Inputs()
usr.take_inputs()
print("Your total due tax is :",usr.total_tax)
usr.display_invest()
print("We always provide option of complete tax free investments.")
# usr.invest_input()
if usr.invest < 150000:
    ch = input("You are eligible for investing money. Do you want to invest (y/n)? : ")
    if ch == 'y':
        print("Menu for investment is : ")
        while(True):
            Inputs.display_menu()
            ch1 = int(input("Enter choice for investment and '6' for exit : "))
            if ch1 >= 6:
                break
            amt = int(input("Enter the amount to be invested : "))
            usr.add_item((ch1),amt)
    else:
        print("Thank you for using our system. <3")
usr.total_tax = cal.tax_cal(usr.ctc,usr.invest)
print("Your total due tax is :",usr.total_tax)
usr.display_invest()