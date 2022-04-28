
from django.contrib import admin
from django.urls import path, include
from api import views
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',views.api_home),
    path('api/products/', include('product.urls')),
    path('api/auth/',obtain_auth_token)
   

  
]
