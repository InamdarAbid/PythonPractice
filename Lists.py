friends = 'Aman,Vishal,Arvind,Kaushal,Sagar'
frList = friends.split(",")
print(frList)
fibo1 = [0,1,1,2,3,5,8,13]
print(fibo1)
print(fibo1[3])
print(fibo1[-3])
print(fibo1[0:4])

fibo2 = [21,34,55]
print(fibo1+fibo2)
fibo1[0] = 9
print(fibo1)
fibo1[0] = 0
fibo = fibo1+fibo2
fibo.append(89)
print(fibo)
print(fibo.pop())
fibo.append(89)
print(fibo)
fibo.remove(89)
print(fibo)
fibo.append(89)
fibo.append(89)
fibo.remove(89)
print(fibo)
# del(fibo,10)
cats = ['mario','delo','vaevo']
cats.append(14)
print(cats)
num = [cats,fibo1,[1,2,3,4]]
print(num[0])
print(num[1][2])

prizes = [5,10,50,100,500]
# double_price = []
# for price in prizes:
#     double_price.append(price * 2)
# print(double_price)

#comprehension method
double_price = [price*2 for price in prizes]
print(double_price)

#Cubing all numbers
nums = [1,2,3,4,5,6,7,8,9,10]
cubed_numbers = [num ** 3 for num in nums if(num ** 3) % 2 == 0]
print(cubed_numbers)

vegs = ['Potato','Tomato','beetroot','lorem','ipsum']
veg_cap =  [veg.upper() for veg in vegs if veg != 'lorem']
print(veg_cap)

i,j,k = 2,3,4
res = [[a,b,c] for a in range(i) for b in range(j) for c in range(k)]
print(res)

a,b = [23,89]
print(a,b) #Unpacking the list