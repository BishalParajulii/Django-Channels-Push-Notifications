from django.contrib import admin
from django.urls import path , include
from .views import notification_page_view

urlpatterns = [
    path("" , notification_page_view , name="notification_page"),
    
]
