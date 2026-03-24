#so basically print here means to give output
#print("Hello, World!")


#Arthmatic opertors

# #Addition
# a = 30
# b =12
# print(a+b)


# #subtraction
# s1 =  15
# s2 = 9
# print(s1-s2)

# #multiplication
# m1 = 2
# m2 = 12
# print(m1*m2)

# #divide
# d1 = 10
# d2 = 5
# print(d1/d2)

# #Modules
# mo1 = 10
# mo22 = 5
# print(d1%d2)



#Comparison Operator
# a = 10
# b =12
# print(a == b)

#Not Equal to
# a = 10
# b=10
# print(a!=b)

# #greater than
# a = 12
# print(a>18)

# #less than
# a = 12
# print(a<18)

#greater equal
# a = 18
# print(a>=18)

#less equal
# a = 12
# print(a<=12)

# a = 20
# b = 25
# print(a == b)


# a = 20
# b = 25
# print(a!=b)

#Assignment operator
# a = 10
# # a = a+3
# a+=3
# print(a)


# a = 10
# a-=3
# print(a)

# a =15
# a/=5
# print(a)

#data type help us categorize a data

#string is a data type that holds textual data! it get intialize by quotes
# a = 'wasiq'
# print(type(a))

# #int is a data type that holds a numerical value
# b = 21
# print(type(b))

# #Boolean is data type that holds true or flase
# c = True
# print(type(c))

# d = 12.56
# print(type(d))

# ab= '12'
# print(type(ab))

# name =input("rnter your name:-")
# age = input("Enter you age:-")
# print(type(age))
# print(name)
# print(age)



# a = 'wasiq'
# print(a)

# b = 'ubaid'
# print(b)

# c = 'Imaad'
# print(c)


#so basically list is data type that stores multiple value or elemts in a single varibale
#index is a numerical location of particular value present in the list, index can't be same
##it allow duplicate values
# lt = ['ubaid',12,'Sahil',True,56.98,'wasiq','sahil','umer']
# lt[0]='moomin'   #we can do updation in a list with index
# lt.append('adil')  #we we add direct by value it get added at last
# lt.insert(1,'furkan') #when we want add a value at particular place in a list
# print(lt)


#so basically list is data type that stores multiple value or elemts in a single varibale
#index is a numerical location of particular value present in the list, index can't be same
##it allow duplicate values, its ordered and its indexed, its mutable means we can change it
# lt = ['Furkan','Imaad',32,True,'Ubaid','Sahil']
# lt[0]='Aadil'  #here we update
# lt.append('umer')  #here it adds direct by value
# lt.insert(1,'Moomin')  #here it takes two things index and value
# lt.remove('Sahil')  #we remove here by value
# lt.pop(0)  #here we remove by index
# print(lt)

#tuple stores multiple values or items i a single variable,its orderes,its indexed
#it allow duplicates, its im mutable or we can say un changeble
# tp = (12,'wasiq',43,90,'ubaid','hanan')
# tp[0] = 'khan'
# print(tp)


#set basically stores multiple items or values in single variable, it's not ordered,its not indexed,its mutble 
#but we can only or remove
# st = {'Sahil','ubaid',12,'khan','Furqan'}
# st.add("Adil")
# st.remove(12)
# print(type(st))  #here type means which type of data a variable holds
# print(len(st)) #here len how many elements or items or there i a variable
# print(st)


# lt =['wasiq', 'umer','ubaid','khan',121,234,90.8]
# print(type(lt))
# print(len(lt))


#Dictionary stores multiple value or items in a single variable through the process  key-value pairs,it' ordered
#its un indexed, it only allows duplicate value it doesn't allow duplicate keys!, its mutable
# dt = {
#     "name":"wasiq",
#     "Roll-no":21,
#     "Pin-code":190001,
#     "Zip-code":190001
# }
# dt["name"]='Sahil'  #here we update though key
# dt['Caste']='Bhat'  # here we add a value
# del dt["Zip-code"]   #here we delete by del keyword
# dt.pop("Pin-code")  #here we delete by pop method
# print(dt)


# lt = [['hanan','kazin',11,21,76],['sahil','Umer',109,23.76],[24,'imaan','muskan',54,89]]
# lt[1][0]='furakan'  #here we update
# del lt[1][1]  #deletation
# # print(lt[2][4])
# # print(lt[1][3])
# # print(lt[0][4])
# print(len(lt))



# lt = [['wasiq',21,24,45,67],['Adil','Sahil',32,891,754],[True,23.89,43,75,12]]
# lt[0][0]='Moomin'  #updation
# del lt[2][0]  #deletion
# lt[1].insert(0,'Hanan')
# print(lt)


# lt = [[['Hanan','ubaid',11,23,34,65],['Kazim','umer','habis',True]],    [['Imaad','abid',34.12],['sahil','khan',112,341]],    [['Madeeha','lubna',23,11.54,90],['kinza',78.90,True]]]

# lt[0][1][0]='Hazim' #updation
# del lt[2][0][0]   #deletion
# # print(lt[2][1][1])
# # print(lt[0][1][1])
# # print(lt[1][1][0])
# print(lt[2])



# lt = [[['wasiq','ubaid',12,45,True],['sahil','khan',21.78]],    [['Madeeha','jasira',56.90,False],['Jasira','owais','Lubna',12.89]],   [['Hazim','khan',90,True],['Kinza','Yasir','Furkan']]]

# lt[2][0][1]='Reeba'  #updation
# del lt[2][1][1]  #delete
# lt[0][1].insert(1,'adil')
# # print(lt[1][0][1])
# # print(lt[0][1][1])
# # print(lt[2][0][0])
# # print(lt[1][1][2])
# print(lt[0])



