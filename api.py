# application programming interface

# import requests,json

# api='https://api.github.com/users'##correct 200 wrong 404
# getData=requests.get(api)
# print(getData)
# print(getData.content)
# print(getData.headers)


# with open('github.json',"w") as file:
#     json.dump(getData.json(),file)

import requests,json

api='https://api.github.com/users'
getData=requests.get(api)
print(getData)
print(getData.content)
print(getData.headers)

with open('github.json',"w") as file:
    json.dump(getData.json(),file)
