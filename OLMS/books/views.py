from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.contrib import messages
from .models import Book, BorrowedBook
from .forms import BookForm
from django.db.models import Q



class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'
    paginate_by = 10

class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'

class BookCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('books:books.list')
    def test_func(self): 
        # How Django Handles AC Is important to me , just checking different methods
        # This method checks if the current user is a staff member.
        # If the user is a staff member, return True to allow access.
        # If the user is not a staff member, return False to deny access.
    
        return self.request.user.is_staff

class BookUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('books:books.list')

    def test_func(self):
        return self.request.user.is_staff

class BookDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Book
    template_name = 'book_confirm_delete.html'
    success_url = reverse_lazy('books:books.list')

    def test_func(self):
        return self.request.user.is_staff

def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if book.available_quantity > 0:
        BorrowedBook.objects.create(book=book, user=request.user)
        book.available_quantity -= 1
        book.save()
        messages.success(request, f'You have successfully borrowed {book.title}.')
    else:
        messages.error(request, f'Sorry, {book.title} is not available for borrowing.')
    return redirect('books:books.detail', pk=pk)

def return_book(request, pk):
    borrowed_book = get_object_or_404(BorrowedBook, pk=pk, user=request.user, status=BorrowedBook.BORROWED)
    book = borrowed_book.book
    book.available_quantity += 1
    book.save()
    borrowed_book.return_book()
    messages.success(request, f'You have successfully returned {book.title}.')
    return redirect('books:books.borrowed')



class BorrowedBooksView(LoginRequiredMixin, ListView):
    model = BorrowedBook
    template_name = 'borrowed_books.html'
    context_object_name = 'borrowed_books'
    paginate_by = 10

    def get_queryset(self):
        if self.request.user.is_staff:
            return BorrowedBook.objects.all().order_by('-borrowed_date')
        else:
            return BorrowedBook.objects.filter(user=self.request.user).order_by('-borrowed_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_admin'] = self.request.user.is_staff
        return context