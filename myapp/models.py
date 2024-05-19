
from django.db import models
from django.db.models.signals import pre_delete
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.conf import settings
from django.utils import timezone


class Folder(models.Model):
    name = models.CharField(max_length=255)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='subfolders')  # Recursive relationship

    def __str__(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.name}/{self.name}"

@receiver(pre_delete, sender=Folder)
def delete_subfolders(sender, instance, **kwargs):
    subfolders = instance.subfolders.all()
    for subfolder in subfolders:
        subfolder.delete()

class File(models.Model):
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, related_name='files')

    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.file.delete(save=False)
        super().delete(*args, **kwargs)

class FailedLoginAttempts(models.Model):
    ip_address = models.CharField(max_length=45)
    timestamp = models.DateTimeField(auto_now_add=True)
    attempts = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f'{self.ip_address} - {self.timestamp} - Attempts: {self.attempts}'

class UploadedImage(models.Model):
    image = models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
class CustomUser(AbstractUser):
    department = models.CharField(max_length=100, blank=True)
    user_type = models.CharField(max_length=50, choices=[
        ('faculty', 'Faculty'),
        ('student', 'Student'),
    ], default='student')
    books_taken = models.IntegerField(default=0)
    books_in_hand = models.IntegerField(default=0)
    books_returned = models.IntegerField(default=0)
    fine = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    @property
    def total_books_taken(self):
        return self.books_taken  

    @property
    def current_books_in_hand(self):
        return self.books_in_hand  

    @property
    def total_books_returned(self):
        return self.books_returned  

    @property
    def fine_amount(self):
        return self.fine 
class Book(models.Model):
    CONDITION_CHOICES = [
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('damaged', 'Damaged'),
    ]

    book_name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    number_of_books = models.IntegerField()
    barcode = models.CharField(max_length=100)
    published_by = models.CharField(max_length=100)
    condition = models.CharField(max_length=100, choices=CONDITION_CHOICES)
    location = models.CharField(max_length=100)

    def __str__(self):
        return self.book_name
class AdminIssuesBooks(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    issued_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(blank=True, null=True)

    @property
    def barcode(self):
        return self.book.barcode

    def __str__(self):
        return f"{self.user.username} issued {self.book.book_name}"