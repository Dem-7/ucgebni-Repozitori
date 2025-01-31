import pprint

import  requests
response = requests.get("https://api.github.com")
# s = response.status_code
# print(s)
# print(response.status_code)
# print(response.ok)
# if response.ok:
#     print("Всё успешно")
# else:
#     print("Хреново")
print(response.text)
print(response.content)
aa = response.json()
pprint.pprint(aa)


import requests
import pprint

dd = {"q" :"c++"}
response = requests.get('https://api.github.com/search/repositories', params = dd)
ll= response.json()
#pprint.pprint(ll)
print(f"колличество репозиториев : {ll['total_count']}")
