import json
import requests
from getpass import getpass;
password=getpass()
auth_endpoint='http://127.0.0.1:8000/api/auth/'
endpoint='http://127.0.0.1:8000/api/products/'

auth_response = requests.post(auth_endpoint,json={'username':'ledzeppelin','password':password}) # custom login

token=auth_response.json()['token']; #gets the  right token if the user exist
headers={
    "Authorization":f"Token {token}"  #then using this token to reach the protected   views
}

response=requests.get(endpoint,headers=headers)



print(auth_response.json());
print(response.json())