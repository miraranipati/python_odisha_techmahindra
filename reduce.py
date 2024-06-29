from functools import reduce

x=[1,2,3,4,5,6] 
# list i can iterate these values
# syntax reduce(function),iterable)
res=reduce((lambda x,y:x*y),x)
print(res)

'''
x=[1,2,3,4,5,6] x=1 y=2 y:1*2 y=2
x=[2,3,4,5,6]   x=2 y=3 y:2*3 y=6
x=[3,4,5,6]....

'''
# x=
x=()

