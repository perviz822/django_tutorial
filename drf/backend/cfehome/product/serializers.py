from pickle import TRUE
from product.models import Product_comments
from product.models import Product
from rest_framework import serializers;

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
    id=serializers.Serializer
    class Meta():
        model=Product_comments
        fields=['id','comment']  

      

