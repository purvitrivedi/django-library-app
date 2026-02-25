from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Publisher
from .forms import BookForm


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

class BookUpdate(UpdateView):
    model = Book
    fields = '__all__'

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class PublisherList(ListView):
    model = Publisher

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        books_without_publisher = Book.objects.filter(publisher__isnull=True)
        context["book_form"] = BookForm
        context["books_without_publisher"] = books_without_publisher
        return context
    
def add_book_to_publisher(request, pk):
    form = BookForm(request.POST)
    if form.is_valid():
        new_book = form.save(commit=False)
        new_book.publisher_id = pk
        new_book.save()
    return redirect('publisher-detail', pk=pk)

def associate_book(request, publisher_id, book_id):
    book = Book.objects.get(id=book_id)
    book.publisher_id = publisher_id
    book.save()

    return redirect('publisher-detail', pk=publisher_id)
