from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('books/', views.BookList.as_view(), name="book-list"),
    path('books/<int:pk>/', views.BookDetail.as_view(), name="book-detail"),
    path('books/create/', views.BookCreate.as_view(), name="book-create"),
    path('books/<int:pk>/update/', views.BookUpdate.as_view(), name="book-update"),
    path('books/<int:pk>/delete/', views.BookDelete.as_view(), name="book-delete"),
    path('books/<int:pk>/associate-genre/', views.associate_genre, name="associate-genre"),
    path('books/<int:pk>/add-and-associate-genre/', views.add_and_associate_genre, name="add-and-associate-genre"),
    path('publishers/', views.PublisherList.as_view(), name="publisher-list"),
    path('publishers/<int:pk>/', views.PublisherDetail.as_view(), name="publisher-detail"),
    path('publishers/<int:pk>/add-book-to-publisher/', views.add_book_to_publisher, name="add-book-to-publisher"),
    path('publishers/<int:publisher_id>/associate-book/<int:book_id>', views.associate_book, name="associate-book")

]