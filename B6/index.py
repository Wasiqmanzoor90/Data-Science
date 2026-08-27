#coments



#exponent
# a = 3
# print(a*a*a)


# #flooer division
# x = 9
# y = 2
# print(x//y)


#Relational operator

# a = 12
# b =12
# print(a==b)


# a = 12
# b = 12
# print(a!=b)


# a = 12
# b = 11
# print(a<b)


# age = 18
# print(age>=18)

# age = 12
# print(age<=12)


#Assigment Operator
# a = 20
# a = a+5
# # a+=5
# print(a)


#Data types  tellls which type of data a particulat variable holds
#int-- it holds proper numerical value eg 12
#float --it holds point values eg 12.56
#string -- it holds textual data eg 'wasiq'
#boolean -- it holds tru/false values



# a = "wasiq"
# print(type(a))


# a = 10
# print(type(a))


# b  = 10.6
# print(type(b))

# c =True
# print(type(c))


# a = '10.87'
# print(a)

# a = 'ayat'
# print(a)

# b = 'athar'
# print(b)


#list stores multiple items in a single variable, its hetrogenous, its orderd, its mutable(Changable)
#indexing is a numerical location of an item presented in list
# lt = ['wasiq','madeeha',12,True, 'khan']
# lt[1]='raziya'  #updation
# lt.append('Ayat')  #add by value
# lt.insert(1,'Eshaan')  #add by index
# lt.remove('wasiq') #remove by value
# lt.pop(4)  #remove by index
# print(lt)


lt = ['Arslan','umaid',21,67,90,87.82,11,True,'Abdul','Maryam','Maryam']

# print(lt[2])
# print(lt[8])
# print(lt[5])
# print(lt[3])
# print(lt[7])
# print(lt[4])
# print(lt[1])
# print(lt[8])


#tuple stores multiple items in a single varaiable, its im mutable(un-changable), its indexed, its ordered

# tp = ('wasiq','khan',21,89,True)
# tp[1]='Ubaid'
# print(tp)


#set stores multiple item in s single variable, its un-ordered, it's un-indexed, it doesnt allow duplicate
# st={'wasiq',21,True,'khan',45.78,'wasiq'}
# st.add('Muzamil')
# st.remove('khan')
# print(st)


#Dictionary stores multiple item in single variable through the process of key-value pairs, its orderd, its key value pairs, it can have duplicates but not duplicate keys, its mutable

# dt={
#     "name":"wasiq",
#     "Roll-no":21,
#     "Adresss":'sgr',
#     "naaw":'wasiq'
   
# }
# dt['name']='umer'
# dt['Email']='z@gmail.com'
# dt.pop('naaw')
# del dt['Email']
# print(dt)


# lt =[['wasiq','umer',True],   ['ubaid',12,89],   ['khan','Maryam',121]]
# # print(lt[0][1])
# # print(lt[2][1])
# # print(lt[1][0])
# # print(lt[2][2])
# # print(lt[1][2])

# lt[0][0]='Ayat'
# lt.append('Saboor')
# lt[0].insert(2,'Athar')
# lt[0].pop(0)
# del lt[0][0]
# print(lt)



# lt = [  [['wasiq','Umer','Ubaid'],[121,78,True]],     [['Gazala','emaan',34.56],  ['Amir','Abdul',False]],
#       [['Madeeha','huda',78.90],['Seerat',89.89, True]]  ]

# # print(lt[1][0][1])
# # print(lt[2][1][0])
# # print(lt[0][1][0])
# # print(lt[2][0][1])
# # print(lt[1][0][0])

# lt[1][0][0]='sania'
# lt[0][0].insert(1,'Umaid')
# lt[0][1].append('Saboor')
# del lt[0][1][0]
# print(lt)


# dt ={
      
#       "Name":{"FirstName":"wasiq","LastName":"Manzoor"},
#       "Adress":{"State":"Kashmir","Pincode":190001},
#       "Subject":{"Major":"CAP2022","Minor":"ACP2022"}
# }


# dt["Name"]["FirstName"] = 'Umer'
# dt['Occupation'] = {"Designation":"Jr Assnt",'Employ-code':9797}
# del dt["Adress"]['Pincode']
# print(dt)
# print(dt['Occupation']['Employ-code'])


