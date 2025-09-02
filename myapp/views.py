from django.shortcuts import render
from .models import *

# Create your views here.

def Homepage(request):
    return render(request, 'index.html')