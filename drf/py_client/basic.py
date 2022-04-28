import json
import requests
'''
endpoint="http://127.0.0.1:8000/api/products/comment/"
response=requests.post(endpoint,json={'id':1,'comment':'hi  i am the first comment'})
print(response.json());
'''

endpoint='http://127.0.0.1:8000/api/products/get_or_post/'

response = requests.post(endpoint,json={'title':'Vacum Cleaner','content':'It is a quality cleaner','price':34})

print(response.json());






