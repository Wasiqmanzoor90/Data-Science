#Arthmatic
# a = 5
# print(a**3)

# a = 5
# print(a*a*a)


#Relational Operators
#Comparison operator
# a = 10
# b = 12
# print(a==b)

#not equal to
# a = 12
# b =12
# print(a!=b)

#Greater than
# a = 15
# b = 18
# print(a>b)

#less than
# a = 19
# b =10
# print(a<b)

#Greater than equal
# a = 18
# print(a>=18)

#less than equal
# a = 12
# print(a<=12)







#Relational operator
#comparison operator
# a = 10
# b =20
# print(a==b)

# a = 3
# b =3
# print(a!=b)


# a = 12
# print(a<18)


# age = 18
# print(age>=18)


# a = 12
# print(a<=12)


#Assignement Operator
# a = 10
# # a = a+5
# a+=5
# print(a)


#Data-Type is concept which tell us which  type of data a particular value holds
#int -- it holds numerical values
#string -- its holds textual data and that should be in between quotes eg ''
#boolean -- it holds true/false
#float -- it holds decimal value


# a =10
# print(type(a))


# a = '10'
# print(type(a))


# a ='wasiq'
# print(len(a))


# a = 12.34
# print(type(a))

# a = True
# print(type(a))





#Data type is a concept whhich tells us which type of data a particular variable holds
#int -- it holds numerical value
#string --- it holds textual data, string represent between quotes ''
#boolean -- it holds true/false
#float --it holds point value

#int
# a = 10
# print(type(a))

# #string
# name = 'Hello'
# print(type(name))

# #boolean
# c = True
# print(type(c))

# #float
# d = 10.34
# print(type(d))


#attribute means function or features of a particular thing
# a = 'wasiq'
# print(a.capitalize())



# c = 'rubhan'
# print(c.upper())


# d = 'MAHOOR'
# print(d.lower())


#list is a collection which holds multiple items into a single variable, it's ,its ordered, it's indexed, it's mutable(Changable)
#index  is a numerical location of an iten which is present in list

# lt = ['wasiq',12,'Rubhan',56.90,True]
# # # print(lt[2])
# # # print(lt[0])
# # # print(lt[3])
# # #slicing is the process  of gettin an item from one partiuclar range to another
# # # print(lt[1:5])

# print(lt)


# pt = ['hanan','abdul',12,76,True,'sheikh']
# pt[0] = 'himyun'  #here we update
# pt.append('wasiq')  #here we add value
# pt.insert(1,'rubhhan')  #here we add at certin place
# pt.remove('wasiq')  #here we remove by value
# pt.pop(0)  #here we remove by index
# print(pt)

# lt =['wasiq',12,'Rubhan',56.90,True]
# lt[2]='Mahor' #update by index
# lt.append('Khan')  #it add by value
# lt.insert(1,'hanan') #here we by index
# lt.remove('wasiq')  #here we remove by value
# lt.pop(3) #here we remove by index
# print(lt)





#Tuple stores multiple item into single variable. it's ordered, it's indexed, it's im mutable(Un chnageble)
# tp =(21,34,89,'wasiq','ibrahim','khalid')
# tp[1] = 'hanan'
# print(tp[3])

#set stores multiple item in single variable, its un-ordered , its un indexed , idoent allow dupliacte value, its sometimes mutable and sometime im mutable
# ss = {'wasiq','kazin','nazim',12,56,True}
# ss.add('Mahoor')
# ss.remove('wasiq')
# print(ss)


#dictionary stores multiple items in a single variable through the process of key value pairs, it's ordered

# dt ={
#     "name":"wasiq",
#     "Roll-no" : 21,
#     "adress": 'sgr'
# }

# dt['name'] = 'hanan'
# # print(dt['name'])  #here we update by key
# dt['pin-code'] = 190001  #here we add by key

# del dt['name']  #here we remove by key
# print(dt)







#start , stop, step
# lt = ['wasiq','umer',12,'rubhan',True,56.90,'khan','Abdullha']
# print(lt[1:4])
# print(lt[-2])
# print(lt[1:])
# print(lt[:-2])
# print(lt[:6])
# print(lt[::2])

# print(lt[1:])
# print(lt[:-1])

# print(lt[:2])
# print(lt[::-2])
# print(lt[0:8:3])



# a = 10
# print(type(a))


# b = '20'
# print(type(b))


# c = True
# print(type(c))

# d = 20.89
# print(type(d))


