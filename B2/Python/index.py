
# # #int
# # a = 10
# # print(a)

# # #strings

# # b = '10'
# # print(b)

# # #bool
# # c = True
# # print(c)

# # #float
# # d =10.324
# # print(d)

# #Athmatic operation
# #addition
# a = 10
# b = 20
# c = a +b
# print('Addition:-',c)


# #subtraction
# a = 30
# b = 10
# c = a - b
# print('Subtraction',c)


# a =5
# b =3
# c = a * b
# print("Multiplication:", c)

# a =9
# b = 2
# c = a/b
# print("Divide:",c)


# a =10
# b = 2
# c = a%b
# print("Modlus:",c)


# a =5
# b = 3
# c = a ** b
# print("Raise Power:",c)

# a =9
# b = 2
# c = a // b
# print("floor division:",c)


# a = 6
# b = 3
# z =a **b
# print(z)

# a =  -15
# b =4
# z = a // b
# print(z)



#Cpmparison
# == basicaly it compares a with b
# a = 10
# b = 20
# print(a == b)

#> this sign mean if a is greater than b and >= either eqilt to greater than
# a = 20
# b =20
# print(a>=b)

#<= this signs means if a is leass than or equal to b
# a = 50
# b =20
# print(a<=b)

#!= basicaly it shows a is equal to b
# a = 10
# b =10
# print(a != b)


# a = 10
# b = 10
# print(a != b)


#Assigment operator
# a = 20
# a+=10
# a = a+10
# print(a)


# b = 30
# b-=3
# print(b)


# c = 30
# c*=2
# print(c)


# d = 10
# d/=2
# print(d)


# d = 10
# d%=2
# print(d)


# a = 10
# b = 20
# a = b
# b = a
# temp = a
# a = b
# b = temp
# print(b,a)
# a,b =b,a
# print(a,b)


# a = 'wasiq'
# print(a)

# b='ahmad'
# print(b)

# c = 'ehsaan'
# print(c)

#so basically when we have to store multiple items or values in a single variable we use list
#its indexed, here index mean numerical locaion present in the list
#its mutable(changeble)
#its ordered means it have same squesnce

# lost = ['wasiq','ahmad', 'ehsaan',12,12.5,True]
# lost[0]='ayaz' #update
# print(lost)

# a = input('enter your name:-')
# print(a)

# lst = [12,'home',11.5,True,'wasiq',123,'ubaid']
# print(lst)
# print(lst[:4])
# print(lst[3:])
# print(lst[1:4])


# lst = ['wasiq','abdul','ahmad','burhan',12,12.5]
# # lst[1]='abrar' 

# #so basically its finds the length of the list
# print(len(lst))
# #finds which data type it is
# print(type(lst))


# b = 'ubaid'
# print(b[2])
# #so basiclly uperr converts small to capital
# a = 'ahmad'
# print(a.upper())

# #capitab to small
# b = 'WASIQ'
# print(b.lower())


# lst = ['Ahmad',12,34.56,True,'Abdul']
# lst[0]='Abrar'  #update
# lst.append('wasiq') #when we inset without index
# lst.insert(0,'Hanan') #when  we add with index
# lst.remove('Abdul')  #when we remove direct by value
# lst.pop(2) #when we remove by index
# print(lst)

#we can store multiple items in a single variable,its immutable,its indexed,its ordered,its allows duplicate valye
# tple =(12,'abdul','hanan',True,12.45,'abdul')
# # tple[1]='wasiq'
# print(tple)

#set stores multiple value or items in a single variable. its unorderd, its un indexed , it does not allow duplicate value,mutable
# st ={"Ehsan",'Abrar',12,45,78.90,
# "Ehsan"}
# st.add("umer")
# st.remove("Abrar")
# print(st)

#it stores multiple values or items in single variable through process key value pairs, is it ordered, its in ky value, its mutable
# dt = {
#     "name":"monis",
#     "rollno":21,
#     "pincode":190001,
    
