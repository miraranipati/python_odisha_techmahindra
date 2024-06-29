class Parent:
    family_name="shettys"

    def properties(self):
        print('Parent prot')

    def business(self):
        print("Parent bu") 

class Child(Parent):
    child_name="Mira"

    def child_pro(self):
        print("c p")

    def child_bus(self):
        print("c b")


obj1=Child()
print(obj1.family_name)
obj1.properties()
obj1.business()
obj1.child_pro()
obj1.child_bus()


               