# Python Assignment 2 for Introduction to Computing
# Question 1 A python code for changes in String
print ("Question Number 1 \n")
Line = "Python is a case sensitive language"
print ("The input string is given as :" , Line)

# (a) Finding the length of the input string
print (" (a) \t The length of the given string is :" , len(Line),"\n")

# (b) Reversing the given input string
print (" (b) \t The input string in reverse can be seen as :", Line[::-1] , "\n")

# (c) Using slice function , store "a case sensitive" in new string
NewLine = Line[10:26]
print (" (c) \t The new String formed is :" , NewLine , "\n" )

# (d) Replace "a case sensitive" with "object oriented"
Line1 = Line.replace("a case sensitive","object oriented")
print ( " (d) \t The new String after replacement is :", Line1 , "\n")

# (e) Finding the index of substring "a"
print ( " (e) \t The index of substring 'a' is",Line.index("a") , "\n")

# (f) Removing the White subspaces from the input string
print ("  (f) \t The String after removing White spaces can be seen as: " , Line.replace(" ",""),"\n \n")

# Question 2 : Storing the information as different types of variables.
print ("Question Number 2 \n \t Enter your Details as asked")
Name = input("Enter Your Name : \t")
SID = input("Enter Your Student Id : \t")
Department = input("Enter your Deparment Name : \t")
CGPA = input("Enter your CGPA : \t")
print ("Hey, ",Name,"Here! \n My SID is ",SID,"\n I am from ",Department," and my CGPA is ",CGPA,"\n")

# Question 3 : Bitwise Operators
#       32  16  8   4   2   1
#a=56 = 1   1   1   0   0   0
#b=10 = 0   0   1   0   1   0
print ("Question Number 3 \n")
a= 56
b= 10
print (" (a) a&b = " , a&b)
print (" (b) a|b = " , a|b)
print (" (c) a^b = " , a^b)
print (" (d) Left shift both a and b with 2 bits \n \t a<<2 =",a<<2,"\n \t b<<2 =",b<<2)
print (" (e) Right shift a with 2 bits and b with 4 bits \n \t a>>2 =",a>>2,"\n \t b>>4 =",b>>4)

# Question 4 : Program to find the greatest numbers from the input
print ("Question Number 4 \n")
print ("To find the greatest numbers from the input")
Num_1 = int(input("Enter first Number :"))
Num_2 = int(input("Enter Second Number :"))
Num_3 = int(input("Enter Third Number :"))

if Num_1 > Num_2 and Num_1 > Num_3:
    print (Num_1 ,"Is the greatest Number \n")
elif Num_2 > Num_1 and Num_2 > Num_3 :
    print (Num_2 ,"Is the greatest Number \n")
else :
    print (Num_3 ,"Is the greatest Number \n")

# Question 5 : Program to Check if name is present in the string entered by user
print ("Question Number 5 \n")
YourSTRING = input("Enter any Statement :")
if "name" in YourSTRING :
    print ("Yes")
else :
    print ("no")

# Question 6 : To check if the triangle can be formed through input sides
print ("Question Number 6 : \t Can a Triangle be Formed? \n")
Side1 = int(input("Enter First Side :"))
Side2 = int(input("Enter Second Side :"))
Side3 = int(input("Enter Third side :"))
if Side1 <(Side2 + Side3) and Side2 <(Side3 + Side1) and Side3 <(Side1 + Side2) :
    print ("yes")
else :
    print ("no")
