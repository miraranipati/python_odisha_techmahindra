mynum=[1,2,3,4,8,7,6,5,3,2,11,20]
##print(type(mynum))
##mynum.sort()    ##asc
mynum.reverse()     ##desc

print(mynum)

###########----------------------
# chars=['b','A','d','z','c','r','K','Watermelon',"orange"]
# chars.sort()
# chars.reverse()
# print(chars)

#########---------------------------
# mydata=[1,2,3,9,0,8,'b','c','d','a']
# mydata.sort() ###errors
# print(mydata)

#############--------------------------
# mylist2=[]
# mylist2.append(0)
# mylist2.append(1)
# mylist2.append(2)
# mylist2.append(5)
# mylist2.append(3)
# print(mylist2)
# mylist2.insert(2,10)
# print(mylist2)
# mylist2.remove(2)
# print(mylist2)
# mylist2.pop()
# print(mylist2)

################----------------------------
mynum=[1,2,3,4,8,5,7,2,1,6,10,2]
print(mynum.count(2))
mynum.remove(2)
print(mynum.count(2))

#############=----------------
copyli=mynum.copy()
print('original',mynum)
print('copy',copyli)