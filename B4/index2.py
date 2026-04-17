#file handling is a process of storing data in a file and retrieving data from a file.
#file handling is done using the built-in functions in python.

#r,w,a,x are the modes of file handling in python.

#w represent writing in a partiuclar file
# file = open("file.txt","w") #open a file in write mode
# file.write("Hello World") #write data to the file
# file.close() #close the file

# #r represents reading a particular file
# file = open("file.txt",'r')
# data = file.read()
# print(data)
# file.close()


# file = open('file.txt','a')
# file.write("I'm from internet")
# file.close()

# file = open("file.txt",'w')
# file.write("And my name is Aadil")
# file.close()


#Here we are handling external files
file = open(r'C:\Users\Dell\Desktop\exam.txt','r')
data = file.read()
print(data)