# # #Arthmatic Operators
# # #Addition
# # a = 12
# # b =11
# # c = a+b
# # print(c)


# # c = 91
# # d = 1
# # print(c-d)


# # e = 4
# # f = 7
# # print(e*f)


# # g = 10
# # h = 2
# # print(g/h)


# # #Modlues means when we want to find reminder
# # i = 10
# # j = 2
# # print(i%j)

# # p = 21
# # l = 2
# # print(p%l)



# #comparison operators

# a  = 10
# b = 18
# print(a==b)


# c = 14
# d = 14
# print(c==d)


# e = 32
# f = 19
# print(e!=f)

# #Greater than operstor
# age = 17
# print(age>18)

# #less thn operator
# age = 17
# # print(age<18)

# #Greater than equal to
# age  = 18
# print(age>=18)

# #less than equal to
# age = 18
# print(age<=18)


#aasignment operators
# a = 12

# b = 20
# b = b+3
# b+=3
# # print(b)

# c = 13
# c = c-3
# # print(c)

# d = 4
# # d = d*4
# d*=4
# print(d)


# e  = 10
# # e = e/2
# e/=2
# # print(e)

# f = 10
# # f = f%2
# f%=2
# # print(f)



# # arthmatic operator
# #exponent
# a = 5
# print(a**3)

# #floor division
# b = 10
# print(b//3)


#Data type tell us which type of data a variable holds
#int :- int holds numerical value
#float :- it holds decimael value
#string :- it holds character or we can say text value  ''
#bool :- boolean holds true/ false value


# jp = 10
# print(type(jp))


# na = 'wasiq'
# print(type(na))

# num = '10'
# print(type(num))

# n1 = 10.67
# print(type(n1))

# cp = True
# print(type(cp))


# a = 12
# b = 13
# print(a==b)



# name = 'wasiq'
# print(name.upper())

# b = 'EHSAAN'
# print(b.lower())


# name = input('Enter you name:-')#taha
# age = input("Enter your age:-")
# print(name)
# print(age)

# np = input('Enter your name:-')
# age = input("Enter your age:-")
# print(np)
# print(age)



#list means when we store multiple items/values in single variable,its ordered,it's indexed,it's changeble(mutable)
#index is numerical location of a item presented in the list
# lt = ['wasiq',12,90,'ehsaan','wareed',10.89,True]
# lt[3]='zeeshan'  #here we update the list
# lt.append('Taha') #here we simply add
# lt.insert(1,'Zamin') #here we add value by index 
# print(lt[1])







# dt = ['ehsaan','wasiq',12,56,90,87,True]
# # print(dt[1])
# # print(dt[5])
# # print(dt[6])

# dt[1]='wareed'  #here we update the existing value
# dt.append("Musaib")  #here we add without index
# dt.insert(2,'zamin') #here we add value by index
# dt.remove('ehsaan')  #here it removes by value
# dt.pop(2)  #here it removes by index
# print(len(dt))  #here it gives use total  umber of items in a particular list
# print(type(dt)) #here it tells use which of variable it is
# # print(dt)




#tuple stores multiple items into a single valriable,it's ordered,it's indexed,it's im mutable(un-changeble)
# tp=('Hanan','Khan',12,87.90,True,'khan')
# # print(type(tp))
# # print(len(tp))
# # print(tp[0])
# print(tp)



# #set dores multiple items into single variable, it's un-ordered, it's un-indexed, it doesn't allow duplicate value, sometimes it's mutable and sometimes it's imutable
# st = {'wasiq','Abdul',12,65,90.67,True,'wasiq'}

# st.remove('Abdul')
# print(st)



# #dictionary stores multiple item into single variable, it stores data in the form of key-value pairs
# #its orders, it un indexed, it's mutable, it doesnt' allow duplicate keys but duplicate values
# dt ={
# "Name":"Taha",
# "Roll-no":22 ,
# "Adress":"Sgr" ,
# "local-adress": "Sgr"
# }
# dt['Name'] = "Eshaan" #here we update data through key name
# dt['School']='ils'  #here we add data through ckey name
# del dt['Roll-no']  #here we delete data
# print(len(dt))
# print(type(dt))
# print(dt)















# # a = 12
# # b = 45
# # print(a==b)


# # c = 13
# # d = 11
# # print(c!=d)


# # x = 13
# # print(x<10)


# #greater than equal to
# age = 18
# print(age<=18)






#index is a numerical location of item in particular variable
#list stores multiple items into single variable, its ordered , its indexed
# lt = [21,'wasiq',11,'khan']
# print(lt)






# a = 10
# b=12
# print(a==b)