# name = 'wasiq'
# print(len(name))
# print(name.capitalize())
# print(name.upper())

# name ='WASIQ'
# print(name.lower())

# name ='wasiq'
# name[0] = 'h'
# print(name)

# a = 10
# b = 25


# c = a # a is empty c holds value 10
# a = b  #  a holds 25  and b is empty
# b = c  #b holds 10

# print(a,b)



# a = 10
# b =16
# a,b = b,a
# print(a,b)







# name = 'wasiq'
# name[0] = 'h'
# print(name)



#Nested list means list within list
# lt = [['wasiq',12,True],['khan','umer',False]]
# lt[0][0] = 'hasik'  #updation
# lt[0].append('Mahoor')
# lt[1].insert(1,'Rubhaan')
# del lt[0][1]
# # print(lt[1][0])
# lt[1].pop(2)
# print(lt)






lt = [   [  ['hanan',12,True,'Abdul'], ['khan','umer' ,45 ]  ],    [ ['Kinza','inaya',101]  ,['Aabid','Gazala',89] ],   [ [47,90,45], ['Maryam','bhat','aahil']  ]  ]


# print(lt[1][0][0])
# print(lt[0][0][3])
# print(lt[2][1][0])
# print(lt[2][0][1])
# print(lt[1][0][1])
# print(lt[2][1][1])
# print(lt[2][0][2])
# print(lt[1][1][1])
# print(lt[0][1][0])

# lt[1][0].append('Rubhaan')
# del lt[0][1][1]
# lt[0][0].insert(1,'Salik')
# lt[0][0][0] = 'Himyun'
# lt[2][1][0] = 'mary'
# lt[1][1].pop(1)
# print(lt)






# dt = {
    
#     "1":{"Name":"wasiq","Roll_no":21},
#     "2":{"Name":"umer","Roll_no":22}
# }


# # dt["1"]={"Name":"ubaid","Roll_no":1}
# dt['1']['Name'] = 'Rubhaan'
# dt['3'] = {"Name":"Hanan","Roll_no":2}
# del dt['1']['Name']
# print(dt)




# dt = {
#     "1":{"name":"wasiq","Roll-no":21,'Adress':'Sgr'},
#     "2":{"name":"ubaid","Roll-no":22,'Adress':'Sgr'},
#     "3":{"name":"umer","Roll-no":23,'Adress':'Sgr'}
    
# }
# dt['1']['name'] = 'hazim'
# dt["4"] = {'name':'Hanan','Roll-no':24,'Adress':'Sgr'}
# del dt['1']['name']
# print(dt)



# dt = {
#     "name":'wasiq',
#     "Roll-no":21,
#     "namee":"wasiq"
# }
# print(dt)


# lt =[[['wasiq','khan',23],[False,'101',8]], [['Madeeha','91',10],['Gazala','Abdul','imaad']],  [[12,89],[102,True,'Rahil']]]
# # print(lt[1][0][0])
# # print(lt[1][1][1])
# # print(lt[0][1][1])
# # print(lt[1][1][0])
# # print(lt[1][0][1])
# # print(lt[0][1][2])


# lt[0][0][0] = 'hanan'
# lt[0][0].append('Himuyun')
# lt[0][1].insert(0,'Mahoor')
# print(lt)



# dt ={
#     1:{"Name":{"fname":"Sheikh" ,"lname":'Wasiq'},"Adress":{"Pincode":190001,"District":'sgr'}},
#     2:{"Name":{"fname":"Malik",'lname':"Rubhan"},"Adress":{"Pincode":190001, "District":"sgr"}},
#     3:{"Name":{"fname":"Mir",'lname':"Madeeha"},"Adress":{"Pincode":190002, "District":"kup"}},
#     4:{"Name":{"fname":"ubaid",'lname':"khan"},"Adress":{"Pincode":192121, "District":"Pulwama"}},
# }

# dt[1]['Name']['lname'] = 'Waqas'
# print(dt[1]['Adress']['Pincode'])
# dt[5] = {"Name":{"fname":"Faizan",'lname':"khan"},"Adress":{"Pincode":190000, "District":"Budgam"}}

# del dt[1]
# print(dt[1])
# print(dt)




#indentation reprsents block of code 
#type-casting means converting one data type to another
#input() by defaults gives string value
# age = int(input("Enter an age:-"))

# if age>18:
#     print("You are elgible")
# else:
#     print("You are not elgible")



# grade = input("Enter you Grade:-")

