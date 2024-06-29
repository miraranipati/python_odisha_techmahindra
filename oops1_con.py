#constructor
class Company:
    def __init__(self,empname,age,address,role,exp,phn):
        #set data mem
        # self.empname=empname  orther wise
        self.eName=empname
        #datamem=pass by value by tempory value
        self.age=age
        self.address=address
        self.role=role
        self.exp=exp
        self.phn=phn

        print("set done for",empname)
        # print("I am Constructor")

    def empDetails(self):
        return f'\n Emp name is {self.eName}\n age is {self.age}\n' 

    @staticmethod
    def greet():
        print("Good even")   

e1=Company("Rohan",25,"Bangalore","Python dev",2,'98757653479')
e2=Company("Raja",28,"BBSR","Python dev",7,'98757653479') 
print(e1.empDetails())
print(e2.age)
e1.greet()



# e1=Company()        
# e2=Company() 