

#Arthmatic operations
# a = 12
# b=10
# c = a+b
# print(c)

# d = 23
# e = 3
# print(d-c)


# f = 2
# g = 10
# print(f*g)

# h = 10
# i = 2
# print(h/i)


# k = 10
# j = 2
# print(k%j)

# z = 5
# print(z**3)

# #exponent
# a = 10
# b=3
# print(a/b)

# #floor division
# c = 10
# d = 3
# print(c//d)


#comparison operator

# a = 12
# b = 14
# print(a ==b)

# c = 23
# d = 34
# print(c!=d)

# g = 12
# print(g>10)

# h = 22
# print(h<20)

# age = 18
# print(age>=18)

# nage = 12
# print(nage<=12)


#assignment operator
# a = 19

# b =12
# # b = b+3
# b+=8
# print(b)

# c = 13
# c-=3
# print(c)

# d = 3
# d*=4
# print(d)

# e = 10
# e/=2
# print(e)

# f =10
# f%=2
# print(f)


# name = input("Enter your name:-")
# age = input("Enter your age:-")
# print(name)
# print(age)




#Data type tells us which type of data a variable holds or we can say store
#int-- int holds numerical values
#string-- string holds textual dataand everthing that is between inside the quotes or treated as string
#float -- float holds decimal value
#bool -- bool holds true or flase value



# a = 29
# print(type(a))

# b = '10'
# print(type(b))

# c = 10.789
# print(type(c))


# x = 12
# y = 13
# print(x==y)

# z=True
# print(type(z))



# a = 10
# print(a)

# b = 'wasiq'
# print(b)

# c = 'junaid'
# print(c)


#List is a data structure that stores multiple items or values into a single variable,
# its ordered,it's indexed
#index is numerical location of an item/value presented in a particaular variable
# lt = ['wasiq','Gazala',12,67,56.90,True]
# lt[1]='Madeeha'  #here we update existing value
# lt.append('Mariya')  #here append means when we didnt add by index 
# lt.insert(1,'umer')  #here we add a value with the help of index
# print(lt)







#list stores multiple items in a single variable, it's ordered,its indexed, its mutable(changeble)
# #index is a numerical location of item presented in a particular variable
# lt = [12,'Kinza',17.89,'Umer','Khan']
# lt[1]='Reeba' #here we update the existing value
# lt.append('Kaleem')  #here we add with value
# lt.insert(3,'Moomin') #here we add with index
# lt.remove('Reeba') #here we remove by value
# lt.pop(3) #here we remove index
# print(len(lt))
# print(lt)



# # Tuple stores multiple items in a single variable,its ordered,its indexed, it's immutable
# tp = (12,'Abdul','Siyab',19,45)
# print(type(tp))



# #set stores multiple item into single variable,its unordered, its un indexed, it's sometimes im mutable and sometimes mutable
# st = {'wasiq',12,89,'khan','umer'}
# st.add("Emaan")
# st.remove('wasiq')
# print(st)



#Dictionary stores multiple items into single variable through the process of key-value pairs, it's ordered, its un indexed
# dt ={
#     "Name":"Wasiq",
#     "Roll-no":21,
#     "id":21,
#     "Class": "6th"
# }
# dt["Name"]='ubaid'
# dt['Section'] = 'B'  #here we add
# del dt["id"]  #here we remove bu key
# print(dt)



# age = 19

# if age>18:
#     print("You are elgible")
#     print("Hello w")
# else:
#     print("You are not elgible")
    
    
# grade = 'A'
# if grade == 'A':
#     print("Pass")
# else:
#     print("Fail")
    
    
    
    
# grade = input("Enter your grade:-")
# if grade == 'A':
#     print("Pass")
# else:
#     print("Fail")
    



#datatype tell us which type of data a particular variable holds

#int -- numerical data
#string --- textual data' --'
#float --- decimal data
#boolean -- true/false







# a = 21

# print(type(a))


# b = 'wasiq'
# print(type(b))

# c = 10.34
# print(type(c))


# d = True
# print(type(d))


# cd = '23'
# print(type(cd))




#list

# lt = [['wasiq','firdous',12,34,True],   ['aiman','gazala',59,False],   ['Mary','Aliza',45.90,True]]
# print(lt[1][1])
# print(lt[0][3])
# print(lt[1][2])
# print(lt[2][1])

# lt[1][1]='khumi'  #here we do updation
# lt.append('Siyam')  #here we add value
# lt[1].insert(1,'Saliq')
# del lt[2][1]  #here we delete by del
# print(lt)




# lt = [['wasiq','umer',12,56,True],    ['Khan',76,90,False]     ,['Aina','malik',65,89]]
# # lt.append('Maria')
# lt[1].insert(0,'kinza')
# del lt [0][0]
# lt[1][1] = 'Shouib'
# # print(lt[1][0])
# # print(lt[2][1])
# print(len(lt))
# print(lt)



# lt = [[['Umi',21,89,True],['Umaid','siyab','azra',11]],    [['Raju','Saint',33,87],['Aiman','sheeba',90.65,False]]]
# # print(lt[0][1][1])
# print(lt[1][0][1])
# print(lt[1][1][0])
# print(lt[1][1][1])
# print(lt[0][0][3])
# print(lt[0][1][2])
# print(lt[1][1][2])
# print(lt[0][1][0])

# lt[0][1][1]='maira'  #here we update
# lt[1][0].insert(0,'Kumar')
# del lt[1][0][3]
# print(len(lt))
# print(lt)






# dt = {
#     "name":{"FirstName":"Shk","LastName":'Wasiq'},
#     "Adress":{"Pincode":190001,"LoacalAdress":"Shergari sgr"}
# }


# dt["name"]['LastName'] = 'Maryam'  #here we update
# dt["Contact"] = {"code":92,"number":9797824344}  #here we add externally
# dt["name"]['MiddleName']='Binte'  #here we add internally

# print(type(dt))  #here we get type
# print(len(dt['Adress']))  #here we get length
# del dt['Contact']
# print(dt["name"]['FirstName'])
# print(dt['Adress']['Pincode'])
# print(dt['name']['MiddleName'])
# print(dt)




# dt = {
#     1:{"name":{"first":"Emaan","Last":"Khan"},"Adress":{"Pin-Code":190001,"LAdress":"Maisuma"}},
#     2:{"name":{"first":"Abdul","Last":"Hanan"},"Adress":{"Pincode":190002,"LAdress":"Pampore"}}
    
# }
# dt[1]["name"]['first'] = 'Kinza'
# dt[2]["name"]={"first":"Mian","Last":"Qureshi"}
# dt[3]={"name":{"first":"Maryam","Last":"Firdous"},"Adress":{"Pincode":190002,"LAdress":"Nowhata"}}
# # print(len(dt[1]['name']['first']))
# print(dt[1]['name']['first'])
# print(dt[2]['name'])
# print(dt[3])


#loop is a program that runs multiple time untill it met a specific condition

# for i in range(100):
#     print("Ils is best")

#i=0
#i+1 = 1
#i=2
# for j in range(0,20,2):  
#     print(j) #i = 0
    
    #2
    
    
# grade = input("Enter your grade:-")
# if grade == 'A':
#     print("Pass")
# else:
#     print("Fail")



grade = input("Enter your grade:-")
if grade == 'A':
    print("Tooper")
elif grade =='B':
    print('Good')
elif grade == 'C':
    print("Average")
else:
    print("Fail")