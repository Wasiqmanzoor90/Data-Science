# a ='umer'
# print(a)

# b ='hanan'
# print(b)
#yoxnhs
# c ='ubaid'
# print(c)

# d ='ali'
# print(d)

# e ='wasiq'
# print(e)

#ok
# abc =['wasiq', 3.5, True, 'ubaid'] #we have created an list
# abc.append('umer') # we have added an element in the list using append function
# abc.remove(3.5) # we have removed an element from the list using remove function
# abc.insert(1,'hanan') # we have inserted an element at index 1 using insert function
# abc.pop(4) # we have removed the last element from the list using pop function
# abc[0]='burhan'
# print(abc)


#tuple
# So Basically Tuple is same as list but the only difference is that tuple is immutable means we cant change the value of tuple once it is created
# thistuple = ('umer',5.6,'hanan',True,'hanan')
# thistuple[0]='musaib'
# print(thistuple)


#set
# So Basically Set is a collection of unordered and unindexed elements
# We can not access the elements of set by referring to an index because sets are unordered the items has no defined order
# Sets are mutable means we can add or remove items from it but we can not change the items of set
# thisset ={'umer',3.4,True,'burhan','umer'}
# thisset.add('ali')
# thisset.remove('burhan')
# print(thisset)

#slicing
# thelist=['wasiq','ubaid',3.5,True,'hanan']
# print(thelist[1:5])

#dictionary
#it store data in key:value pairs
# thisdict = {
#     'name': 'umer',
#     'age': 25,
#     'gender': 'male',
#     'sex':'male'
# }
# thisdict['age']=26  #we can change the value of a key
# print(thisdict)

# thislist = ['apple','umer',3.5,10, True]
# thislist[1]='hanan'  #editing the value at index 1
# thislist.append('ubaid')
# thislist.insert(2,'burhan')
# thislist.remove('apple')
# thislist.pop(0)
# print(thislist)


# #tupple
# thistuple = ('umer',3.5,True,'hanan')
# print(thistuple[0])

#set
# thiset = {'umer',3.5,True,'hanan','umer'}
# thiset.add('ubaid')
# thiset.remove('hanan')
# print(thiset)

# thisdict = {
#     'Name': 'umer',
#     'Age': 25,
#     'Gender': 'male',
#     'Sex': 'male'
# }
# thisdict['State'] ="kashmir"
# thisdict['Name']='hanan'
# thisdict.update({'Age':26})
# thisdict.pop('Gender')
# print(thisdict)

#nested dict 

# nestdisct ={
#     "1":{"name":"wasiq", "age":25,'pincode':190015},
#     "2":{"name":"burhan", "age":23,'pincode':1900012},
#     "3":{"name":"hanan", "age":22,'pincode':190013},
#     "4":{"name":"alim", "age":21,'pincode':190014}
# } 
# #adding the element in nested dict
# nestdisct['5']={"name":"ubaid", "age":24,'pincode':190016}
# #removing the element from nested dict
# nestdisct.pop('2')
# # print(len(nestdisct["1"]['name']))
# nestdisct.update({'3':{'name':'umer'}})
# # print(type(nestdisct))
# print(nestdisct["3"])

# nestdict = {
#     "1":{"name":{"firstname":"Abdul","lastname":"Moomin"},"Dob":{"Day":5,"Month":8 ,"year":2000}},
#     "2":{"name":{"firstname":"saliq","lastname":"mushtaq"},"Dob":{"Day":2,"Month":11 ,"year":2001}},
#     "3":{"name":{"firstname":"Hanan","lastname":"Manzoor"},"Dob":{"Day":17,"Month":1 ,"year":2007}}
# }
# nestdict['4']={"name":{"firstname":"Manan","lastname":"Malik"},"Dob":{"Day":5,"Month":10 ,"year":2005}}
# nestdict["2"]={"name":{"firstname":"Wasiq","lastname":"Manzoor"},"Dob":{"Day":5,"Month":12 ,"year":1960}}
# print(nestdict["2"])

# nestlist = [['hanan',1,980,2.0],    [234,523,'kamran',12],    [214,223,'umran',212]]
# nestlist[2][2] = 'abdul'
# nestlist[2].append('iram')
# nestlist[2].insert(4,'Madeeha')
# del nestlist[2][4]
# print(nestlist[2][1])

