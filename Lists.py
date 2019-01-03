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
