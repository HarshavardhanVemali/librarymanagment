from django.contrib import admin
from .models import Folder,File,Book
from .models import UploadedImage,CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import AdminIssuesBooks

class SubFolderInline(admin.TabularInline):
    model = Folder
    extra = 1
class FileInline(admin.TabularInline):
    model = File
    extra = 1
class FolderAdmin(admin.ModelAdmin):
    inlines = [SubFolderInline, FileInline]

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        if not change:
            for i in range(1, 9):
                subfolder_name = f'SEM-{i}'
                subfolder = Folder.objects.create(name=subfolder_name, parent=obj)

if not admin.site.is_registered(Folder):
    admin.site.register(Folder, FolderAdmin)
admin.site.register(UploadedImage)
class CustomUserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('department', 'user_type', 'books_taken', 'books_in_hand', 'books_returned', 'fine')}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'user_type', 'department', 'books_taken', 'books_in_hand', 'books_returned', 'fine')
    search_fields = ('username', 'email', 'first_name', 'last_name', 'department')
    ordering = ('username',)

admin.site.register(CustomUser, CustomUserAdmin)
class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'category', 'number_of_books', 'barcode', 'published_by', 'condition', 'location')
    search_fields = ('book_name', 'author', 'category', 'barcode')

admin.site.register(Book, BookAdmin)
class AdminIssuesBooksAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'issued_date', 'return_date')
    search_fields = ('user__username', 'book__book_name', 'book__barcode')
    list_filter = ('issued_date', 'return_date')

admin.site.register(AdminIssuesBooks, AdminIssuesBooksAdmin)