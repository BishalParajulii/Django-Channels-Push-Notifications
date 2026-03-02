from django.contrib import admin
from django import forms
from .models import Notification


# Register your models here.

class SendNotification(forms.Form):
    message = forms.CharField(label="Notification Message" , max_length=200)
    
    
@admin.register(Notification)

class NotificationAdmin(admin.ModelAdmin):
    add_form_template = "admin/custom_add_form.html"
    
