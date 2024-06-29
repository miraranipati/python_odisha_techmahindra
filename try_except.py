a=10
b=0
# print(a/b)

# try:
#     print(a/b)
# except Exception as e:
#     print("i can not divide",e)

# finally:
#     print('i am going to run 100 if try or pass')
    


try:
    print(a/b)
except Exception as e:
    print("i can not divide",e)
else:
    print("if try get passed") #if error not present
finally:
    print('i am going to run 100 if try or pass')

print("hello")        
