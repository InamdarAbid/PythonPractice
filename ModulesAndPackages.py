#Modules contain the code to be invoked frequenty so we can write it once and import it whenever required.
#Package is collection of modules
# from Classes import Names
# person = Names()
# person.display() #You can also use print statement here
# print(person.name,"is",person.height,"ft tall")

from HumanRace.Human import Names
from HumanRace.calc import human_age,area

person1 = Names("Abid",22,5.5,"i10")
print(human_age(person1.age))
print(area(15))