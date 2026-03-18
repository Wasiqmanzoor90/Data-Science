# # #output function
# # print("hello world")

# # #addition
# # a = 12
# # b = 10
# # z = a+b
# # print(z)

# # #subtraction
# # c = 19
# # d = 10
# # e = c-d
# # print(e)

# # #multiplication
# # f = 3
# # g = 5
# # h = f*g
# # print(h)

# # #division
# # de = 8
# # cd = 4
# # zd = de/cd
# # print(zd)

# # #If we have to find reminder
# # fg = 8
# # cg = 4
# # wa = fg%cg
# # print(wa)


# # #exponent(raise power)
# # n1 = 2 ** 3
# # print(n1)

# # #floor division
# # n2 = 7 // 2
# # print(n2)

# #addition
# # a = 8
# # b = 8
# # z = a-b
# # print(z)

# #subtraction
# # x = 8
# # y = 2
# # yz = a%b
# # print(yz)


# # xyz = 5**5
# # print(xyz)


# # b = 7/3
# # print(b)

# # c = 7//3
# # print(c)


# #its a int data type
# a = 10
# print(a)

# #its is string data type
# b = '20'
# print(b)

# # its bool data type
# c = True
# print(type(c))

# #its float data type
# d = 24.65
# print(type(d))

#comparison
# a = 10
# b = a
# print(b)

# #equal to
# a =20
# b=30
# print(a == b)

# #greater than equal to
# c = 40
# d =20
# print(c>=d)

# #less than equal to 
# c = 30
# d = 30
# print(c<=d)

# #greate than equal to
# age =18
# print(age>=18)


# #not equal to
# df =20
# de = 10
# print(df!=de)


#Assigment operator
# a = 10
# b = a
# print(b)

# a = 10
# # a = a + 5 
# a += 5
# print(a)

# b = 14
# # b = b - 4
# b-=4
# print(b)

# c = 4
# c*=4
# print(c)

# f = 6
# f/=6
# print(f)

# n = 7
# n%=3
# print

# l = 9
# l%=2
# print(l)

# k = 11
# k%=3
# print(k)

# o = 13
# o%=3
# print(o)

# j = 17
# j%=3
# print(j)

# a =input("Enter your name:-")
# print(a)

# a= 'aiman'
# print(a)


# b= 'aqib'
# print(b)

# c= 12
# print(c)
# a = input("enter your name")
# print(a)

#list is an an data type which is used to store multiple values in a single variable, its indexed
#its ordered and allows duplicate values, its mutable(changeble)

# lst = ['aiman','aqib',12,67.89,True,13,'reeba','adnan','reeba']
# lst[6] = 'jasira'  #update by index 
# lst.append("Hena")  #add by direct value where we dont give index so thats why it comes in last position
# lst.insert(5,'adnan malik')  #add by index at particular place
# lst.remove('adnan malik')   #remove by direct by value
# lst.pop(1) #remove by index
# print(lst)


# a = 'My name is Emaan'
# print(a)

# b = "My name is gazala"
# print(b)

# c =10
# print(c)


# #its ordered,its mutable,its indexed ,it allows duplicate values
# lt  = ['My name is emaan','My name is gazala',10,'Aiman',123,'hanan',True,'khan']
# print(type(lt))
# print(len(lt))
# lt[5]='wasiq'  #it updates
# lt.append('Abdul')  #add value directly thats why its at last
# lt.insert(2,'reeba') #when we add by index at particular place
# lt.remove('Aiman') #when we remove direct by value
# lt.pop(5) #when we remove by index
# print(lt)


#in tuple we can store multiple items or values in a single varibla,its ordered,its indexed,it allows duplicate values
#its immutable*(un-changeble)
# tp = (12,'wasiq','hanan',23,110,'aiman',28,'adnan','wasiq')
# print(type(tp))  #so basically type tell us which type of data is this
# print(len(tp)) #len tell us how items or values or present inside a variable
# tp[1]='abdul'
# print(tp)


# #so basically it stores multiple items or values in a single varibale,its unordered,it doesn't allow duplicate values
# # ,its un-indexed,it only adds and remove by direct value,its doesnt update
# st = {'adnan',11,'Tabish',True,12.78,90,'adnan'}
# st.add('Aiman')  #add value directly thats why its at last
# st.remove(11)  #remove by direct value
# print(st)