# if grade == 'A':
#     print("Topper ")
# else:
#     print("Fail")



#when we to check multiple conditions we use concept of elif
# grade = input("Enter your grade:-")

# if grade == 'A':
#     print("Topper")
# elif grade == 'B':
#     print("Good")
# elif grade == 'C':
#     print("Average")
# else:
#     print("Fail")


# n = int(input("Enter an number:-"))

# if n >0:
#     print("Positive number")
# elif n == 0:
#     print("You entered zero")
# else:
#     print("Negative number")


# '19'
# a = int(input("Enter your age:-"))
# print(a>18)

# age = int(input("Enter your age:-"))


# if age>18:
#     print("You are egible")
# else:
#     print("you are not elgible")


# grade = input("Enter you grade:-")
# # if grade == 'A':
# #     print("Topper")
# # else:
# #     print("Fail")


# if grade == 'A':
#     print("Topper")
# elif grade == 'B':
#     print("Good")
# elif grade == 'C':
#     print("Average")
# else:
#     print("Fail")

# '34'

# n = int(input("Enter an number:-"))
# if n >0:
#     print("Positive")
# elif n == 0:
#     print("You entered zero")
# else:
#     print("Negative number")



# age = float(input("Enter you age:-"))
# print(age>18)




# n1 = float(input("Enter an ist number:-"))
# op = input("Enter an operator:-(+,-,/,*,%)")
# n2 = float(input("Enter an second number:-"))


# if op == '+':
#     print(n1+n2)
# elif op == '-':
#     print(n1-n2)
# elif op == '*':
#     print(n1*n2)
# elif op == '/':
#     print(n1/n2)
# elif op == '%':
#     print(n1%n2)
# else:
#     print("Invalid operator")


# n = int(input("Enter an number:-"))
# if n % 2 ==0:
#     print("Even")
# else:
    
#     print("odd number")

# usern = input("Enter you username:-")
# passw = input("Enter an password")

# if usern =='wasiq':
#     if passw =='1234':
#         print("Login sucessfull")
#     else:
#         print("invalid password")
# else:
#     print("Invalid username") 
    
    




# age  = int(input("Enter an number:-"))
# if age>18:
#     print("You are elgible")


#23.56 float
#23 int 

#int ---float 
#float ---int 23.56--


# a = float(input("Entera number:-"))
# print(a)



#And means both the condition should be true
#or means one of the conitions should be true
# b_age = int(input("Enter your age:-"))
# g_age = int(input("Enter you age"))


# if b_age>21 or g_age>18:
#     print("You are welcome")
# else:
#     print("You are not allowed")


# print("My nam e is wasiq")
# print("My nam e is wasiq")
# print("My nam e is wasiq")
# print("My nam e is wasiq")
# print("My nam e is wasiq")


#Loop is a program that runs multiple time until met specific condition
#i is a temporary variable 
#i have a default value 0

#i = 0
#i=i+1
#i=i+1
#i=i+1
# for i in range(10):
#     print("My name is wasiq")#0 1 ,2 ,3,.......,9
    
    
    
# for i in range(1,20,2):
#     print(i)


# tab = int(input("Enter an number:-"))

# for i in range(1,11):
#     res = tab*i
#     print(tab,'x',i,'=',res)
   

# a = float(input("Enter an number:-"))
# print(a)


#string = 23  int to float 23.0
#int 23 #float to int 23.56   23
#float 23.0


#break stops the current number iteration
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
    
    
#continue skips curent number of iteration

# for i in range(10):
#     if i == 6:
#         continue
#     print(i)
    


# lt = ['wasiq','abdul',121,34,True,420]



# for i in lt:
#     if i == 121:
#         break
#     print(i)



# dt = {
#     "name":'wasiq',
#     "roll-no":21,
#     "pincode":190001
# }


# for key,value in dt.items():
#     print(key,':-',value)





# lt =[12,45,90,34,91,54,8,2,101,30]

# x = int(input("Enter an number"))
# flag = 0
# for num in lt:
#     if num == x:
#         flag = 1
        
# if flag == 0:
#     print(x,'is not in list')
# else:
#     print(x,'is in list')


#11
# 2,4,5,6,7,8,9,10


    
#prime 11   1 and 11



# #7
# #6
# n = int(input("Enter an number:-"))