# }
# dt["pincode"]=192121  #update
# dt['Gender']='Male'
# dt.pop('rollno')
# print(dt)

# lt = [['wasiq',12,34,56,90,32,'ubaid'],['umer','kazim',34,56,34]]
# lt[0][6]='Ahsaan'  #update in nesting list
# lt.append('ayaz')   #we add without index
# lt[0].insert(3,'Moonis')  #we add with index
# del lt[0][0]  #we remove
# print(lt)

# lst = [[['ubaid',12,89,76],['umer','khubaib',True,90.56]],  [['ayaz',126.89,11],['khan',125,97]],  [['Adeena',11,34.5],[432,90,63,'Ahmad']]]
# # print(lst[2][0][0])
# # print(lst[0][1][1])
# # print(lst[2][1][0])
# # print(lst[1][1][0])
# # print(lst[1][1][2])
# # print(lst[1][0][1])
# # print(lst[0][1][3])
# lst[1][0][0]='wasiq'
# lst[0][1].insert(1,'saliq')
# del lst[1][1][0]
# print(lst)


# dit = {
#     "1":{"name":"wasiq","pincode":190001},
#     "2":{"name":"umer","pincode":190002},
#     "3":{"name":"owais","pincode":190003},
# }

# dit = {
#     "1":{"name":"wasiq","pincode":190001},
#     "2":{"name":"umer","pincode":190002},
#     "3":{"name":"owais","pincode":190003},
# }

# dt ={
    
#     "1":{"Name":{"Firstname":"Abrar","Lastname":"iqbal"},"adress":{"pincode":190001,"city":"ompora"},"country":{"state":"kashmir","district":"Budgam"}},
#     "2":{"Name":{"Firstname":"Moonis","Lastname":"Farooq"},"adress":{"pincode":190002,"city":"harwan"},"country":{"state":"kashmir","district":"srinagra"}},
#     "3":{"Name":{"Firstname":"tufail","Lastname":"Bakshi"},"adress":{"pincode":190003,"city":"mataan"},"country":{"state":"kashmir","district":"anatnag"}},
# }   

# dt["1"]['Name']['Firstname']='Ubaid'  #update
# dt['4']={"Name":{"Firstname":"Ayaz","Lastname":"Parray"},"adress":{"pincode":190003,"city":"harwan"},"country":{"state":"kashmir","district":"srinagra"}},
# del dt["3"]['Name']["Lastname"]
# # print(dt["1"]['Name']['Firstname'])
# # print(dt["1"]['adress']['city'])
# print(dt["3"])

# age = int(input("Enter your age"))
# if (age>18):
#     print("You are elgible")
# else:
#     print("You are not elgible")


# grade = input("Enter your grades")
# if (grade == 'A'):
#     print("Pass")
# else:
#     print("Fail")

# age = int(input("Enter you age:-"))
# if (age>18):
#     print("You are elgible")
# else:
#     print("You are not elgible")

# num = int(input("Enter an number:-"))
# if(num % 2 == 0):
#     print("Its an evem number")
# else:
#     print("Its an odd number")


# grade = input("Enter you grade:-")
# if(grade == 'A'):
#     print("Topper")
# elif(grade =='B'):
#     print("Good Student")
# elif(grade == 'C'):
#     print("Avergae")
# else:
#     print("Fail")

# try:
#     n1 = float(input("Enter ist number:-"))
#     op = input("Enter an operator(+,-,*,/,%)")
#     n2 =  float(input("Enter second number:-"))

#     if(op == '+'):
#         print(n1+n2)
#     elif(op == '-'):
#         print(n1-n2)
#     elif(op == '*'):
#         print(n1*n2)
#     elif(op =='/'):
#         print(n1/n2)
#     elif(op=='%'):
#         print(n1% n2)
#     else:
#         print("Invalid operator")
# except ZeroDivisionError:
#     print("Cant dived by zero")
    
    
# print("My name is Ahmad")
# print("My name is Ahmad")
# print("My name is Ahmad")
# print("My name is Ahmad")
# print("My name is Ahmad")