#its unordered,its unindexed,it doesnt allow duplicate value, it allow only add and remove
# ty = {'Aiman',11,22,'Adnan',True,'Aiman'}
# ty.add('Hina')
# ty.remove('Aiman')
# print(ty)



# a = 'wasiq'
# print(a[2])


# b = 'jasira'
# print(b.upper())

# c = 'ADNAN'
# print(c.lower())


# a = 'Aiman'

# print(a[1:5])


# c = 'Khan'
# print(c[1:])

# d = 'Adnan'
# print(d[:3])


#Dictionary stores multiple value in a single varibale throught the process  of key-value pairs
#its ordered,it not indexed its key-valued pairs ,it alows duplication only for values but not for keys
#its mutable(changable)
# dt={
#     "name":"Adnan",
#     "roll-no":21,
#     "Adress":"Kupwara",
#     "local":"Kupwara"
# }
# dt['name']='Ubaid' #updation with key
# dt["Parentage"] = 'khan'  #when we have add
# dt.pop('roll-no') #when we have to remove
# del dt["name"]  #another form of remove
# print(dt)



# # #nested list means were we store multple list in a single list
# lt = [['Jasira',12,87,'Khalid','iram'],[97,82,'Hanan','Umer',45],[39,'Gazala',90,'khan',12.78]]

# lt[0][4]='Madeeha'  #here we update 
# lt[0].append("zubair")  #here we add by value
# lt[0].insert(1,'ubaid')  #here we add at particular place
# del lt[1][2]  #here we remove by index

# print(lt)

#Nested Dictionary means when we store multiple dictionary in single ditionary
# dt = {
#     "1":{"name":"Jasira", "Roll-no":21, "Grade":"A"},
#     "2":{"name":"Adnan", "Roll-no":22, "Grade":"A"},
#     "3":{"name":"Aqib", "Roll-no":23, "Grade":"B"},
#     "4":{"name":"Tabish", "Roll-no":24, "Grade":"A+"}
# }
# dt["1"]["name"]="Madeeha"   #here we update
# dt["5"]={"name":"Reeba", "Roll-no":25, "Grade":"B+"}  #here we add
# del dt["1"]["Grade"]  #here we delete 
# print(dt)

#nested 
# lt = [[['Ubaid',12,'Amir','Khan',32,True],['Reeba','Kinza',78,90]],   [[21,112,'Jasira','Adnan',809],['Aqib','emaan',91,48,12]]     ,[['Tabish','kazim',34,'Nayla'],['Saba','umer',213,87]]]

# # lt[1][0][2] = 'Wasiq'  #updation
# # lt[1][0].insert(2,'Tabish') #add
# # del lt[1][0][3]  #delete

# # print(lt[0][1][1])
# # print(lt[1][0][2])
# # print(lt[2][0][3])
# # print(lt[0][1][0])
# # print(lt[1][0][3])
# # print(lt[2][1][0])
# print(lt[0][1][3])





# dt = {
#     "1":{"name":{"FirstName":"Jasira","Latname":"Fayaz"},"Adress":{"State":"Kashmir","Local-Adress":"Srinagar","Pincode":190001}},
#     "2":{"name":{"FirstName":"Ahsaan","Lastname":"Malik"},"Adress":{"State":"Jammu","Local-Adress":"Katra","pincode":190003}},
#     "3":{"name":{"FirstName":"Reeba","Lastname":"Hamid"},"Adress":{"State":"Kashmir","Local-Adress":"Bandipora","pincode":190002}}
# }

# dt["1"]["name"]["FirstName"] = "Madeeha"  #updation
# dt["4"]={"name":{"FirstName":"Adnan","Lastname":"Tahir"},"Adress":{"State":"Kashmir","Local-Adress":"Kupwara","Pincode":190005}}
# #Adding the value
# del dt["1"]['Adress']["State"]   #delete a particular value
# print(dt["1"]["name"]["FirstName"])   
# print(dt["1"])
# print(dt["1"]["Adress"]["Pincode"])
# print(dt["2"]["name"]["Lastname"])
# print(dt["2"]['Adress']["State"])
# print(dt["3"]["Adress"]["Local-Adress"])








