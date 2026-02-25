from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView

from .models import Book


# Create your views here.

def home(request):
    return render(request, 'index.html')

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

class BookCreate(CreateView):
    model = Book
    fields = '__all__'