# for i in range(0,20,2):
#     print(i)

# tab = 3
# for i in range(1,11):
#     res = tab *i
#     print(tab,'x',i,'=',res)


# lst =['Wasiq','Ahmad','Ubaid','Moonis','Ehsaan']
# for names in lst:
#     print(names)
    
# a = 'Ahsaan'
# for y in a:
#     print(y)
    
# dic={

#     'name':'wasiq',
#     "roll-no":12,
#     "adress":190001
# }

# for key,value in dic.items():
#     print(key,':',value)

#break
# for i in range(1,11):
#     if i == 5:
#        break
#     print(i)
    

#Skip the rest of this loop iteration and move to the next one.

    
# for i in range(1,11):
#    if i == 5:
#       break
#    print(i)    


# for i in range(1,11):
#    if i > 5:
#       continue
#    print(i)

   
    

# dico ={
#    "name":"wasiq",
#    "Roll-no":'12',
#    "adress":190001
# }
# for key,value in dico.items():
#    if key == 'Roll-no':
#       continue
#    print(key, ':',value)
   
# lt = [11,'ubaid',45,90,76]
# for l in lt:
#    if l == 'ubaid':
#       continue
#    print(l)


# num =  [11,34,45,89,71,49,61,32,10,90,76]
# flag = 0
# x = int(input("Enter an nmber:-"))
# for nums in num:
#    if nums == x:
#       flag =1
      
# if flag == 1:
#    print(x, 'is in the list')
# else:
#    print(x,'is not in the list')

#9
# n = int(input("Enter an number:-"))
# if (n<=1):
#    print('Not Prime')
# else:
#    for i in range(2,n):
#       if(n%i ==0):
#          print('Not prime Number')
#          break
#    else:
#       print('Prime Number')

#11
# n = int(input("Enter an number:-"))
# if n<=1:
#    print("Not Prime")
# else:
#    for i in range(2,n):
#       if n%i==0:
#          print("Not Prime")
#          break
#    else:
#       print("Prime number")

#Mom
#hello
# word = input("Enter an Word:-")
# rev = ""
# for ch in word:
    #rev = M + ""
    #rev = o + M = OM
    #rev = M + OM = MOM
    
    #rev = h + "" = h
    #rev = e + h = eh
    #rev = l + eh = leh
    #rev = l + leh = lleh
    #rev = o + lleh = olleh
    #olleh
    
    # rev = ch +rev
    #hello = olleh
    #Mom = Mom
# if word == rev:
#     print("Palindrome")
# else:
#     print("Not Palindrome")
    
# word = input("Enter an Word:-")
# rev = ""  #enpty varibale
# for ch in word:  # word int ch
#    rev = ch + rev 
#    #M + ""= M
#     #o + M = OM
#     #M +OM = MOM
    
    
#    #h + "" = h
#    #e + h = eh
#    # l + eh = leh
#    # l +leh = lleh
#    # o + lleh = olleh
 
#  #hello =  olleh  
#  #Mom   = Mom
# if word == rev:
#    print("Palindrome")
# else:
#    print("Not Palindrome")


# for i in range(3): #outer loop
#     print(i)
#     for j in range(3): 
#         print(i)


# for i in range(5):
#     print()
#     for j in range(3):
#         print("Hello",end="  ")

# i = 0
# while i <= 30:
#     i = int(input("Enter an number:-"))
#     print(i)
    
# while True:
#     n = int(input("Enter an number:-"))
#     if n% 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
#     cht = input("Enter yes to repeat")
#     if cht !='yes':
#         print("You are done")
#         break




# def add(n1,n2):
#     print(n1+n2)

# def sub(n1,n2):
#     print(n1-n2,'subtraction')



