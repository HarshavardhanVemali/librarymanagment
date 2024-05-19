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