# def reverse(num):
#     num=str(num)
#     return num[::-1]

# num=107
# print(reverse(num))

data=[]
com="tcs"
def emp(name,sal):
    bonus=1000
    print(f' company name is {com} Emp name {name} sal is {sal}')
    return sal+bonus

emp1=emp('abc',20000)
data.append(emp1)
emp2=emp('jkl',678)
data.append(emp2)

print(data)
print(sum(data))