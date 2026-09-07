#This is comment

#arthmatic operators
# a = 12
# b =10
# print(a+b)

# a = 12
# b = 11
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


#exponent
# a = 3
# print(a**4)

#floor division
# a = 9
# b =2
# print(a//b)



#Relationa operator
# a = 10
# b = 10
# print(a==b)

# a = 12
# b = 12
# print(a!=b)

# a = 21
# b =29
# print(a<b)

# age = 18
# print(age>=18)


# age = 15
# print(age<=15)


#Assignment Operators
# a = 10

# a = 21
# # a = a+4
# a+=4
# print(a)


# a = 13
# a-=3
# print(a)




#Data-Type tells us which type of value a particular variable holds
#int --- means a variable holds numerical data
#string -- holds textual data
#float --- holds decimal value
#bollean -- holds True/False value



# a = 12
# print(type(a))

# b = "Tanfeez"
# print(type(b))


# c = 12.89
# print(type(c))

# d = True
# print(type(d))


#list stores multiple item into single variable, its ordered, its mutable("Changeble") it allow duplicate value
#index is numerical representation of position of item in list
# lt =['wasiq',12,78,True,'khan']
# lt[0]='tanfeez'
# lt.append('abdul')  #add by value
# lt.insert(1,'Madeeha')  #add by index
# lt.remove('khan')  #delete by value
# lt.pop(4)  #delete by index
# print(lt)


#Tuple stores multiple item in single variable, its orederd, its indexed, it allow duplicate value, its im mutable(un-changeble)
# tp =('wasiq','Tanfeez','Khan',121,56,101)

# print(tp[0])



#set sores multiple item in single variable, its unorderd, its un-indexed, its sometimes mutable and sometimes im mutable
# st = {'Tanfeez','Abdul',29,True}
# st.add("Madeeha")
# st.remove("Tanfeez")
# print(st) 


#Dictionary store multiple items in single variable, it stores item through process of key value pairs, its ordered

# dt ={
#     "Name":'Tanfeez',
#     "roll-no":21,
#     'adress':'Khanyaar'
# }
# dt['Name']='Aahil'  #update in dictionary
# dt['Email'] = 'k@gmail.com'  # Add in dictionary
# dt.pop('roll-no') #here we delete by pop
# del dt['Name']  #here we delete by del
# print(dt)



# lt = ['wasiq','khan',True,'abdul','innam',23,69]
# # print(lt[-2])
# # print(lt[1:4])
# print(lt[2:])
# print(lt[:4])


# age = int(input("Enter your age:-"))
# if age>=18:
#     print("You can vote")
# else:
#     print("You cannot vote")


# grade = input("Enter your grade:-")

# if grade == 'A':
#     print("Topper")
# elif grade =='B':
#     print("Good")
# elif grade =='C':
#     print("Average")
# else:
#     print("Fail")

#And, Or

# b_age  = 19
# g_age = 17

# if b_age>21 or g_age>16:
#     print("You are allowed")
# else:
#     print("You are  not allowed")


# n1 = int(input("Enter ist number:-"))
# op=input("Enter your operator(+,-,*,/)")
# n2 = int(input("Enter second number:-"))

# if op =='+':
#     print(n1+n2)
# elif op == '-':
#     print(n1-n2)
# elif op=='*':
#     print(n1*n2)
# elif op =='/':
#     print(n1/n2)
# else:
#     print("invalid operator")


# n1 = int(input("Enter an number:-"))
# if n1> 0:
#     print("Positive number")
# elif n1 ==0:
#     print("Zero number")
# else:
#     print("Negative number")

# x = int(input("Enter an number:-"))
# if x % 2==0:
#     print(x,"is even number")
# else:
#     print("odd number")



# print("I m in ils")
#loop is a program that runs multiple time untill it met a specific condition
#i=0
# for i in range(2,10,2):
#     print(i)

#break keyword simply break the iteration
# for i in range(10):
#     if i ==5:
#         break
#     print(i)
    
#continue mean simply skip a particular iteration
# for i in range(10):
#     if i == 6:
#         continue
#     print(i)


# lt=['wasiq',12,89,81,11,14.78,True]
# for d in lt:
#     if d == 'wasiq':
#         continue
#     print(d)


# dt ={
#     "name":"Tanfeez",
#     "pin-code":190001,
#     "adress":"Khanyar"
# }
# # print(dt,'is is')
# for key,value in dt.items():
#     print(key,':-',value)


# tab = int(input('Enter an number:-'))
# for i in range(1,11):
#     res = tab*i
#     print(tab,'X',i,'=',res)

#6
#7
#5
# x = int(input("Enter an number:-"))
# if x <=1:
#     print("Not Prime!")
# else:
#     for i in range(2,x):
#         #6%2 ==0
#         #5/2 = =0
#         #5/3 ==0
#         #5/4==0
#         if x%i ==0:
#             print(x,"is not Prime!")
#             break
    
#     else:
#         print(x,"Prime number")



# lt = [23,89,10,11,56,34,111]
# n = int(input("Enter an number:-"))
# flag =0
# for num in lt:
#     if n == num:
#         flag=1
        
