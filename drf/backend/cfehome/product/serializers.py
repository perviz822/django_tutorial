from pickle import TRUE
from product.models import Product_comments, Product

from rest_framework import serializers;
from product.models import Carpets

class ProductSerializer(serializers.ModelSerializer):  # changing the representation of data
    discount=serializers.SerializerMethodField(read_only=True);  # configuring fields
    double_price=serializers.SerializerMethodField(read_only=True)
    class Meta:
        model=Product;
        fields=['title',
                'price',
                'content',
                'double_price',
                'discount',
                ]

    def get_discount(self,obj):
        try:
         return obj.get_discount();     
        except:
         return None;  

    def get_double_price(self,obj):
          try:
             return obj.double_price();     
          except:
             return None;

class Product_comment_serializer(serializers.ModelSerializer) :
    class Meta():
        model=Product_comments
        fields=['id','comment',]  

class CarpetSerializer(serializers.ModelSerializer):
    information=serializers.SerializerMethodField()
    class Meta():
        model=Carpets;
        fields=['name','year','information'];

    def get_information(self,obj) :
       try:
           return obj.get_information()
       except: 
          return self.context['request'].data['information']

    

      

