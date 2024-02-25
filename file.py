#file io

file1 = open("kalpesh.txt","wb")
print(file1.mode)
print(file1.name)
file1.write(bytes("write this is to my file ok done this is by me kalpeshs snanse","UTF-8"))
file1.close()