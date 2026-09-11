#This is coment

# a = 10
# b =12
# c = a+b
# print(c)

# a = 10
# b = 8
# print(a-b)

# a = 2
# b = 10
# print(a*b)


# a = 10
# b = 2
# print(a/b)

# a = 10
# b = 2
# print(a%b)


# a = 2
# print(a**4)


#relational operator
#comparison operator
# a = 10
# b =10
# print(a==b)


# a = 10
# b= 10
# print(a!=b)



# a = 10
# b =7
# print(a<b)

#greater than equal to operator
# a = 18
# print(a>=18)

#less than equal to operator
# a = 12
# print(a<=12)



#Assignment operator
# a = 10
# # a = a+5
# a+=5
# print(a)


# a = 10
# a-=3
# print(a)

# b = 10
# b*=2
# print(b)


# c = 4
# c%=2
# print(c)


#Datatype is a process which tells us which type of data a particular holds
#int --- it holds numerical value
#string  -- it holds textual data it consider evrthing that is between ''
#bool --- it holds true/false data
#float --it holds decimal value



# a = 10
# print(type(a))

# b = "wasiq"
# print(type(b))


# c = True
# print(type(c))

# d = 10.67
# print(type(d))




# a = 'wasiq'
# print(a)

# b = 'faizan'
# print(b)


#list stores multiple values into a single variable
#index is numerical adress of an value presented in particular list, it's ordered, it's indexed , it allow duplicate value, it's mutable(Changeble)
# lt = ['wasiq',12,'khan','Ubaid',78.12,11]
# # print(lt[5])
# # print(lt[2])
# # print(lt[1])
# # print(lt[3])
# lt[1] = 'faizan'
# lt.append('Gowhar') #here  we add by value
# lt.insert(2,'Abdul')  #here we add by index
# lt.remove('wasiq')  #here we remove by value
# lt.pop(2) #here we remove by index
# print(lt)




# lt = ['wasiq',12,'khan','Ubaid',78.12,11,'hanan','umer',True]
# # print(lt[2:9])
# # print(lt[2:])
# # print(lt[-2])
# # print(lt[:6])

# # print(lt[0:9:3])

# print(lt[::-2])
# print(len(lt))


# #Tuple stores mutiple item in a single variable, its ordered, it's indexed, it's im mutable(un changeble)
# tp = ('wasiq','hanan','abdul',12,90,'wasiq')
# # tp[1]='arshika'
# print(tp)

#set stores multiple item in a single variable,it's unordered, it's un indexed, it does,t allow duplicates, sometimes mutable
# st={'wasiq',12,90,'ubaid','khan','wasiq'}
# st.add('Zayeem')
# st.remove('wasiq')
# print(st)


#Dictionary stores multiple item in a single variable, it stores data in key-value pairs, it's ordered

# dt ={
#     "name":"wasiq",
#     "roll-no":21
# }

# dt["name"] = 'Maddeha' #here we update
# dt['Adress'] = "Sgr"  #here we add 
# del dt['name']  #here we delete
# print(dt)


#string is im mutable
# a = 'wasiq'
# a [0]= 'h' 
# print(a)


# name  = 'wasiq'
# print(name.capitalize())
# print(name.upper())


# name = 'WASIQ'
# print(name.lower())




#set stores multiple item in a single variable, it's not ordered, it's unindexed, it doesnt allow duplicate 
# st ={'wasiq','abdul','khan',12,45,'khan'}
# st.add('faizan')
# st.remove('wasiq')
# print(st)



#dictionary stores multiple item in a single variable, in the process key-value pairs, key should not be same


# dt ={
    
#     "name":'Faizan',
#     "roll-no":12,
#     "namee": 'Faizan'
# }
# dt['roll-no'] = 22 #here we update
# dt['Adress'] ='sgr'  #here we add
# del dt['namee']  #here we delete
# print(dt)


# dt={
#     "1":{"name":"Faizan","Roll-no":21},
#     "2":{"name":"Arrob","Roll-no":22},
#     "3":{"name":"Faheem","Roll-no":23}
# }

# dt["1"]['name'] = 'wasiq'
# dt["2"] = {"name":'Aruba','Roll-no':1}
# del dt["1"]['name']
# print(dt)


lt = [['abdul','khan',23,True],  ['Hanan','kinza',56],   ['Ainan','gazala',False]]
lt[1][0] = 'inayat'
lt[0].append('Madeeha')
lt[1].insert(0,'zayeem')
del lt[0][1]
# print(lt[0][1])
# print(lt[1][1])
# print(lt[2][1])
# print(lt[0][3])
# print(lt[1][2])
# print(lt[1][0])
print(lt)