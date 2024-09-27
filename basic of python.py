# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 10:51:34 2024

@author: dell
"""
########################

"""19-april-2024"""

########################
a=10
a
type(a)

a=2.4
a
type(a)

a=2+3j
a
type(a)

a="sam"
a
type(a)

# operator in python
#1-arithmatic operators
#2-logical operator
#3-relational operator



###########
#arithmatic operators 
a=38
b=10

#+
a+b
#-
a-b
#*
a*b
#/
a/b

#% modulus
#it is nothing but the reminder
a%b
#**  exponentiation
#power of the upper no. to the refernce power of lower
a**b

#// floor division
#only get the possible value or nearest value of result(exact),
#without fractional anwer
a//b

#relational operators
a>b   #grater than 
a<b   #smaller than
a==b   #equal to
a!=b   #not equal to

a=True
b=False
a&a
a&b
a|a
a|b
b|b

#####################

"""20-april-2024"""

#####################

#python tokens 

#keywords
#identifiers
#operators
#literals

#keywords in python
#True,False ,class,or,not,for,from,is,if,elif,return,
#def,del,nonlocal,global,yeild,and,finally,continue,none
#while,as,try

true=[1,2,3,4]
print(true)
#cannot assign keyword as dictionary,variables



#identifiers
#identifiers are case sensetive

Student="mustafa"
student="abhi"
print(Student)

#literals in python
#literal are  constant in python
#literal are not change


a="ms"
a=3.14
a=100
a=True
a=2+6j

#here 'ms',3.14,'100','True',2+6j all are the literals 

a="HEllo World"  #hello word is lirals

#python strings

#string is basically sequence of charater enclose in single quotes ,doublequotes,triple quotes
#single quotes('')
str1='this is python'
print(str1)
str1
#double quotes("")
str2="this is my second code "
print(str2)
str2

#triple quotes
str3="""
this is 
multi 
line of code
"""
str3
print(str3)

#indexing in python
#indexing is sequence of the charater's numeric values start from '0'

my_str='this is my code'
my_str[0]    #'t'
my_str[-1]   #'e'
my_str[4]   #' '

#for in range of the indexing in the given variables

my_str[4:10]   #'is my'

#finding length of the string
my_str="My name is mustafa"
len(my_str)

#conveting upper case 
my_str.upper()

#coverting lower case
my_str.lower()

#replacing of character in python
my_str.replace('a','u')
#replacing word from variable
my_str.replace('is','are')

my_str.replace('mustafa','pratik')



#cout of the literal
my_str="my my name is is mustafa 300 300 300"
len(my_str)

my_str.count('is')

my_str.count('300')

my_str.count("s")

##########################

"""22-april-2024"""

##########################

my_str="my name is ms,i have pc"
print(my_str)
#finding the value of sub string 
#index value is come out for find method
my_str.find("ms")
#slipt the string 
my_str.split()
#split by charater 
#ther is charater spliting
my_str.split('i')

#data structure in python
# 1.tuple
# 1.list
# 1.dictionary
# 1.set
#tuple
#around bracket
#tuple is heterogeoneous data stucture
##tuple is imutable/not change original value

tup1=(1,True,3.14,2+5j,"data")
type(tup1)

#extacting a data in tuple 
#tupl[]
tup1[0]  #1

tup1[-1] #data

tup1[1:4] #the last value in indexing is enclosive
#tuple are not mutable
tup1[1]=False
tup1
#lenghth of the tuple
len(tup1)
#addition/concatinate of two tuples
tup1=(1,True,3.14,2+5j,'data')
tup2=('ms',7.7,4,5+2j,"hello")
#the result  depends on sequence
tup1+tup2
tup1,tup2
tup2+tup1
tup2,tup1

#repate the tuple
tup1*5

tup1*3+tup2

#minimum value and maximum values in tuple
tup3=(3,4,5,6,7,8,9)
min(tup3)
max(tup3)

#list
#square bracket
#list is mutable/changeable
#list is heterogeneos
listl=[1,True,3.14,2+5j,'data']
type(listl)
#indexing of list
listl[0]

listl[-1]
#extracting data in tuple
#list are mutable 
listl[1]=False
listl

#lenght of the list
len(listl)

#addition of the tuple

l1=[1,2,3,4,5]
l2=[6,7,8,9,0]

l1,l2

l1+l2

l2,l1

l2+l1

#minimum and maximum value in  tuple
min(l1)
max(l1)

#mutable list
l1[1]="data"
l1
#appending a value in list
l1.append('data')
l1

#poping a value from list
l1.pop(2)
l1
l1.pop()
l1

#inserting of the list
L1=["banana","gauva","mango","apple"]
L1.sort()
L1


#revesing of the list
L1.reverse()
L1

#inseting in the list
#insertion in list
L1.insert(1,"chicku")
L1

L1.insert(3,"orange")
L1

#multiply of list
L1*2

#dictionary in data structure
#curly bracket/braces
#heterogeneous
#mutable

d1={"apple":100,"mango":80,"banana":40,"gauva":30}
type(d1)

d1.keys()

d1.values()
#adding a value in dictionary
d1["chicku"]=90
d1
#changing existing value 
d1["mango"]=60
d1

#fuctions in dictionary
#updating a dictionry with other

d1={"apple":100,"mango":80}
d2={"banana":40,"gauva":30}
d1.update(d2)
d1

#poping a keys from dict
d1.pop("gauva")
d1


#set 
#curly braces
#sets are unordered and unindex collection of data
#sets are mutable 
#duplicates are not allowed in sets


s1={1,3.34,"data",1+4j}
s1

type(s1)
#repetition is not allowed in sets
s1={1,3.34,"data",1+4j,1,3.34}
type(s1)
s1
#addition of element in sets
s1.add("mustafa")
s1
s1.add("ms")
s1
s1.add(False)
s1

##########################

"""23-april-2024"""

##########################
#updating a list in set
s1.update([21,5+7j,"Hello",False])
s1

#remove elementb from list
s1.remove("data")
s1
s1.remove("ms")
s1
s1.remove('Hello')
s1

#union in set 
#addition in sets 
s1={1,2,3}
s2={"a","b","c"}
s1.union(s2)

#union of two sets having same elements

s1={1,2,3}
s2={2,3,4}
s1.union(s2)

#intersetion of two sets
s1.intersection(s2)


s1={"a","b","c","d","e"}
s2={"c","d","a"}

s1.intersection(s2)

#if else statment
a=20
b=30

if a>b:
    print("a is greter than b")
    
else:
    print("b is greter than a")    

#if....elif...else statement
a=70
b=80
c=30
if (a>b) & (a>c):
    print(" a is greatest")
    
elif (b>a) & (b>c):
    print("b is greatest")
    
else:
     print("c is greatest")    

#tuple with if...else

tup1=("a","b","c","d","e")

if 'data' in tup1:
    print("data is present")
    
else:
    print("data is not present")


#list with if.....else
l1=["a","b","c","f","e","f","g"]
if l1[3]=='d':
     print("index is correct")

else:
    print("index is incorrect")



#if.....else
l2=['a','b','c','d','e']
if l2[3]=='d':
   l2[3]='a'
l2 


#dictionary with if.....else condition

d1={"A":30,"B":40,"C":90}
if d1['A']==30:
    d1['A']=d1['A']+100
d1    

#looping statment 
#looping is repetion of task 
#while loop
i=1
while i<=10:
    print(i)
    i=i+1
      
i=1
while i<=10:
    print(i)
    i=i+2

i=2
while i<=10:
    print(i)
    i=i+2

i=1
n=2
while i<=10:
    print(n," * ",i," = ", n*i)
    i=i+1

i=1
n=2
while i<=10:
    print(n*i)
    i=i+1

#while loop with list

#adding in list by while loop
l1=[1,2,3,4,5]
i=0
while i<len(l1):
       l1[i]=l1[i]+100
       i=i+1
       l1

#for loop 
#for lopp is used to iterate over a sequence

l1=["mango","gauva","apple","watermelon"]
#for loop impliment
for i in l1:
    print(i)


#list with fro loop
#define a list
l1=["mango","apple","gauva","cherry"]
#for loop
for i in l1:
    print(i)

#nested for loop 
#for loop inside for loop
l1=["red","white","blue"]
l2=["laptop","shirt","bike"]
for i in l1:
    for j in l2:
        print(i,j)

#fuction define 
#fuction is basically block of code which perform specific task
#def means defination 
def hello():
    print("hello mustafa")
hello()

#fuction with return
def add_10(x):
    return x+10
add_10(8)

#define a fuction 
def hii():
    print("mustafa is good player")
hii()    


#return function 
def sub_A(x):
    return x+40
sub_A(5)

##fuction as mul
def mul_m(y):
    return y*20
mul_m(2)

#fuction as divide
def div_c(w):
    return 10/w
div_c(100)

#fuct for power of fuction
def power_(q):
    return q**10
power_(2)

#even odd fuction for even odd number determination
def even_odd(x):
    if x%2==0:
        print(x," is odd number")
    else:
        print(x," is even number")
even_odd(5)
even_odd(8)

#prctice for even odd number
def odd_even(g):
    if g%2==0:
        print(g,"is even number")
    else:
        print(g,"is odd number")
odd_even(99)        
odd_even(104)


def odd_even(o):
    if o%2==1:
        print(o,"is odd number")
    else:
        print(o,"is even number")
odd_even(333)
odd_even(18)


########
#lambda fuction
g=lambda x:x*x*x
g(10)

##lambda with filter 
#lambda fuction parameter 
#list second paramer 
#filter takes two parameters 
#1.lambda,2.list
#list is coveting original list
#for odd numbers
l1=[1,2,3,4,5,6,7,8,9,0]
final_list=list(filter(lambda x:(x%2!=0),l1))
final_list
#for even numbers
l1=[87,98,67,54,65,61,34,48,90,91,28]
final_list=list(filter(lambda x:(x%2==0),l1))
final_list

#lambda with map
#map is used for all individual element for map 
#multiply by map fuction
l1=[1,2,3,4,5,6,7,8,9,0]
final_list=list(map(lambda x:(x*2),l1))
final_list
#square of all the elements from the list
l1=[1,2,3,4,5,6,7,8,9]
final_list=list(map(lambda x:x**2,l1))
final_list

#reduce
#reduce fuction :consilidate result by sequal
#fro sum operation
#y,x
l1=[1,2,3,4,5,6,7,8,9]
from  functools import reduce
sum=reduce(lambda x,y:x+y,l1)
sum
#x,y
l1=[1,2,3,4,5,6,7,8,9]
from  functools import reduce
sum=reduce(lambda x,y:x+y,l1)
sum

#sub operation
l1=[1,2,3,4,5,6,7,8,9]
from functools import reduce
sub=reduce(lambda y,x:x-y,l1)
sub

#for multiplication
l1=[1,2,3,4,5,6,7,8,9]
from functools import reduce
mul=reduce(lambda x,y:x*y,l1)
mul

#for division
l1=[1,2,3,4,5,6,7,8,9]
from functools import reduce
div=reduce(lambda x,y:y/x,l1)
div
#y,x
l1=[1,2,3,4,5,6,7,8,9]
from functools import reduce
div=reduce(lambda y,x:y/x,l1)
div


#########################

#OBJECT ORIENTED PROGRAMIN

#class in python
#class is user define data type

#object in python
#object are specific instance of data type

class Phone():
    def make_call(self):
        print("i am making a call")
    def play_games(self):
        print("i am plying a games")
        
p1=Phone()        
p1.make_call()
p1.play_games()        
        
#ex.2
Phone()
Phone().make_call()
Phone().play_games()

###############################

class cricket():
    def Batsmen(self):
        print("i am batsmen")
    def Boler(self):
        print(" i am boller")
        
c1=cricket()
c1.Batsmen()
c1.Boler()


######################
