# c = 23
# d = 19
# print(c!=d)


# a = 18
# print(a>12)

# k = 15
# print(k<18)


# age = 18
# print(age>=18)

# age = 17
# print(age<=17)



# a = 20
# # a = a+3
# a+=3
# print(a)


# a = 13
# a-=3
# print(a)





# #index is numerical location of items presented in particular variable
# #list store multiple items or value in a single variable, it's orddered, its indexed
# lt =['wasiq',12,34.67,True,'ehssan','khan','alim',23,'Taha',False]
# lt[4]='Malik' #here we update through index
# lt.remove('Taha') #here we remove by value
# lt.pop(3) #here we remove by index
# lt.append('arfat') #here we add by value
# lt.insert(5,'ubaid') #here we add by index

# print(lt)





# #nested list
# lt = [['Amir','Abdul',12,78,91],   ['Khan','Amina',True,89],    ['ubi','kumi',34,65,True]]
# # print(lt[1][1])
# # print(lt[2][1])
# # print(lt[0][1])
# # print(lt[1][2])
# # print(lt[2][0])
# lt[2][1]='zainab'  #here we update
# lt.append('wasiq')

# lt[1].insert(1,'Taha') #here we add by index
# del lt [0][1]  #here we delete
# print(len(lt))
# print(lt)



# lt = [ [['Amir','Malik',12,67.89] ,['Umaid','Ubi',2,True]],  [[False,89.90],  ['siyab','maryam','aina']]  ]


# lt[0][1][0] = 'ubaid'
# lt[1][0].insert(0,'wareed')
# lt[0][1].insert(0,'Taha')
# del lt[0][1][1]
# lt[0].append('wasiq')
# print(lt)

# print(lt[0][1][0])
# print(lt[1][1][0])
# print(lt[0][1][1])
# print(lt[0][0][1])
# print(lt[0][0][3])
# print(lt[1][1][2])
# print(lt[1][0][0])


# print(lt[1][0][1])
# print(lt[0][0][0])
# print(lt[1][1][0])
# print(lt[0][1][2])





# dt ={
    
#     "name":{"FirstName":"Shk","Lastname":"Wasiq"},
#     "Adress":{"Pincode":190001,'Local-Adress':'Maisuma'}
    
# }

# dt["Adress"]['Local-Adress']= 'Sonwar'  #here we update
# dt['name']={'FirstName':'Taha','Lastname':"Sofi"} #here we are updating whole
# dt["name"]["MiddleName"] = 'Ahmad' #here we add internally
# dt["Contact"]={"code":92,"phn-no":9797854644} #here we add contact key
# del dt["Adress"]['Pincode'] #here we delete an individual
# print(len(dt))
# print(dt)
# # print(dt['name']['Lastname'])



# dt={
#     1:{"name":{'fName':"Eshaan",'lName':"Khan"},'adress':{"pin-code":190001,'LAdress':"Batmalo"}},
#     2:{"name":{"fName":"Gazala","lName":"Malik"},"adress":{"Pin-code":190002,'LAress':"Maisuma"}}
# }
# print(len(dt[1]['name']['fName']))
# dt[2]['name']={'fName':"Wasiq",'lName':"Manzoor"}
# dt[1]['name']['fName'] = 'Murtaza'
# dt[3]={"name":{"fName":"Taha","lName":"sofi"},"adress":{"Pin-code":190002,'LAress':"Soura"}}# here we add 3rd key

# print(dt[1]['name']['fName'])
# print(dt[2])
# print(dt[3])




# pt={
    
#     1:{"Name":{"first":"Wareed","Last":'Sofi'},"Class":{"Section":'A',"Roll-no":19}},
#     2:{"Name":{"first":"taha","Last":'Sofi'},"Class":{"Section":'B',"Roll-no":20}},
# }

# pt[1]['Name']["first"] = 'Hazik' #here we update

# pt[3]={"Name":{"first":"Shk","Last":'Wasiq'},"Class":{"Section":'C',"Roll-no":23}},
# del pt[1]
# print(pt[2]['Class']['Section'])
# print(pt)







#indentation is a block of code


# grade = input("Enter an grade:-")
# if grade=='A':
#     print("Pass")
# else:
#     print("Fail")

#ttt
#oki
# grade = input("Enter your grade:-")

# if grade == 'A':
#     print("Tooper")
# elif grade =='B':
#     print("Good")
# elif grade =='C':
#     print("Average")
# else:
#     print("Fail")



#Type-casting means when we convert one data type into anaother
# age = float(input("Enter an age;:-"))
# if age >21:
#     print("Youy can go to canada")
# else:
#     print("You cannot go")
    
    

