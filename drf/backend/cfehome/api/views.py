from django.http import JsonResponse
from django.shortcuts import render
import json
from product.serializers import Product_comment_serializer
from product.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response;
from rest_framework.decorators import api_view
from product.serializers import ProductSerializer

@api_view(["POST"]) # giving permissons to requests
def api_home(request,*args,**kwargs):
    instance=Product.objects.all().order_by("?").first();
    serializer = ProductSerializer(data=request.data);
    if serializer.is_valid():
        print('serializer  is valid')
    else:
        print('serializer is not valid')    
   
       # data=model_to_dict(model_instance,fields=['title','content','price'])
    return JsonResponse(serializer.data);



@api_view(["POST","GET"])
def comments(request):
    data={};
    serializer=Product_comment_serializer(data=request.data);
    if serializer.is_valid():
     return JsonResponse(serializer.data);      
    else:
        print('serializeris not valid')
        return JsonResponse(data); 


   
   






# Create your views here.