# if flag ==1:
#     print(n,"is in list")
# else:
#     print(n, 'is not in list')
        
        
#hello
#mom
# word =input("Enter an word:-")
# rev = ''

# for ch in word:
#     # = h + '' =h
#     #h = e + h = eh
#     #eh = l + eh = leh
#     #leh = l +leh = lleh
#     #lleh = o + lleh = olleh
#     # rev =olleh
#     #'' = m + '' = m
#     #m = 0 + m = om
#     #om = m + om = mom
#     rev = ch + rev
#     #olleh ==hello
    
# # if rev == word:
# #     print(word,"is Palindrome")
# # else:
# #     print(word,'is not palindrome')


# a = 'wasiq'
# a[2]='m'
# print(a[2])

# a= 15
# b = 25
# c = a
# a =b
# b =c
# print(a,b)

# a = 12
# b =25
# a,b = b,a
# print(a,b)
# for i in range(10):
    

# i = 0
# while i <30:
#     i=int(input("Enter an number:-"))
#     print(i)
    
    
# while True:
#     x = int(input("Enter an number:-"))
#     if x % 2 ==0:
#         print("Even number")
#     else:
#         print("Odd number")
#     ch = input("Enter yes to repet:-")
#     if ch !='yes':
#         break



# while True:
    # n =int(input("Enter an number:-"))
    # if n <=1:
    #     print("Not Prime")
    # else:
    #     for i in range(2,n):
    #         if n % i ==0:
    #             print("Not Prime")
    #             break
    #     else:
    #         print("Prime number")
    # cht = input("Enter no to exit:-")
    # if cht == 'no':
    #     break
    
    
    

# while True:
#     word = input("Enter an word:-")
#     rev =''
#     for ch in word:
#         rev = ch+rev

#     if rev == word:
#         print(word,'Is palindrome')
#     else:
#         print(word,'Not palindrome')
        
#     xz = input("Enter yes to continue:-")
#     if xz != 'yes':
#         break




# while True:
#     n1 = int(input("Enter an number:-"))
#     op = input("Enter an operator(+,-,*,/)")
#     n2 = int(input("Enter an number:-"))
    
#     if op == '+':
#         print(n1+n2)
    
#     elif op == '-':
#         print(n1-n2)
    
#     elif op == '*':
#         print(n1*n2)
    
#     elif op == '/':
#         print(n1/n2)
#     else:
#         print("Invalid Operator")
#     cht = input("Enter yes to continue")
#     if cht!='yes':
#         break


#funtion is a block of code that we use multiple time and its also reusable and maintain code formation
# def add():
#     a = 10
#     b=25
#     print(a+b)

# add()


#Argument passing means when we pass an value to and implementation of function from where it get called
# def add(x,y):
#     print(x+y)
    

# a = int(input("Enter an number:-"))
# b=int(input("Enter an number:-"))
# add(a,b)

#Local  variable is a variable that we can only acess from block of code and can't be acessed from the outside of the block
#Global variable means the variable that we can acess from anywhere
# a = 20
# def ok():
#     print(a)
# ok()



# def sq(x):
#     print(x*x)

# n = int(input("Enter an number:-"))
# sq(n)

# def even_odd(x):
#     if x % 2 ==0:
#         print(x, 'Even number')
#     else:
#         print(x, 'odd number')
    


# k = int(input("Enter an number:-"))
# even_odd(k)



# def pos_neg(x):
#     if x>0:
#         print(x, 'Positive number')
#     elif x == 0:
#         print('You entered', x)
#     else:
#         print(x, 'Negative Number')



# l = int(input("Enter an number:-"))
# pos_neg(l)



# from index1 import add, primeNo, Palindrome

# # add(12,13)

# # n =int(input("Enter an number:-"))    
# # primeNo(n)

# word = input("Enter an word:-")
# Palindrome(word)



# def add(a,b):
#     return a+b


# ap=add(12,11)
# print(ap)

#lambda is anmoyns function that is smilar to function but its used for smaller tasks

# add = lambda x,y: x+y

# print(add(12,11))


# sq = lambda x: x*x
# print(sq(3))


# even_odd = lambda x : 'even' if x % 2==0 else 'odd'

# print(even_odd(4))


# lt =[2,3,4,5,6,7,8]
# sq = list(map(lambda x: x*x,lt))
# print(sq)


# num =['11','12','13','14','15','16','17']
# n1 = tuple(map(int,num))
# print(n1)


# a= 'wasiq'
# print(str.capitalize(a))
# print(str.upper(a))

# names =['BOB','ALICE','KAHN','ABDUL']
# n = list(map(str.lower,names))
# print(n)

# names = ['wasiq','khan','umer','mueen']
# n  = tuple(map(str.upper,names))
# print(n)


# lt =[1,2,3,4,5,6,7,8,9,10]
# e = list(filter(lambda x : x %2 ==0, lt))
# print(e)

# num =[-21,11,-90,-11,-34,56,70,90]
# f  =  list(filter(lambda x: x<0,num))
# print(f)



