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
dt = {
    "name":"wasiq",
    "Roll-no":21,
    "Pin-code":190001,
    "Zip-code":190001
}
dt["name"]='Sahil'  #here we update though key
dt['Caste']='Bhat'  # here we add a value
del dt["Zip-code"]   #here we delete by del keyword
print(dt)
