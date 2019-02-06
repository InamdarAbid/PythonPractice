#Writing to a file
output = "Text to be wtitten to the file. \nNew line text."

save = open('SampleFile.txt','w')
save.write(output)
save.close()

#Append 
append = '\nSome new text'

save = open('SampleFile.txt','a')
save.write(append)
save.close()

#Read
txt = open('SampleFile.txt','r').read()
print(txt)
xtx = open('SampleFile.txt','r').readlines() #Will return list
print(xtx)