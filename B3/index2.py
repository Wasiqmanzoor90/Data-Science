# def add(a,b):
#     return print(a+b)






#file  handling is process when we create, read and updata a particular file
#r stand for read
#w stand for write
#a stand for append


#we have created a file
# file = open("File.txt",'w')
# file.write("Hello im from bemina")
# file.close()


# file = open("File.txt",'r')
# data = file.read()
# print(data)
# file.close()




# file = open("File.txt",'a')
# file.write(" and my name is Reeba")
# file.close()





# file = open('File.txt','w')
# file.write("Jasira")
# file.close()

#its new way that was created by python in this the file automatically get closed
# with open('File.txt','r') as f:
#     data = f.read()
#     print(data)
    
    
# with open('ayman.txt','w') as f:
#     f.write("Hello world!")


# with open("ayman.txt",'a') as f:
#     f.write(" and my name is syed aiman")


with open(r"C:\Users\Dell\Desktop\jasira.txt",'w') as f:
    f.write("My name is jasira")
    
    
with open(r"C:\Users\Dell\Desktop\exam.txt",'r') as f:
    data = f.read()
    print(data)