# zage = int(input("Enter an age:-"))
# wage = int(input("Enter an age:-"))

#And operataot simply means both the conditions should be true
# if zage >21 and wage>31:
#     print("You can go")
# else:
#     print("You cannot")
    
# #Or operator means one of the condition should be trur
# if zage >21 or wage>21:
#     print("You can go")
# else:
#     print("You cannot")


#positive, negative and zero number

# num = int(input("Enter an number:-"))
# if num > 0:
#     print("Postive number")
# elif num == 0:
#     print("You entered zero")
# else:
#     print("Negative number")


#odd and even number

# n2 = int(input("Enter an number:-"))

# if n2 % 2 ==0:
#     print("Even number")
# else:
#     print("Odd number")

#try - except is a method to handle error gracefully
# try:
#     n1 = float(input("Enter ist number:-"))
#     op = input("Enter an operator(+,-,*,/)")
#     n2 = float(input("Enter 2nd number:-"))

#     if op == '+':
#         print(n1+n2)
#     elif op == '-':
#         print(n1-n2)
#     elif op == '*':
#         print(n1*n2)
#     elif op == '/':
#         print(n1/n2)
#     else:
#         print("Inavlid operator")

# except ZeroDivisionError:
#     print("Can't divide by zero")


# username = input("Enter your name:-")
# password = input("Enter your password:-")

# if username == 'Wasiq':
#     if password == '12397':
#         print("Login sucessfull")
#     else:
#         print("Invalid password")
# else:
#     print("Invalid username")


#0+1 = 1+1 = 2
#i = 10
#loop is a method that runs multiple times untill it met a specific condition or we can say the condition should be true
#i is temporary variable and its starts by default from 0
#range tell us from where we have to start and to end and its also how many steps we skip
# for i in range(1,20,2):
#     print(i) 

       
# for i in range (10):
#     print(i,':',"My name is wasiq")


# for i in range(20):
#     if i % 2 ==0:
#         print(i)


#7
# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#     res = tab * i
#     print(tab,'x',i,'=',res)
    
    

# lt = ['wasiq','aimnan','hello',12,34,98,True]


# for bt in lt:
#     print(bt)



# dt={
#     "name":"zamin",
#     "Roll":23,
#     "Adress":"Sgr"
        
# }
# for k,v in dt.items():
#     print(k,':-',v)



# num=[23,65,98,101,29,51,101]
# flag = 0
# x = int(input("Enter an number:-"))

# for numsss in num:
#     if x == numsss:
#         flag=1
    
# if flag ==1:
#     print(x,"is in the list")
# else:
#     print(x,"is not in the list")
    
    
# a = 10
# b = 19

# c = a
# a = b
# b=c
# print(a,b)


# a = 32
# b=16

# a,b = b,a
# print(a,b)



#6
#7
#8
# while True:
#     n = int(input("Enter an number:-"))
#     if n <=1:
#         print("Not Prime")
#     else:
#         for i in range(2,n):  #2 : 6

#             if n % i==0:
#                 print(n,"is not Prime number")
#                 break
                
#         else:
#             print("prime Number")
#         choice = input("Do you want to continue? (y/n):-")
#         if choice != 'y':
#             break



# #hello
#  #mom
# word  = input("Enter an word:-")
# rev = ""


# for ch in word:
#     #"" = h+"" = h
#     #h = e+h = eh
#     #eh = l +eh = leh
#     #leh = l leh = lleh
#     #lleh = o +lleh = olleh 
    
    
#     #"" = m + "" = m
#     #m =o +m = om
#     #om = m +om = mom
#     rev = ch+rev
#     #olleh = hello
#     #mom = mom
# if rev == word:
#     print("Palindrome")
# else:
#     print("Not Palimdrome")






# lt = ['wasiq','taha','hanan',121,90]
# print(lt[1:5])
# print(lt[-2])
# print(lt[2:])
# print(lt[:2])


  
# i = 0

# while i< 30:
#     i = int(input("Enter an number:-"))
#     print(i)




# for i in range(10)


# while True:
#     x = int(input("Enter an number:-"))
#     if x % 2==0:
#         print("Even number")
#     else:
#         print("odd number")
        
#     ch = input("Enter y to repeat:-")
#     if ch != 'y':
#         break





# try - except is a method to handle error gracefully
# while True:
#     try:
#         n1 = float(input("Enter ist number:-"))
#         op = input("Enter an operator(+,-,*,/)")
#         n2 = float(input("Enter 2nd number:-"))

#         if op == '+':
#             print(n1+n2)
#         elif op == '-':
#             print(n1-n2)
#         elif op == '*':
#             print(n1*n2)
#         elif op == '/':
#             print(n1/n2)
#         else:
#             print("Inavlid operator")