#identation is a block of code , 1 indentation =1 tab = 4 spaces
#TypeCasting means when we convert one data type into another data type
# age = int(input("Enter an number:-"))
# if age > 18:
#     print("You are elgible to vote")
# else:
#     print("You are not elgible")



# grade= input("Enter your grade:-")
# if grade == 'A':
#     print("You are Pass")
# else:
#     print("You are fail")



#Nested if else means when we have to check multiple condition
# grade = input("Enter an Grade:-")

# if grade == 'A':
#     print("Topper")
# elif grade == 'B':
#     print("Good Student")
# elif grade == 'C':
#     print("Average student")
# elif grade == 'D':
#     print('Pass Student')
# else:
#     print("Fail")




#Calculator
# n1 = float(input("Enter an ist number:-"))
# op = input("Enter an operator(+,-,*,/)")
# n2 = float(input("Enter an second number:-"))

# if op == '+':
#     print(n1+n2)
# elif op == '-':
#     print(n1-n2)
# elif op == "*":
#     print(n1*n2)
# elif op == '/':
#     print(n1/n2)
# else:
#     print("Invalid Operator")


# n = int(input("Enter an number:-"))
# if n%2 == 0:
#     print("Even number")
# else:
#     print("Odd number")

# username = input("Enter your Username:-")
# password = input("Enter an password:-")
# if username == 'Wasiq':
#     if password == '123':
#         print("Login Sucessfull")
#     else:
#         print("Wrong Password")
# else:
#     print("Invalid Username")

# n = int(input("Enter an number:-"))
# if n > 0:
#     print(n,"Positive Integer")
# else:
#     print(n,"Negative Number")


# a = 20
# b=10
# #logical operator/ logical gates
# #here or means one of the codition should be true

# if a == 20  or b ==15:
#     print("True")
# else:
#     print("False")
    

# #here and means both of the conditions should be true
# if a == 20  and b ==15:
#     print("True")
# else:
#     print("False")

# print("Hello im from ILS")
# print("Hello im from ILS")
# print("Hello im from ILS")
# print("Hello im from ILS")

# for i in range(5):
#     print("Hello im from ILS")
    
    
#loops is a program that runs multiple times until it met a specific condition
#here i is temporary variable


# for i in range(5):
#     print(i)


#here range takes three values first starting point, ending point and jumps
# for i in range(0,20,2):
#     print(i)



# try:
#     n1 = float(input("Enter an ist number:-"))
#     op = input("Enter an operator(+,-,*,/)")
#     n2 = float(input("Enter an second number:-"))

#     if op == '+':
#         print(n1+n2)
#     elif op == '-':
#         print(n1-n2)
#     elif op == "*":
#         print(n1*n2)
#     elif op == '/':
#         print(n1/n2)
#     else:
#         print("Invalid Operator")
# except ZeroDivisionError:
#     print("Cant Divide by zero")


# tab = int(input("Enter an number:-"))
# for i in range(1,11):
#     res = tab*i
#     print(tab,'x',i,'=',res)


# lt =['jasira','reeba','Aqib','aiman','adnan','tabish']
# for i in lt:
#     print(i)
    
# name = 'wasiq'
# for names in name:
#     print(names)






# lt = [12,56,'jasira','abdul','hanan']
# for pk in lt:
#     print(pk)


# dt = {
#     "name":"Kazim",
#     "Roll-no":32,
#     "Adress":"Khayam"
# }

# for key,value in dt.items():
#     print(key, value)

# for i in range(1,20):
#     if i% 2 ==0:
#         print(i)


#in while loop we dont know the current number of utteration
#in for loop we know already the current number of itteration or we can say how many times it will run
# num = 0
# while num < 30:
#     num = int(input("Enter an number:-"))
#     print(num)


#5 1 ,5
#4 1,2,4
#1 1

#11
#8


# for i in range(20):
#     if i == 10:
#         break  #here break means to stop the iteration at 10
#     print(i)


# for i in range(20):
#     if i == 10:
#         continue  #here continue means to skip the iteration at 10
#     print(i)


