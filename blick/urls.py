from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('listings/', views.listings, name='listings'),
    path('news/', views.news, name='news'),
    path('contact/', views.contact, name='contact')
]