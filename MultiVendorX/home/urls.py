from django.urls import path
from .views import *

app_name = 'home'

urlpatterns = [
    path('', HomeView.as_view(), name=''),
    path('cart/', cartView.as_view(), name='cart'),
    path('store/', storeView.as_view(), name='store'),
]