# dt ={
#       "1":{"Name":{"FirstName":"Ubaid","LastName":"Khan"},"Adress":{"State":"Kashmir","Pincode":190001}},
#       "2":{"Name":{"FirstName":"Imaad","LastName":"Bhat"},"Adress":{"State":"Kupwara","Pincode":192121}},
#       "3":{"Name":{"FirstName":"Mir","LastName":"Madeeha"},"Adress":{"State":"Baramulla","Pincode":192123}},
# }
# dt["1"]['Name']['FirstName'] = 'Ayat'
# del dt["1"]['Adress']['Pincode']
# print(dt["1"])


# if -ese
#Indentation represents block of code = 1 indentation = 1 tab = 4 Spaces
# grade = input("Enter Yoyr grade:-")

# if grade == 'A':
#     print("Tooper")
# else:
#       print("Fail")
      
# grade =input("Enter an grade:-")

# if grade =='A':
#       print("Topper")
# elif grade =='B':
#       print("Good")
# elif grade== 'C':
#       print("Average")
# else:
#       print("Fail")
      
#input gives by default string value
#Type casting means converting one data type to another
# age = int(input("Enter Your age:-"))
# '21'
# if age >=18:
#       print("You can vote")
# else:
#       print("You cannot vote")

# x = int(input("Enter an number:-"))
# if x%2==0:
#       print("Even number")
# else:
#       print("odd number")


# x =int(input("Enter an number:-"))
# if x>0:
#       print("Positive number")
# elif x==0:
#       print("You entered zero")
      
# else:
#       print("Negative number")


# username = input("Enter your name:-")
# password = input("Enter your password:-")

# if username == 'wasiq':
#       if password == '1234':
#             print("Login sucessfull")
#       else:
#             print("Invalid password")
# else:
#       print("Inncorect username")


#And mean both condition should be true
#or means one of the conditions should be true
# girl = int(input("girl age:-"))
# boy = int(input("boy age:-"))

# if girl>=18 or boy>=18:
#       print("Allowed")
# else:
#       print("Not allowed")
      
      

# a = 2
# b = 21
# c=35
# if a>=b and a>=c:
#       print(a,"is greater")
# elif b>=a and b>=c:
#       print(b," is greater")
# else:
#       print(c,"is greater")


#Excetion handling means to simply identify an error and handle it gracefully
# try:
#       n1 = int(input("Enter ist number:-"))
#       op = input("+,-,x,/:-")
#       n2 = int(input("Enter 2nd number:-"))

#       if op =='+':
#             print(n1+n2)
#       elif op == '-':
#             print(n1-n2)
#       elif op =='x':
#             print(n1*n2)
#       elif op == '/':
#             print(n1/n2)
#       else:
#             print('Invalid operator')

# except ZeroDivisionError:
#       print("Cant divide by zero")
      
  #i =0  
  #i+1 = 1 
  #i+1 = 2
  #i = 9 +1
  #loop is program that runs multiple time until the condition becomes true
  #i is an temporary variable which have default value of 0
  
# for i in range(10):
#       print(i)
      
            
      
# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#       res = tab * i
#       print(tab,'X',i,'=',res)


# print('i am in ils')
# print('i am in ils')
# print('i am in ils')
# print('i am in ils')

#0
#i+1
# for i in range(1,20,2):
#   print(i)


# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#   res= tab * i
#   print(tab,'X',i,'=',res)


# lt = ['wasiq','Umer',12,32,89,True]

# for dt in lt:
#   print(dt)



# dt ={
#   "Name":'Khan',
#   "Roll-no":21,
#   ' Adress':'Maisuma'
# }

# for key,value in dt.items():
#   print(key,':-',value)


#break stop current iteration
# for i in range(10):
#   if i ==5:
#     break
#   print(i)

#continu skips current itteration
# for i in range(10):
#   if i ==5:
#     continue
#   print(i)


# for i in range(100):
#   if i %2==0:
#     print(i,'is even')
#   else:
#        print(i,'is odd')


#7
#
#6

#2-5


# x = int(input("Enter an number:-"))
# if x <=1:
#   print("Not prime")
# else:
#   for i in range(2,x):

#     if x % i ==0:
      
#       print("Not Prime number")
#       break
            
#   else:
#       print("Prime number")




# n = [12,25,90,21,46,101,31]

# flag = 0
# x = int(input("Enter an number:-"))
# for num in n :
#   if x == num:
#     flag =1
    
# if flag ==1:
#   print(x,'is in list')
# else:
#   print(x,"is not in list")
   
   
# #hello
#mom
# word = input("Enter an number:-")
# rev = ''
# for ch in word:
#     #'' = h +'' = h
#     #h = e + h = eh
#     #eh = l + eh  = leh
#     #leh = l+leh = lleh
#     #lleh = o+lleh = olleh
    