# scram = [[['wasiq',19,254,0.7],['umaran',9.0,65]]     ,[[40,1000,'maryam',29],['kamran',11,'abdul']]   ,[[999,367,'hadiya'],[209,'waqas','ubaid']]]

# print(scram[0][1][2])


# obc=[[[1,11],  [5,34]]    ,[[80,89],[23,56]],    [[11,145],[51,32]]]
# print(obc[1][1][1])


    

# a = int (input("Enter you age: "))
# if(a>=18):
#     print("you are elgible to vote")

# else:
#     print("you are not elgible")
    
    
# evenodd = int(input("Enter any number"))

# if(evenodd % 2 == 0):
#     print("this is even number")
# else:
#     print("this is odd number")

# age = int(input("enter any number"))

# if(age>=25):
#     print("Your Post Graduation is in Completed")
# elif(age>=22):
#     print("Your graduation is done")
# else:
#     print("You are still in school!")

# try:    
#     n1 = int(input("Enter number1:-"))
#     n2 = int(input("Enter number 2:-"))

#     op = input("Choose your Operator:- +, -, *, /, %")

#     if(op == '+'):
#         s = n1+n2
#         print("sum",s)
    
#     elif(op == '-'):
#         sub = n1-n2
#         print("subtraction:", sub)
    
#     elif(op =='*'):
#         mul = n1*n2
#         print("Mult", mul)
    
#     elif(op == '/'):
#         div = n1/n2
#         print("division", div)
        

    
#     else:
#         print('Invalid operator')

# except ZeroDivisionError:
#     print("Cant divded by zero")

# n1 = int(input("enter an number"))
# if(n1%2 == 0):
#     print("its an even number")
# else:
#     print("its an odd number")




# for i in range(0,20,2):
#     print(i)

# fruit = ['apple', 'mango', 'pear']
# for fruits in fruit:
#     print(fruits)

# thisdict = {
#     'Name': 'umer',
#     'Age': 25,
#     'Gender': 'male',
#     "pin code": 190001
# }
# for key,value in thisdict.items():
#     print(key,":",value)

# tab = 3
# for i in range(1,11):
#     res = tab * i
#     print(tab,"x",i,"=", res)
    
# dicto = {
#     "name":"Burhaan",
#     "Roll no": 12,
#     "Pin-code":190001
# }

# for ind,val in dicto.items():
#     print(ind,":", val)
    
# for i in range()

# for i in range(1,11):
#     if(i == 5):
#         continue
#     print(i)

# n = int(input("Enter an number"))
# if(n<=1):
#     print("Not a prime number")
# else:
#     for i in range(2,n):
#         if(n%i==0):
#             print("Not an Prime number")
#             break
#     else:
#         print("Prime number")





# word = input("enter an word:-")
# rev = ""

# for ch in word:
#     rev = ch + rev
    
# if word == rev:
#     print("Palindrome")
    
# else:
#     print("Not Palindrome")
    

            
            
# i = 25
# while i < 30:
#     i= int(input("Enter an number:-"))
#     print(i)
# else:
#     print("You are done")

# while True:
#     n = int(input(":Enter an number:-"))
#     if(n%2==0):
#         print("Even number")
#     else:
#         print("odd number")
#     cht = input("Enter (yes/no) to repeat or close:-")
#     if cht != 'yes':
#         print("Bye Bye")
#         break

# a = 10
# b=20
# a,b = b,a
# print(a,b)
# temp = a
# a = b
# b= temp
# print(a,b)
# for i in range(1,11)


# from ok import add
# a = int(input("Enter number 1:-"))
# b = int(input("enter number 2:-"))
# ab=add(a,b)
# print(ab)
# def add(lt):
#     return lt.append(100)

# lst = [22,33,45]
# add(lst)
# print(lst)

# lst.append(10)
    
# v=12  

# def ok(y,z):
#   print(y,z)
    

# num = 5
# n1 = 6
# ok(num,n1)

# add = lambda x,y:x+y

# ok=add(12,13)
# print(ok)

# check_num = lambda x:'Even' if x%2==0 else 'odd'


# num = int(input("Enter an number:-"))
# print(check_num(num))



