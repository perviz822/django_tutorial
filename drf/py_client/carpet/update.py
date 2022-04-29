
import requests;
endpoint='http://127.0.0.1:8000/api/products/post/carpet/1/'
response=requests.post(endpoint,json={'name':'Israeli Carpet','year':1976})
print(response.json());