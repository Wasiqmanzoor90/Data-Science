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





dt ={
    
    "name":{"FirstName":"Shk","Lastname":"Wasiq"},
    "Adress":{"Pincode":190001,'Local-Adress':'Maisuma'}
    
}

dt["Adress"]['Local-Adress']= 'Sonwar'  #here we update
dt['name']={'FirstName':'Taha','Lastname':"Sofi"} #here we are updating whole
dt["name"]["MiddleName"] = 'Ahmad' #here we add internally
dt["Contact"]={"code":92,"phn-no":9797854644} #here we add contact key
del dt["Adress"]['Pincode'] #here we delete an individual
print(len(dt))
print(dt)
# print(dt['name']['Lastname'])