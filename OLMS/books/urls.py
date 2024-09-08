from django.urls import path
from . import views

app_name = 'books'


urlpatterns = [
    path('', views.BookListView.as_view(), name='books.list'),
    path('<int:pk>/', views.BookDetailView.as_view(), name='books.detail'),
    path('create/', views.BookCreateView.as_view(), name='books.create'),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name='books.update'),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name='books.delete'),
    path('<int:pk>/borrow/', views.borrow_book, name='books.borrow'),
    path('<int:pk>/return/', views.return_book, name='books.return'),
    path('borrowed/', views.BorrowedBooksView.as_view(), name='books.borrowed'),

]