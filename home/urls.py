from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('',views.index, name= 'home'),
    path("about/", views.about, name= 'about'),
    path("gadgets/", views.gadgets, name= 'gadgets'),
    path("contact/", views.contact, name= 'contact'),
]