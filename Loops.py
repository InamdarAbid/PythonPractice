#for loops
for i in range(5):
    print(i)

for i in range(0,5):
    if i % 2 == 0:
        print("Even")
    else:
        print("Odd")

friends = ['Dev','Rant','Abid','Aman','Rita']

#Method 1 for ranges
for friend in friends:
    print(friend)

#Mehtod 2 for ranges using len method 
for friend in range(len(friends)):
    print(friend)

for friend in friends:
    if friend == 'Abid':
        print(f'{friend} is main legend')
    else:
        print(f'{friend} is also a legend')

#while loops

n = int(input("Enter a number : "))
i = 0
''' 
Following commented code produce infinite loop 
while i < n:
    print(i)
'''

while i < n:
    print(i)
    i+=1 #Increment as per your requirements replace 1 by any number

#break 
i = 0
while i < n:
    if i > 10:
        break
    else:
        print(i)
    i+=1