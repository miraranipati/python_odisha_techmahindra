'''
OOP: Object Oriented Programing

Class Human: adam
    datamembers:variables   name,age,gender
    methods:function        eat(),sleep(),walks()


'''

# class Employee:
#     #initialise the data members
#     companyName='GUVI'
#     since='1995'

#     #method is intialise
#     def companyDetails(self):
#         return f"Company name is {self.companyName}\nSince{self.since}"
    
# #create obj for class company
# e1=Employee()
# print(e1.companyDetails())
# e2=Employee()
# print(e2.companyDetails())
# e3=Employee()
# print(e3.companyDetails())        




class Employee:
    #initialise the data members
    companyName=None
    since=None

    #method is intialise
    def companyDetails(self):
        return f"Company name is {self.companyName}\nSince{self.since}"
    
#create obj for class company
e1=Employee()
e1.companyName="Infocys"
e1.since=2001
print(e1.companyDetails())
e2=Employee()
print(e2.companyDetails())
e3=Employee()
print(e3.companyDetails())    