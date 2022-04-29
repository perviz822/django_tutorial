from turtle import pos
from product.views import ProductDetailView;
from product.views import Product_comment_detail_view , update_carpet, ProductListCreateApiView, ProductListApiView ,UpdateProductView , post_or_get,DeleteProductView,post_carpet
from django.urls import path;
from api.views import comments

urlpatterns=[
    path('<int:pk>/',post_or_get),
    path('comments/<int:pk>/',Product_comment_detail_view().as_view()),
    path('comment/',comments),
    path('create/',ProductListCreateApiView.as_view()),
    path('',ProductListApiView.as_view()),
    path('get_or_post/',post_or_get),
    path('<int:pk>/update/',UpdateProductView.as_view()),
    path('<int:pk>/delete/',DeleteProductView.as_view()),
    path('post/carpet/',post_carpet),
    path('post/carpet/<int:pk>/',update_carpet)
    
]