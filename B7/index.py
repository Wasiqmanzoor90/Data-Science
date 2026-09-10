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






dt = {
    
    "1":{"Name":"wasiq","Roll_no":21},
    "2":{"Name":"umer","Roll_no":22}
}


# dt["1"]={"Name":"ubaid","Roll_no":1}
dt['1']['Name'] = 'Rubhaan'
dt['3'] = {"Name":"Hanan","Roll_no":2}
del dt['1']['Name']
print(dt)