#     #'' = m +''= m
#     #m = o +m = om
#     #om = m + om = mom
#     rev = ch+rev
    
# if word == rev:
#     print(word,"is Palindrome")
# else:
#     print(word,"is not palindrome")
    
# lt = [12,25,90,21,46,101,31]
# # print(lt[1:5])
# # print(lt[:])
# # print(lt[-2])
# # print(lt[::3])
# # print(lt[2:])
# print(lt[-1::])


# print(lt[4:])

# lt=[12,25,90,21,46,101,31]
# lt.sort()
# print(lt[-1])


# My name is wasiq


# word = input("Enter an sentence:-")
# # word.split() #split mean remove spaces
# print(len(word.split()))


#my name is wasiq

# lt=[12,25,90,21,46,101,31]
# lt.sort(reverse=True)
# print(lt)


# for i in range(10):
#   print(i)


# i = 0
# while i <30:
#   i = int(input("Enter an number:-"))
#   print(i)

# while True:
#   x = int(input("Enter an number:-"))
#   if x % 2 == 0:
#     print(x,'is even')
#   else:
#     print(x,'is odd')
#   # cht = input("Do you want to continue:-")
#   # if cht =='no':
#   #   break




# while True:
#   n = int(input("Enter an number:-"))
#   if n <=1:
#     print("Not prime number")
#   else:
#     for i in range(2,n):
#       if n%i==0:
#         print("Not Prime ")
#         break
#     else:
#       print("Prime number")
#   cht = input("Enter yes to continue:-")
#   if cht !='yes':
#     break


# try:
#   x = 10/0
# except ZeroDivisionError:
#   print("Cant divide by zero")

#value error

# try:
#   num = int(input("Enter an number:-"))
#   print(num)
# except ValueError:
#   print("Invalid value")

#type error
# try:
#   a ="21"+2
#   print(a)
# except TypeError:
#   print("Type mismatch error")

# #name error
# try:
#   print(a)
# except NameError:
#   print('a is not defined')


# try:
#   lt= [12,78,90]
#   print(lt[3])
  
# except IndexError:
#   print("This item doesnt belong in list")


#key error
# try:
#   dt={
#     "name":"Michall"
#   }
#   print(dt['age'])
# except KeyError:
#   print("This key doesnt belong to dict")
  


# try:
#   a =10
#   a.append(20)
# except AttributeError:
#   print("This thing doesnt belong to this ")




# from index1 import add,sq
# a = int(input("Enter an number:-"))
# b= int(input("Enter an number:-"))
# add(a,b)

# sq(a)





#lambda is a type of function which is used for smaller tasks



# def add(a,b):
#   return a+b


# print(add(10,12))

# add = lambda x,y: x+y
# print(add(11,12))

# sq = lambda x : x*x

# print(sq(3))

# even_odd = lambda x : 'even' if x%2==0 else 'odd' 

# print(even_odd(9))


# lt =[2,3,4,5,6]
# sq = tuple(map(lambda x: x*x,lt))
# print(sq)


# num =['11','21','55','10','89']
# ap = list((map(int,num)))
# print(ap)




# num =[1,2,3,4,5,6,7,8,9,10]
# sq = list(filter(lambda x: x%2==0,num))
# print(sq)


# names = ['BOB','ALICE','KHAN','UMER']
# n = list(map(str.lower,names))
# print(n)

# a = 'wasiq'

# print(a.capitalize())

# a = 'wasiq'

# print(a.upper())

# lt =[-90,21,-11,56,-90,11]
# n = list(filter(lambda x: x<0,lt))
# print(n)


# fruits = ['Kiwi','apple','Mango','pinanapple','pomogrante']
# n = list(filter(lambda x: len(x)>4,fruits))
# print(n)



# names = ['bob','umer','wasiq']
# n = list(map(str.capitalize,names))
# print(n)


#File handling is the process of creating updating and deleting a particulat file
#r stands reading file
#w stand creating a file
#a stands updating a paricular file
#x deleting a particular file


#Here we create a file
# file = open('file.txt','w')
# file.write("Hello from world")
# file.close()

#here we read a particular file
# f = open('file.txt','r')
# data = f.read()
# print(data)


# f = open('file.txt','w')
# f.write('Hello world')


# f = open('file.txt','a')
# f.write(' ,from wasiq')
# f.close()

# f = open('file.txt','r')
# d = f.read()
# print(d)


# f = open('file.txt','x')
# f.close()

f = open('f1.txt','w+b')
f.write(b"Hello sibtain")
f.close()