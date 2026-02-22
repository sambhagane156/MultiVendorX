from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class cartView(TemplateView):
    template_name = 'cart.html'

class storeView(TemplateView):
    template_name = 'store.html'