# dt = {
#     1:{'name':"sahil",'Roll-no':21},
#     2:{'name':"Moomin",'Roll-no':22},
#     3:{'name':"Furkan",'Roll-no':23}
# }


# dt[1]={'name':"umer",'Roll-no':11} #updation
# dt[2]['Roll-no']=12
# del dt[3]['Roll-no']
# dt[4]={'name':"Tehseen",'Roll-no':13}
# print(dt[1])
# print(dt)



# dt = {
#     1:{"name":{"First-name":"Sahil","Lastname":"Bhat"}, "Adress":{"District":"Srinagar","Pin-code":190001,"local-adress":"Hyderpora"}},
#     2:{"name":{"First-name":"Adil","Lastname":"Ahmad"}, "Adress":{"District":"Pulwama","Pin-code":192301,"local-adress":"Kaka-Pora"}},
#     3:{"name":{"First-name":"Furkan","Lastname":"Ahmad"}, "Adress":{"District":"Budgam","Pin-code":192302,"local-adress":"Beerwah"}},
#     4:{"name":{"First-name":"Tehseen","Lastname":"Motto"}, "Adress":{"District":"Srinagr","Pin-code":190002,"local-adress":"Nawkadal"}},
#     5:{"name":{"First-name":"Moomin","Lastname":"Shareif"}, "Adress":{"District":"Srinagar","Pin-code":190017,"local-adress":"Shalteng"}},
# } 
# dt[1]['name']['First-name']= 'Rahil'  #here we update
# dt[5]['name']={"First-name":"Mumin","Lastname":"Dar"}

# del dt[2]['name']['Lastname']  #gere we delete
# dt[6]={"name":{"First-name":"sheikh","Lastname":"wasiq"}, "Adress":{"District":"Srinagar","Pin-code":190017,"local-adress":"Bemina"}} #here we add
# # print(dt[2]['Adress']['Pin-code'])
# # print(dt[4]['Adress']['District'])
# # print(dt[4]['name']['Lastname'])
# # print(dt[5]['Adress']['local-adress'])
# # print(dt[1]['name']['First-name'])
# print(dt[6])

#Typecating:- when we convert one data type into anothere datype
#indetation: Basically it means block of code
# age = int(input("Enter your age:-"))

# if age > 18:
#     print("You are elgible to vote")
# else:
#     print("You are not elgible to vote")


# grade = input("Enter your grade")
# if grade == 'A':
#     print("Topper")
# else:
#     print("Average")


#when we have to check multiple conditions we use nested if else
# grade = input("Enter your grade:-")
# if grade == 'A':
#     print("Topper student")
# elif grade == 'B':
#     print("Good student")
# elif grade == 'C':
#     print("Average")
# else:
#     print("Fail")
    
    
    
# n = int(input("Enter an number:-"))
# if n>0:
#     print(n,"is Positive number")
# elif n < 0 :
#     print("Negative")
# else:
#     print("0 You entered zero")


#in and operator both the codition should be true
#in or operator one of the condition should be true
# a = 13
# b =20

# if a > 18 or b>18:
#     print("Done")
# else:
#     print("Not done")


# n = int(input("Enter an number:-"))
# if n % 2 == 0:
#     print("even number")
# else:
#     print("Odd number")
    
    
# n1 = int(input("Enter ist number:-"))
# op = input("Enter an operator(+,-,*,/)")
# n2 = int(input("Enter second number:-"))

# if op == '+':
#     print(n1+n2)
# elif op =='-':
#     print(n1-n2)
# elif op == '*':
#     print(n1*n2)
# elif op == '/':
#     print(n1/n2)
# else:
#     print("invalid operator")


# print("My name is wasiq")
# print("My name is wasiq")
# print("My name is wasiq")
# print("My name is wasiq")
# print("My name is wasiq")


#loop is a program that runs multiple times untill it met the specific condition


# for i in range(50):
#     print("Hello world")

#0
#break is keyword that stops the execution
# for i in range(20):
#     if i == 11:
#         break
#     print(i)
    

#continue is a keyword that skips the current number of execution
# for i in range(13):
#     if i == 6:
#         continue
#     print(i)


#when we want to get from particular item to another or we can say range based! we use the concept of slicing
# lt = ['wasiq', 'umer','ubaid','khan',121,234,90.8]
# print(lt[1:7])
# print(lt[2:])
# print(lt[:3])
# print(lt[-1])



# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#     res = tab*i
#     print(tab,'x',i,'=',res)



# data=['wasiq','umer','khan',121,78,90]
# for ok in data:
#     print(ok)

# a = 'furkan'
# for name in a:
#     print(name)


# dt ={
#     'name':"Sahil",
#     "Roll-no":21,
#     "Pin-code":190001
# }

# for key,value in dt.items():
#     print(key,value)
    
# for i in range(1,20):
#     if i % 2 ==0:
#         print(i)


#manual swapping here we use third variable for swapping
# a = 20
# b=15
# c = a
# a = b
# b=c
# print(a)
# print(b)

#automatic swaping which is in python only
# a = 32
# b=15

# a,b = b,a
# print(a)
# print(b)



# num = [11,21,3,4,93,39,89,107,111,207]
# flag = 0
# #23
# x = int(input("Enter an number:-"))

# for nums in num:
#     if x == nums:
#         flag=1

# if flag ==1:
#     print(x,'is in list')
# else:
#     print(x,'is not in list')


#8
#6
#11
#7
n = int(input("Enter an number:-"))
if n<=1:
    print("Not Prime")
else:
    for i in range(2,n):
        if n%i==0:
            print(n,"is not Prime")
            break
    else:
        print(n,"Prime number")