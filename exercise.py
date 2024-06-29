''' Do Type Conversion for   a) int to string 
                             b) string to int 
                             c) bool to string 
                             d) string to bool   '''
#a
number=3478 
number=str(number)
print(number,type(number  ))
#b
variable="1254"
variable=int(variable)
print(variable,type(variable))
#c
var1=True
var1=str(var1)
print(var1,type(var1))
#d
var2="true"
var2=bool(var2)
print(var2,type(var2))

##2


skills = list(input("Enter skills separated by comma and space: ").split(", "))

# Print the list of skills
print("Skills:", skills)

print(type(skills))