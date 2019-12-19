from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import DetailView
from .models import Thread

# Create your views here.
class ThreadList(ListView):
    model = Thread

class ThreadDetail(DetailView):
    model = Thread