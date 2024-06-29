'''
# Laptop Manufacture Factory
# Create a class Laptop Add constructor with
the attributes DeviceName, Processor, InstalledRam,
DeviceID, ProductId, SystemType, ManufuctureDate.
# Create a method to print the laptop details.

Manufacture 5 laptops objects by taking inputs from the user
 and pass the values to the class blueprint.
'''
class Laptop:
    def __init__(self,deviceName,processor,installedRam,deviceID,productId,systemType,manufuctureDate) :
        self.deviceName=deviceName
        self.processor=processor
        self.installedRam=installedRam
        self.deviceID=deviceID
        self.productId=productId
        self.systemType=systemType
        self.manufuctureDate=manufuctureDate

    def printDetails(self):
        print(f'\nDeviceName={self.deviceName}\n Processor={self.processor}\n InstalledRam={self.installedRam}\nDeviceID={self.deviceID}\n ProductId={self.productId}\n SystemType={self.systemType}\nManufuctureDate={self.manufuctureDate}\n--------------------\n')    


l1=Laptop(" Dell XPS 15","Intel Core i7-10750H"," 16GB DDR4"," XYZ123","DELLXPS15-2024","Windows 10 Pro 64-bit"," 2023-06-15")
l2=Laptop("MacBook Pro 13","Apple M1 Pro","16GB unified memory","JKL345","MACBOOKPRO13-2024","macOS Monterey","2023-10-05")
l3=Laptop("HP","Intel","64GB","klj12","hp-2021","window","2021-03-12")
l4=Laptop("Lenovo","Intel","128GB","klj12","lenovo-2021","window","2022-03-12")
l5=Laptop("Dell","Intel","64GB","klj12","dell-2021","window","2020-03-12")

l1.printDetails()
l2.printDetails()
l3.printDetails()
l4.printDetails()
l5.printDetails()