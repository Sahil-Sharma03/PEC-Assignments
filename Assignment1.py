#First Question , Program to find the average of three numbers
print ("First Question \n")
print ("Finding Average of any three number feeded by the user") 
_1st_Number= input("Enter the first number: ")
_2nd_Number= input("Enter the second number: ")
_3rd_Number= input("Enter the third number: ")
avg = (int(_1st_Number)+int(_2nd_Number)+int(_3rd_Number))/3
print("The average of three numbers is: \t ", avg,"\n") 

# Second Question , Program to compute a person's income tax
print ("Second Question \n")
print ( "Computing a Person's Income Tax ")
print ( "All Taxpayers are charged a flat rate of 20%")
print ( "All taxpayers are allowed a standard Deduction of 10k dollars")
print ( "For each dependent , a taxpayer is allowed an additional 3k dollars reduction")
GrossIncome = float(input("Enter your Gross income: "))
Dependents = int(input("Enter number of dependents: "))
print ( "Taxable Income = Gross Income - Standard Deduction - (Dependent Deduction* No of Dependents)")
Taxable_Income = (GrossIncome - 10000 -(3000*Dependents))
print ( "Taxable Income =" , Taxable_Income)
Tax = Taxable_Income*0.2
if (Tax>0) :
    {print("Income Tax is: ", Tax , "\n")}
else :
    {print ("No Tax , Income Must be Greater \n ")}

# Third Question , Program to store different Data type values
print ("Third Question \n")
print ( "Storing Different types of Data types into a list") 
Student1 =  [ '21104019', "Sahil", "M", "Electrical Engineering", 9.8]
print(Student1 , "\n") 

# Fourth Question ,Program to enter marks of 5 students and sort them
print ("Fourth Question \n")
print ("Entering Marks and Sorting them")
_1st_Student= input("Enter marks of First Student \t")
_2nd_Student= input("Enter marks of Second Student \t")
_3rd_Student= input("Enter marks of Third Student \t")
_4th_Student= input("Enter marks of Fourth Student \t")
_5th_Student= input("Enter marks of Fifth Student \t")
Marks = [ _1st_Student , _2nd_Student ,_3rd_Student , _4th_Student, _5th_Student]
print ( " Marks Entered are \t", Marks)
Marks.sort()
print("Sorted Marks =" , Marks ,"\n") 

# Fifth Question (a) Program to print list after removing 4th Element
print ("Fifth Question \n Color ['Red' , 'Green' , 'White' , 'Black' , 'Pink' , 'Yellow'] \n")
Color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print ("(a) Program to remove specified list after removing 4th element")
Color.pop(3)
print("New list of Color is" ,Color , "\n")

# Fifth Question (b) Program to remove 2 colours and replace them with one
print ("(b) Program to remove Black and Pink and Replace with Purple")
Color[3] = 'Purple'
print("New List of Color is " , Color , "\n Thank You")
