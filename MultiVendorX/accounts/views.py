from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class signinView(TemplateView):
    template_name = 'signin.html'

class registerView(TemplateView):
    template_name = 'register.html'