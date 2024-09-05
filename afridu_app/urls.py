from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header ="Login to AFRIDU Registration Portal"
admin.site.site_title ="Welcome to AFRIDU REGISTRATION dashboard"
admin.site.index_title ="Welcome to AFRIDU's Dashboard"

urlpatterns = [
    path('', views.register, name="register"),
    path('thanks', views.thanks, name="thanks"),
]