#5
#4
# n = int(input("Enter an number:-"))  #ist step
# if n <=1: 
#     print("Its not Prime Number")
# else:
#     for i in range(2,n):
#         if n % i ==0:
#             print("Not Prime number")
#             break
#     else:
#         print("Prime number")


# num = [21,32,11,45,65,89,91,72,22]
# flag = 0

# #22
# x = int(input("Enter an number:-"))
# for nums in num:
#     if  x== nums:
#         flag=1
        
# if flag == 1:
#     print(x,'is in the list')
# else:
#     print(x,'is not in list')

#hello
#mom
# word = input("Enter an word:-")
# reverse =''

# for ch in word:
    
#     #'' = h + ""
#     #h =  e + h = eh
#     #eh = l + eh = leh
#     #leh = l + leh = lleh
#     #lleh = o + lleh = olleh
    
    
#     #'' =  m + '' = m
#     #m =  o + m = om
#     #om = m + om = mom
#     reverse = ch+reverse
       
#       #hello == olleh 
#       #mom == mom     
# if word == reverse:
#     print("it's Palindrome")
# else:
#     print("it's not Palindrome")



# for i in range(10):
#     print(i)

# i = 0
# while True:
#     if i < 30:
#         i = int(input("Enter n number:-"))
#         print(i) 


# while True:
#     n = int(input("Enter an number:-"))
#     if n % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")
#     ch = input("Enter yes to repeat:-")
#     if ch !='yes':
#         print("You are Done")
#         break


# while True:
#     try:
#         n1 = float(input("Enter an ist number:-"))
#         op = input("Enter an operator(+,-,*,/)")
#         n2 = float(input("Enter an second number:-"))

#         if op == '+':
#             print(n1+n2)
#         elif op == '-':
#             print(n1-n2)
#         elif op == "*":
#             print(n1*n2)
#         elif op == '/':
#             print(n1/n2)
#         else:
#             print("Invalid Operator")
#     except ZeroDivisionError:
#         print("Cant Divide by zero")
#     choice = input("Enter yes to repeat")
#     if choice != 'yes':
#         print("You are done")
#         break
   
   
#Function is a block of code, its used for specific task, its reusable
# def add():
#     a = 10
#     b = 12
#     print(a+b)
# add()




# from index2 import add
# #20
# n1 =int(input("Enter ist number:-"))
# #10
# n2 =int(input("Enter second number:-"))
# add(n1,n2)

# print()



# def evenodd(n):
#     if n % 2 == 0:
#         print("Even number")
#     else:
#         print("Odd number")

# #8
# num = int(input("Enter an number:-"))
# evenodd(num)


# def check(x):
#     if x > 0:
#         print("Positive number")
#     elif x < 0:
#         print("Negative number")
#     else:
#         print("You enterred zero")
    
# num = int(input("Enter an number:-"))  
# check(num)


# def sq(x):
#     return x*x*x

# num = int(input("Enter an number:-"))
# print(sq(num))


#lamda function is an anomous function which we for small tasks 
# add = lambda x,y: x+y

# n1 = int(input("Enter ist number:-"))
# n2 = int(input("Enter second number:-"))
# print(add(n1,n2))



# evenodd = lambda x: 'even' if  x %2==0 else 'odd'
# n = int(input("Enter an number:-"))
# print(evenodd(n))



#map is used for iteration
# num=[2,5,9,6,8]
# sq = list(map(lambda x: x**2, num))
# print(sq)

# num =['11','22','78','89','101','67']
# st = list(map(int,num))
# print(st)

# names = ['BOB','ALIC','JOHN','AIMAN','KHAN']
# st = list(map(str.lower,names))
# print(st)


# num=[2,3,4,5,6,7,8,9]
# st = list(filter(lambda x: x%2==0,num))
# print(st)


# num = [-21,-3,87,56,11,19,-89,-67]
# st = list(filter(lambda x: x <0,num))
# print(st)

# fruit=['Banana','apple','kiwi','mango','cherry']
# st = list(filter(lambda x: len(x)>5,fruit))
# print(st)


# for i in range(5): #outer loop
#     for j in range(3):  #inner
#         print(i)
        
        
# for i in range(5):
#     print()
#     for j in range(3):
#         print("Hello world",end=" ")
        

