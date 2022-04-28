import json
import requests
'''
endpoint="http://127.0.0.1:8000/api/products/comment/"
response=requests.post(endpoint,json={'id':1,'comment':'hi  i am the first comment'})
print(response.json());
'''

endpoint='http://127.0.0.1:8000/api/products/2/update/'

data={
    'title':'Brand new product',
    'price':37,
    'content':'IT IS THE UPDATED CONTENT'
}

response = requests.put(endpoint,json=data)

print(response.json());