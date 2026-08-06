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



lt = [  [['wasiq','Umer','Ubaid'],[121,78,True]],     [['Gazala','emaan',34.56],  ['Amir','Abdul',False]],
      [['Madeeha','huda',78.90],['Seerat',89.89, True]]  ]

# print(lt[1][0][1])
# print(lt[2][1][0])
# print(lt[0][1][0])
# print(lt[2][0][1])
# print(lt[1][0][0])

lt[1][0][0]='sania'
lt[0][0].insert(1,'Umaid')
lt[0][1].append('Saboor')
del lt[0][1][0]
print(lt)
