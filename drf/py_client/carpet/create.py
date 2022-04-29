from rest_framework import request
import requests;
endpoint='http://127.0.0.1:8000/api/products/post/carpet/'
response=requests.post(endpoint,json={'name':'Iranian Carpet','year':1992,'information':'It is the oldest carpet of Iran'})
print(response.json());