# fruits = ['Banana','Apple','Kiwi','Mango','Pineapple']
# sq = list(filter(lambda x: len(x)>4,fruits))
# print(sq)


#Exception handling means to handle an error smothly

# try:
#     a = 10
#     b=0
#     print(a/b)
# except ZeroDivisionError:
#     print("Cant divide by zero")


#value error
# try:
#     num = int(input("Enter an number:-"))
#     print(num)
# except ValueError:
#     print("Invalid format")

#Type error
# try:
#     a = 22
#     b ='10'
#     print(a+b)
# except TypeError:
#     print("Cant add str and int")

#Name Error
# try:
#     print(a)
# except NameError:
#     print("This variable is not declared")




# try:
#     lt = [51,11,67,32]
#     print(lt[8])
# except IndexError:
#     print("This index doesnt belong in list")

# try:
#     dt={
#         "Name":"wasiq"
#     }

#     print(dt['roll-no'])
# except KeyError:
#     print("This key doesnt exist")

# try:
#     a = 'wasi'
#     a.append('q')
#     print(a)
# except AttributeError:
#     print('This attribute doesnt exist here!')


# for i in range(5):
#     print()
#     for j in range(3):
#         print("Hello")



# lt=['wasiq','abdul','khan','ubaid']
# s = list(map(str.capitalize,lt))
# print(s)


#file handling means to read and write data into file
#w -- creating a file
#r -- reading a file
#a -- update the file

# f = open('file.txt','w')
# f.write("Hello world")
# f.close()


# f = open('file.txt','r')
# data = f.read()
# print(data)

# file = open('file.txt','a')
# file.write(", from Wasiq")
# file.close()

# f = open('file.txt','w')
# f.write(', and from tanfeez')
# f.close()


# f = open('tan.txt','x')
# f.write('Hello world')
# f.close()

#Modern way of handling a file

# with open('piku.txt','w') as f:
#     f.write("Ok")


# with open('piku.txt','r') as f:
#     d=f.read()
#     print(d)


# with open('piku.txt','a') as f:
#     f.write(' sir')


# with open('khan.txt','w+b') as f:
#     f.write(b"I am khan")

# with open('khan.txt', 'r+b') as f:
#     d = f.read()
#     print(d)






# with open(r"C:\Users\Dell\Desktop\Hello\wasiq.txt",'w') as f:
#     f.write("Hello world!")




#object oriented programming is a programming paradigm that uses objects and classes in programming. It aims to implement real-world entities like inheritance, polymorphisms, encapsulation, etc in the programming. The main aim of OOP is to bind together the data and the functions that operate on them so that no other part of the code can access this data except that function.


#oops has 4 pillars
#Encapsulation
#abstraction
#inheritence
#polymorphism

#class is a blueprint or template that is used to create an object

# class ils:
#     def hello(self):  #here self means refrence or adress of an object
        
#         print("Hello from ils")
    
#     def info(self):
#         print('Are you coming')

    
#     def bye(self):
#         print("Are you coming back?")
        

# i = ils()  #object is instance of class
# i.hello()
# i.info()
# i.bye()

#encapsulation means binding of data
#abstraction means hiding the complexity your code


#polymorphism means same function diffrent behaviour
# class Cat:
#     def speak(self):
#         print("Meow Meow")
        
# class Dog:
#     def speak(self):
#         print("Bow Bow")
        
# c = Cat()
# d = Dog()
# c.speak()
# d.speak()


#ineretence means acessing properties from parent to child class
# class Animal:
#     def wild(self):
#         print("Lion is king jungle")
        

# class Dog(Animal):
#     def Behaviour(self):
#         print('dog is friendly animal')
        




# d = Dog()
# d.Behaviour()
# d.wild()


#constructor is a method that automatically run when object of class is created
# class Ils:
#     def __init__(self):
#         print("Hello from constructor!")
    
#     def hello(self):
#         print("Hello i'am wasiq")
    
#     def bye(self):
#         print("Will meet you soon!")
        
# i = Ils()



# class dps:
#     def __init__(self):
#         print("Hello from constructor")
#         self.__bye()
    
#     def _hello(self):
#         print("Hello from protected function")
    
    
#     def __bye(self):
#         print("Hello from private function")
        
# d = dps()
# d._hello()

#Multiple inheritence means when we inherit properties from diffrent parent class
# class A:
#     def show(self):
#         print("This a is from A class")
        
# class B:
#     def display(self):
#         print("This is from Class B")
        
# class C(A,B):
#     pass

# ca = C()
# ca.show()
# ca.display()

        

#Method Resolution order means when two class have same attribute or method
# class A:
#     def show(self):
#         print("This is from class A")

# class B:
#     def show(self):
#         print("This is from class B")
        
        
# class C(A,B):
#     pass

# cc = C()
# cc.show()
# cc.show()



#Multilevel inheritence means base class is derived from anther from base class creating heirarchy

class A:
    def a_method(self):
        print("This is from class A")
        
class B(A):
    def b_method(self):
        print("This is from class B")
        
        
class C(B):
    pass

ob = C()
ob.a_method()
ob.b_method()