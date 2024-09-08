from django.db import models
from django.conf import settings
from django.utils import timezone

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13, unique=True)
    publication_date = models.DateField()
    quantity = models.PositiveIntegerField(default=1)
    available_quantity = models.PositiveIntegerField(blank=True, null=True)
    image = models.ImageField(upload_to='books/covers', null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if self.available_quantity is None:
            self.available_quantity = self.quantity
        super(Book, self).save(*args, **kwargs)

class BorrowedBook(models.Model):
    BORROWED = 'borrowed'
    RETURNED = 'returned'
    STATUS_CHOICES = [
        (BORROWED, 'Borrowed'),
        (RETURNED, 'Returned'),
    ]

    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    borrowed_date = models.DateField(auto_now_add=True)
    return_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=BORROWED)

    def __str__(self):
        return f"{self.book.title} - {self.user.username} ({self.status})"

    def return_book(self):
        self.status = self.RETURNED
        self.return_date = timezone.now().date()
        self.save()