# a = int(input("Enter ist number:-"))
# b = int(input("Enter second number:-")) 
# add(a,b)
# sub(a,b)

# a = 12
# b= 19
# if(a>18 and b>18):
#     print("Both are elgible")
# else:
#     print("Both are not elgible")
    
# a = 12
# b= 19
# if(a>18 or b>18):
#     print("Both are elgible")
# else:
#     print("Both are not elgible")





#5
# n1 = int(input("Enter an first number:-"))
# #6
# n2 = int(input("Enter an second number"))
# add(n1,n2)
# sub(n1,n2)


#in and operator both condition shoild be true
# a = 19
# b=11
# if(a>18 and b>18):
#     print('you are elgible')
# else:
#     print("You are disqualified")


# #in or operatar at least one condition true
# a = 19
# b=11
# if(a>18 or b>18):
#     print('you are elgible')
# else:
#     print("You are disqualified")



# def evenodd(x):
#     if x % 2 == 0:
#         print("Even Number")
#     else:
#         print("Odd Number")

# n = int(input("Enter an number:-"))
# evenodd(n)

# def table(tb):
#     for i in range(1,11):
#         Res =tb*i
#         print(tb,'x',i,'=',Res)
    
    
# t = int(input("Enter an number:-"))
# table(t)


#its an anomys function that we use for small task
# add = lambda a,b: a+b
# print(add(12,34))


# eveodd = lambda x: 'even' if x % 2 == 0  else'odd'
# n = int(input("Enter an number:-"))
# print(eveodd(n))


#it itterates  the value from list and put it new varible
# num =[2,4,6,9]
# sq =list(map(lambda x: x**2,num))
# print(sq)




# add = lambda a,b: a+b
# print(add(12,23))



# num =[ 2,4,6,8,9]
# sq = list(map(lambda x: x**2,num))
# print(sq)


# num = [2,4,6,78,34]
# sq = list(map(lambda x: x**2,num))
# print(sq)


# nums = ['11','31','23','19','51']
# st = list(map(int,nums))
# print(st)


# names = ['BOB','ALICE','HANNAH','ALIM']
# st = list(map(str.lower,names))
# print(st)


# num = [2,3,4,5,6,7,8,9]
# st = list(filter(lambda x: x % 2 == 0, num))
# print(st)



# nums = [-21,5,-6,11,21,-11,8]
# st = list(filter(lambda x: x>0,nums))
# print(st)


# words = ['apple','banana','kiwi','grape','avocado']
# st = list(filter(lambda x: len(x)>5,words ))
# print(st)


#Object Oriented Programing Language(OOPS)
# Four Pillars Of OOPS
# Encapsulation, Polymorphism, Abstraction, Inheritence

#Today we talk about classes and objects

# class Project:
#     def add():
#         a= 10
#         b=12
#         print(a+b)
        
#     def sub():
#         a= 10
#         b=12
#         print(a-b)
        
# pro = Project    #

# pro.add()
# pro.sub()

# from index1 import chk

# x = int(input("Enter an number"))
# rsd=chk(x)
# print(rsd)



#Polymorphism same function but diffrent behaviour
#self is basically adress od an object


# class Dog:
#     def speak(self):
        
#         print("Dogs Bark!")
   
# class cat:
#     def speak(self):
#         print("Cats Meom")


# d = Dog()
# d.speak()

# c = cat()
# c.speak()




#when we in inherit properties from parent class to child class
# class Animal:
#     def speak(self):
#         print("Animal Speaks")
        
# class Dog(Animal):
#     def bark(self):
#         print("Dog Barks!")
        
# d = Dog()
# d.speak()
# d.bark()

#contructor get runs automatically when the object of the class is created
#it intialize by __init()__


# class Calc:
    
#     def __init__(self):
#         print("Hello im from constructor")
#         self.add(12,13)
#     def add(self,a,b):
#         print(a+b)


# c = Calc()


