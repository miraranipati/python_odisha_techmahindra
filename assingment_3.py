'''
1 .Take a inputs and Evaluate the expressions
a)Take the Students name
b)Take the student English marks
maths, science, social, tamil, hindi
 while taking the inputs it should be in the range (0-100)
c)calculate the % and print
% <35% print fail and print the Grade 'F'
% >=35% and <55% print just pass and print the Grade 'D'
% >=55% and <60% print  pass and print the Grade 'C'
% >=60% and <75% print  average and print the Grade 'B'
% >=75% and <90% print  good and print the Grade 'A'
% >=90% and <100% print  excellent  and print the Grade 'A+'
'''

# #1  if elif else
# name=input("Enter Student Name:\n")

# mark=[]
# english=int(input("Enter english mark it should be in the range (0-100)\n"))
# mark.append(english)
# maths=int(input("Enter maths mark it should be in the range (0-100)\n"))
# mark.append(maths)
# science=int(input("Enter science mark it should be in the range (0-100)\n")) 
# mark.append(science)
# social=int(input("Enter social mark it should be in the range (0-100)\n"))
# mark.append(social)
# tamil=int(input("Enter tamil mark it should be in the range (0-100)\n"))
# mark.append(tamil)
# hindi=int(input("Enter hindi mark it should be in the range (0-100)\n"))
# mark.append(hindi)

# percentage=sum(mark)/6
# print(percentage)

# if(percentage>=90 and percentage<100):
#     print("Excellent")
#     print("Grade 'A+'")
# elif(percentage>=75 and percentage<90): 
#     print("Good")
#     print("Grade 'A'")
# elif(percentage>=60 and percentage<75):
#     print("Average")
#     print("Grade 'B' ") 
# elif(percentage>=55 and percentage<60):
#     print("Pass")
#     print("Grade 'C'") 
# elif(percentage>=35 and percentage<55):
#     print("Just Pass")
#     print("Grade 'D'")  
# elif(percentage<35):
#     print("Fail")
#     print("Grade 'F'") 
# else:
#     print("Invalid")

'''
# 2)write a 4 functions
a)to find the area of circle
b) to find the area of rectangle
c)to find the area of square
d)find the area of triangle
take the inputs from the user for all 4 operation
'''

# # 2)a) area of circle
# def areaOfCircle(r):
#     area=3.14*r*r
#     return area

# radius=int(input("Enter radius of Circle\t"))
# area=areaOfCircle(radius)
# print(f'Area of circle is {area}')

# #2)B)area of rectangle
# def areaOfRectangle(l,w):
#     area=l*w
#     return area

# length=int(input("Enter length of rectangle\t"))
# width=int(input("Enter width of rectangle\t"))
# area=areaOfRectangle(length,width)
# print(f'Area of rectangle is {area}')

# #2)c)area of square
# def areaOfSquare(length):
#     area=length*length
#     return area

# length=int(input("Enter length of square\t"))
# area=areaOfSquare(length)
# print(f'Area of square is {area}')

# #2)d)area of triangle
# def areaOfTriangle(base,height):
#     area=(base*height)/2
#     return area

# base=int(input("Enter base of triangle\t"))
# height=int(input("Enter height of triangle\t"))
# area=areaOfTriangle(base,height)
# print(f'Area of triangle is {area}')

'''
3. Write a python program
 to take the inputs of two employees  
     EmployeeName    EmployeeSalary    and return its salary & employeename. 
  Add bonus of 10% of its salary and credit to his account.  
Add emp1 and emp2 salaries with bonus and store it into salarydetails list

'''


salaryDetails=[]
def employeeDetails(name,salary):
    bonus=0.1*salary
    print(f'Employee name {name} sal is {salary}')
    return salary+bonus


emp1=employeeDetails('Raj',50000)
salaryDetails.append(emp1)
emp2=employeeDetails('Lisa',600000)
salaryDetails.append(emp2)

print(salaryDetails)
