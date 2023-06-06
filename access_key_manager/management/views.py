from django.shortcuts import render
from .models import Key
from django.views.generic import ListView
# Create your views here.
class ListView(ListView):
    model = Key
    template_name = 'management/key_detail.html'
    ordering = ['name']