# if n <=1:
#     print("Not Prime")
# else:
#     #2 to 6
#     #2to 5
#     for i in range(2,n):
#         #7%2 ==0
#         #7%3==0
#         #7%4 ==0
#         #7%5 ==0
#         #7%6 ==0
#         #6%2 ==0
#         if n%i==0:
#             print("Not Prime")
#             break
#     else:
#         print("Prime number")
            
            


# #hello
# #mom

# while True:
#     word = input("Enter an word:-")
#     rev =''


#     for ch in word:
#         #'' = h + ''
#         #h = e + h
#         #eh= l + eh = leh
#         #leh = l+leh =lleh
#         #lleh = o + lleh = olleh
        
        
#         #'' = m+'' = m
#         #m = o +m = om
#         #om = m +om = mom
#         rev = ch+rev
        
#     if rev == word:
#         print('Palindrome')
#     else:
#         print("Not Palindrome")
#     choice = input("Enter yes to repeat:-")
#     if choice != 'yes':
#         break




# n = input("Enter an word:-")
# word = n[::-1]

# if n == word:
#     print("Palindrome")
# else:
#     print("Not Palindrome")


# n =5
# for i in range(n, 0,-1):
#     print('*'*i)



# for i in range(5):
#     for j in range(3):
#         print(j)


# for i in range(5):
#     print()
#     for j in range(3):
#         print("Hello")


#Exception handling in Python is a mechanism used to manage runtime errors gracefully, preventing your program from crashing abruptly

# try:
#     a = 10
#     b =0
#     print(a/b)
# except ZeroDivisionError:
#     print("Cant divide by zero")


# try:
#     a = 'wasiq'
#     a.append('a')
#     print(a)
# except AttributeError:
#     print("string doesn't have this feature")

# try:
#     age = 13
#     if age>18:
#     print("You are elgible")
#     else:
#      print("You are not")
# except IndentationError:
#     print("Indentation is wrong")

# try:
#     lt =['wasiq',12]
#     print(lt[4])
# except IndexError:
#     print("There is noe specific index")

# try:
#     a = 'wasiq'
#     b = 10
#     print(a+b)
# except TypeError:
#     print("cant add string and integer")
    
# try:   
#     a = int(input("Enter an number"))
#     print(a)
# except ValueError:
#     print("cant convert word to numerical value")

# try:
#     a ='wasiq'
#     print(a)
# except SyntaxError:
#     print("ok")

# try:
#     print(a)
# except NameError:
#     print("This thing doesnt exist")





# for i in range(10)

#in while loop we don't know the current number of iterations on the other hand in for loop
# we know the current number of iterations already
# i = 0
# while i <30:
#     i = int(input("Enter an number:-"))
#     print(i)




# while True:
#     n = int(input("Enter an number:-"))
#     if n % 2==0:
#         print("Even number")
#     else:
#         print("Odd number")
#     ch = input("Enter(yes/no) to repeat:-")
#     if ch != 'yes':
#         break




#funtion is a block of code which is used to perform a specific task, it can be called multiple times in a program
#argument pass means passing a value from function where it called to real function
# def add(x,y):
#     print(x+y)



# a = int(input("Enter an number:-"))
# b=int(input("Enter an number:-"))
# add(a,b)




# def sq(x):
#     print(x*x)
    
# sq(3)



# def sub(a,b):
#     return a-b

# s = sub(10,2)
# print(s)





# def work():
#     for i in range(10):
#         print(i)

# work()


# def add(x,y):
#     return x+y

# add(10,12)


#Lambda function is anomnys function and basically used for smaller tasks!
# a = lambda x,y: x+y

# print(a(12,4))


# sq = lambda x: x*x

# n =int(input("Enter an number:-"))
# print(sq(n))


# pos = lambda x: 'Negative' if x<0 else 'Positive'


# n =int(input("Enter an number:-"))
# print(pos(n))


# evenodd = lambda x: 'even' if x%2==0 else 'odd'

# print(evenodd(4))



# lt = ['12','45','67','89','101']
# tp = list(map(int,lt)) 
# print(tp)



# names =['BOB','ALICE','KEVIN','ABDUL','KHAN']

# n = list(map(str.lower,names))
# print(n)


# num = [2,4,6,8,10,12]
# sq = list(map(lambda x: x*x,num))
# print(sq)



# num = [-21,-56,34,67,-89,67-11,-1]
# neg = list(filter(lambda x: x<0,num))
# print(neg)


# num = [2,3,4,5,6,7,8,9,10]
# n = list(filter(lambda x: x%2==0,num))
# print(n)