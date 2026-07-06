# class ILS:
#     def __init__(self):
#         print("Helllo from constructor!")
#         self.hello()
    
#     def hello(self):
#         print("Hello From Mr class")
        
#     def goodbye(self):
#         print("Will see you!")
        

# ils = ILS()




# class calculator:
#     def __init__(self):
#         print("Welcome to my calculator")
    
#     def add(self,x,y):
#         print(x+y)
        
        
#     def Sub(self,x,y):
#         print(x-y)
        
        
#     def Mul(self,x,y):
#         print(x*y)
        
        
#     def divide(self,x,y):
#         print(x/y)
        
        
# cal = calculator()


#file handling is the process of reading and writing data to a file. In python, there are two types of files text files and binary files. Text files are human-readable files that contain plain text, while binary files contain data in a format that is not human-readable.


#w,a,x,r
#W stands for creating a file
# file= open("zamin.txt","w")
# file.write("Hello i am from nishat and i am studyng in ils")
# file.close()


#r stands for rading a particular file
# file = open("zamin.txt",'r')
# data = file.read()
# print(data)


#a here means append
# file = open('zamin.txt','a')
# file.write(" And  i am also in islamia collage!")
# file.close()

# file = open("zamin.txt",'r')
# d = file.read()
# print(d)

# file = open("zamin.txt",'w')
# file.write(" And my friend is wareed")
# file.close()



# file = open(r"C:\Users\Dell\Desktop\wasiq.txt",'r')
# p = file.read()
# print(p)

# file = open("C:\Users\Dell\Downloads\wareed.txt",'w')
# file.write("Hello i am soura")
# file.close()




# with open("zamin.txt",'r') as f:
#     d = f.read()
#     print(d)



# with open('zamin.txt','a') as f:
#     f.write(" and i live in sgr")


# with open("eshaan.txt",'w') as f:
#     f.write("Hi i am eshaan")



# with open(r"C:\Users\Dell\Desktop\ils.txt",'w') as f:
#     f.write("Hi i am from ils\n")
#     f.write("Hi i am from sgr ")


with open(r"C:\Users\Dell\Desktop\ils.txt",'r') as f:
    p = f.read()
    print(p)


# with open(r"C:\Users\Dell\Desktop\ils.txt", 'a') as f:
#     f.write("\nAnd i live in batmalo")