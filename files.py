# The read function
path = '/storage/emulated/0/python_course/days.txt'
myFile = open(path,'r')
print(myFile.read())
print('\n')
myFile.seek(0)#commes back to the start of the file due to the presence of the first read fxn above
print(myFile.readlines())#myFile.readlines() is set to a list
myFile.seek(0)
print(myFile.readline())#reads just the first line
path2 = '/storage/emulated/0/python_course/read.txt'
fileInput = open(path2, 'r')
print(fileInput.readline()) #reads just the first line
fileInput.seek(0)
print(fileInput.readlines(20))
print('\n')

#The write function
path3= '/storage/emulated/0/python_course/read3.txt'
fileInput = open(path3, 'w')
print(fileInput.write("The content has been updated"))

#The append function
fileInput = open(path2, 'a')
text = fileInput.write(" Programming is fun")
print(text)

fileInput.close()


