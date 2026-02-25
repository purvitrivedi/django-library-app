from django.shortcuts import render
from django.views.generic import ListView

from .models import Book


# Create your views here.

def home(request):
    return render(request, 'index.html')

class BookList(ListView):
    model=Book