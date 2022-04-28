from cgitb import lookup
from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import generics ,authentication,permissions
from product.models import Product_comments
from product.models import Product
from product.serializers import ProductSerializer,Product_comment_serializer
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from product.permissions import  IsStaffMember




class ProductDetailView(generics.RetrieveAPIView):
    queryset=Product.objects.all();
    serializer_class = ProductSerializer;


class Product_comment_detail_view(generics.RetrieveAPIView):
    queryset=Product_comments.objects.all();
    serializer_class=Product_comment_serializer;


class ProductListCreateApiView(generics.ListCreateAPIView):
    queryset=Product.objects.all(); 
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=ProductSerializer;
  
class ProductListApiView(generics.ListAPIView):
    queryset=Product.objects.all();
    serializer_class=ProductSerializer;
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[IsStaffMember] #gives  permission to see product list if user is able to see products.


 

@api_view(["POST","GET"])
def  post_or_get(request,pk=None,*args,**kwargs): # handling post and  get_list request in single view
    if request.method=="POST":
        data={};
        serializer=ProductSerializer(data=request.data); #post
        if serializer.is_valid():
            data=serializer.data;
        return JsonResponse(data)
     
    if request.method=="GET":
        if pk is not None:
         obj=get_object_or_404(Product,pk=pk)
         data=ProductSerializer(obj,many=False).data
         return JsonResponse(data,safe=False)

        queryset=Product.objects.all();
        serializer=ProductSerializer(queryset,many=True); #list view
        return JsonResponse(serializer.data,safe=False)
        


class UpdateProductView(generics.UpdateAPIView):  #update view
       queryset=Product.objects.all();
       lookup_field='pk'
       serializer_class=ProductSerializer


class DeleteProductView(generics.DestroyAPIView):  #update view
    queryset=Product.objects.all(); 
    lookup_field='pk';
    serializer_class=ProductSerializer;


     



          



    








# Create your views here.
