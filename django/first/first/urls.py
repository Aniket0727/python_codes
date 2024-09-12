"""
URL configuration for first project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from first import views
from django.conf import settings
from django.conf.urls.static import static

# from .views import delete_product
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),
    path('login', views.login,name='login'),
    path('home', views.home,name='home'),
    path('about', views.about,name='about'),
    path('contactus', views.contactus,name='contactus'),
    path('addproduct', views.addproduct,name='addproduct'),
    path('profile',views.profile,name='profile'),
    path('viewproduct',views.viewproduct,name='viewproduct'),
    path('logout',views.logout,name='logout'),
    path('rp_products',views.rp_products,name='rp_products'),
    path('product_detail/<int:pk>/', views.product_detail, name='product_detail'),

    path('pclick',views.pclick,name='pclick'),
    path('delete_product', views.delete_product, name='delete_product'),
    path('otp', views.otp, name='otp'),
    
]
    


if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
    
    # urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT2)
