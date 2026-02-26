from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Book, Publisher, Genre
from .forms import BookForm, GenreForm


# Create your views here.

def home(request):
    return render(request, 'index.html')

class BookList(ListView):
    model = Book

class BookDetail(DetailView):
    model = Book

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        all_genre = Genre.objects.all()
        genre_form = GenreForm()
        context['all_genre'] = all_genre
        context['genre_form'] = genre_form
        return context

class BookCreate(CreateView):
    model = Book
    fields = '__all__'

class BookUpdate(UpdateView):
    model = Book
    fields = ['name', 'author', 'publisher']

class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('book-list')


class PublisherList(ListView):
    model = Publisher

class PublisherDetail(DetailView):
    model = Publisher

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books_without_publisher = Book.objects.filter(publisher__isnull=True)
        context["book_form"] = BookForm()
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

def associate_genre(request, pk):
    book = Book.objects.get(id=pk)
    selected_genre_ids = request.POST.getlist('genre')

    if selected_genre_ids:
        selected_genre_ids = [int(genre_id) for genre_id in selected_genre_ids]
        book.genre.set(selected_genre_ids)
    else:
        book.genre.clear()

    return redirect('book-detail', pk=pk)


def add_and_associate_genre(request, pk):
    book = Book.objects.get(id=pk)
    form = GenreForm(request.POST)

    if form.is_valid():
        new_genre = form.save()
        book.genre.add(new_genre.id)
        return redirect('book-detail', pk=pk)
    



