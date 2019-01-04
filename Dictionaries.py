#initialize
food = {"Abid":"Non-Veg","John":"Veg","Shravan":"Jain","Rita":"Veg"} 
print(food)

#Another way of initialisation
person_info = dict(name='Abid',age = 22,height='5.5ft')
print(person_info)

print(food["John"])
print(food["Rita"])
# print(food["Aman"]) key error Aman not in dictionary
# key in dictionay to check if key exist
print("Abid" in food)
print("Aman" in food)

list1 = list(food.keys())
print(food.keys())
print(list1)
list2 = list(food.values())
print(list2)

#Count the number of values in list
print(list2.count("Veg"))
print(list2.count("veggi"))
#Add new element
food["Aman"] = "Veg"
print(food)

def display(dict):
    for key,val in dict.items():
        print(f'I am {key}. I am a {val} person.')

#Take input from user
food_items = {}
while True:
    name = input("Enter your name : ")
    foo = input("Enter food type : ")
    food_items[name] = foo 
    char = input(" Do you want to add more data(y/n) : ")
    if char == 'n':
        break   
    else:
        continue 

display(food_items)