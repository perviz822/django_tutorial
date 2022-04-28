import json
import requests
'''
endpoint="http://127.0.0.1:8000/api/products/comment/"
response=requests.post(endpoint,json={'id':1,'comment':'hi  i am the first comment'})
print(response.json());
'''

endpoint='http://127.0.0.1:8000/api/products/2/'

response = requests.get(endpoint)

print(response.json());






