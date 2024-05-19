from django import forms
from .models import UploadedImage
from .models import Folder,File,Book
from .models import CustomUser
from .models import AdminIssuesBooks, Book

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
class UploadImageForm(forms.ModelForm):
    class Meta:
        model = UploadedImage
        fields = ['image']
class FolderForm(forms.ModelForm):
    class Meta:
        model = Folder
        fields = ['name', 'parent']

class FileUploadForm(forms.ModelForm):
    class Meta:
        model = File
        fields = ['name', 'file'] 

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password', 'user_type', 'department']
        widgets = {
            'password': forms.PasswordInput(),
        }
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['book_name', 'author', 'category', 'number_of_books', 'barcode', 'published_by', 'condition', 'location']

class IssueBookForm(forms.ModelForm):
    username = forms.CharField(max_length=150, required=True)
    barcode = forms.CharField(max_length=255, required=True)

    class Meta:
        model = AdminIssuesBooks
        fields = ['username', 'barcode']

class ReturnBookForm(forms.ModelForm):
    barcode = forms.CharField(max_length=255, required=True)

    class Meta:
        model = AdminIssuesBooks
        fields = ['barcode']