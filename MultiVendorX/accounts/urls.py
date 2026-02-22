from django.contrib import admin
from django.urls import path,include
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('signin/', signinView.as_view(), name='signin'),
    path('register/', registerView.as_view(), name='register'),
]
