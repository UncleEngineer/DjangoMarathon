# เลขาของห้อง myapp

from django.urls import path
from .views import Homepage, About, Services, Products, Contact

urlpatterns = [
    path('', Homepage, name='home'), # localhost:8000 / www.loong.com
    path('about', About, name='about'),
    path('services', Services, name='services'),
    path('products', Products, name='products'),
    path('contact', Contact, name='contact'),
]