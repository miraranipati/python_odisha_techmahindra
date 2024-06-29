# number=[1,2,3,4,5]
# res=list(map((lambda x:x**2),number))
# print(res)

def sq(a):
    return a*a

def cube(a):
    return a*a*a

function=[sq,cube]
num=[2,3,4,5,7]

for i in num:
    res=list(map((lambda x:x(i)),function))
    print(res)

