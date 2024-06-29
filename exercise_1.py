
mylist=[23,4,5,6,7,8,1,2,3,9,0,122,10,2,3,4,3,3,2]
##1
#a
print(mylist[6:9])  #o/p:[1, 2, 3]
#b
print(mylist[9:15]) #o/p: [9, 0, 122, 10, 2, 3]
#c
print(mylist[5:])   #o/p: [8, 1, 2, 3, 9, 0, 122, 10, 2, 3, 4, 3, 3, 2]
#d
print(mylist[12:])  #o/p:[10,2, 3, 4, 3, 3,2]
#e
print(mylist[12: :2])   #o/p: [10, 3, 3, 2]
#f
print(mylist[3:11:2])   #o/p:[6, 8, 2, 9]
#g
print(mylist[6::4])     #o/p:[1, 0, 3, 2]


##2 negative slice
print("negative slice")
#e
print(mylist[-7::2])    # o/p: [10, 3, 3, 2]
#f
print(mylist[-16:-9:2])    #o/p: [6, 8, 2, 9] 
#g
print(mylist[-13::4])       #o/p: [1, 0, 3, 2]
#h
print(mylist[-13:-7])

#  print(mylist[])