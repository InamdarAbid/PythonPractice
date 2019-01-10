#map(function,data)
from random import shuffle
def jumble(data):
    anagram = list(data)
    shuffle(anagram)
    return ''.join(anagram)

list1 = ['Abid','Aman','Vishal','Rita','Varun']
anagrams =[]
print(list(map(jumble,list1)))

#using list comprehension
anagrams = [jumble(word) for word in list1]
print(anagrams)

#Using for loop
anagrams = []
for word in list1:
    anagrams.append(jumble(word))
print(anagrams)