#     except ZeroDivisionError:
#         print("Can't divide by zero")
#     cht = input("Enter y to repeat:-")
#     if cht!= 'y':
#         break




#funtion is block of code! its reusable, it keeps our code in orginsed  way, it only run when get called
#Argument Paases is a method when we pass a value from function where its called to it real function
# def add(x,y):
#     return x+y
    




# #15
# a = int(input("Enter an number:-"))
# #5
# b = int(input("Enter an number:-"))

# print(add(a,b))





# def repeat():
#     for i in range(10):
#         print("My name is wasiq")
        
# repeat()



# def evenodd(n):
#     if n % 2==0:
#         print("Even number")
#     else:
#         print("odd number")





# x = int(input("Enter an number"))
# evenodd(x)





# def evenodd():
#     x = int(input("Enter an number"))
#     if x % 2==0:
#         print("Even number")
#     else:
#         print("odd number")



# evenodd()



# def sq(x):
#     return x*x



# n = int(input("Enter an number:-"))
# print(sq(n))



# def posneg():
#     while True:
#         x = int(input("Enter number:-"))
#         if x> 0:
#             print("Positive number")
#         elif x == 0:
#             print("zero")
#         else:
#             print("Negative")
#         cht = input("Enter y to repeat:-")
#         if cht!= 'y':
#             break


# posneg()

# from ok import evenodd, pal


# n = int(input("Enter an number:-"))
# evenodd(n)

# pal()



    #lambda function is a small anonymous function which is used to small tasks
        
# add = lambda x,y:  x+y

# n1 = int(input("Enter an number:-"))
# n2 = int(input("Enter an number:-"))
# print(add(n1,n2))


#even odd with the help of lambda

# evenodd = lambda x: "even" if x%2==0 else "odd"
# n = int(input("Enter an number:-"))
# print(evenodd(n))


# num = [2,3,4,5,6]

# sq = tuple(map(lambda x: x*x,num))
# print(sq)




# num = ['11','23','90','64','91']
# numerical = list(map(int,num))
# print(type(numerical))

# names= ['BOB','ALICE','ZAMIN','ESHAAN','KHAN']
# sq = list(map(str.lower,names))
# print(sq)

# names=['bob', 'alice', 'zamin', 'eshaan', 'khan']
# sq = list(map(str.upper,names))
# print(sq)


# num =[14,15,16,17,18,19,20,21,23,26]
# sq = list(filter(lambda x: x%2==0,num))
# print(sq)


# num =[-14,15,-16,17,-18,-19,20,-21,23,-26]
# sq = list(filter(lambda x: x>0,num))
# print(sq)


# fruit = ['Kiwi','apple','mango','banana','pineapple']
# sq1 = list(filter(lambda x: len(x)>5,fruit))
# print(sq1)



# names = ['moomin','hanan','khan','murtaza','wareed','zamin','maryam']
# sq = list(filter(lambda x: x.startswith('m'),names))
# print(sq)


# student=[
#     {"name":"wareed","marks":30},
#     {"name":"zamin","marks":80},
#     {"name":"Eshann","marks":90},
#     {"name":"Murtaza","marks":20},
# ]
# sq = list(filter(lambda x: x['marks']>36,student))
# print(sq)



# num =[4,5,6,17,18,19,20,21,23,26]
# sq = list(filter(lambda x: x%2==0 and x>15,num))
# print(sq)





# for i in range(5):  #outerloop
#     for j in range(3):  #innerloop 
#         print(j)
        
# #nested loop mean when we have loop inside a loop
# for i in range(5):
#     print()
#     for j in range(3):
#         print("Hello world")


# num =[2,3,2,4,3,6,7]
# uniq = list(set(num))
# print(uniq)




# num = [21,107,89,2,78,11,69]
# num.sort()
# print(num[-2])



# num = [21,107,89,2,78,11,69]
# num.sort(reverse=True)
# print(num)



#My name is wasiq
# sen = input("Enter an sentence:-")
# word = sen.split() # remove spaces
# print(len(word))



#Object oriented programing language(OOPS) is way of writing your code in more organized and archetecture way
#class is a blueprint which is used to create ral thing or we can say an object
#objet is a real thing that get created from class 

#self is an adress of an object

# class ok:
#     def greeting():
#         print("Hello world")
    
    
#     def goodbye(self):
#         print(self)
#         print("Good bye will meet you")
        
        

# tp = ok()  # object get created from class
# tp.goodbye()


#OOPS have four principal
#encapsulation
#polymorphism
#inheritence
#abstraction



 