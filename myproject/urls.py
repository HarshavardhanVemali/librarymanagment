from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('about.html/', views.about, name='about'),
    path('faculty.html', views.faculty, name='faculty'),
    path('facultypage.html', views.facultypage, name='facultypage'),
    path('contact.html', views.contact, name='contact'),
    path('attendance.html', views.attendance, name='attendance'),
    path('regulation.html', views.regulation, name='regulation'),
    path("login/",views.login_view,name="login"),
    path('regulation/<int:folder_id>/', views.subfolder, name='subfolder'),
    path('download/<str:file_path>/', views.download_file, name='download_file'),
    path('adminlogin/', views.admin_login, name='adminlogin'),
    path('adminpage/', views.admin_page, name='adminpage'),
    path('logout/', views.logout_view, name='logout'),
    path('adminregulation/',views.admin_regulation,name='adminregulation'),
    path('upload/', views.upload_image, name='upload_image'),
    path('delete_image/', views.delete_image, name='delete_image'),
    path('add_regulation/', views.add_regulation, name='add_regulation'),
    path('delete_regulation/', views.delete_regulation, name='delete_regulation'),
    path('adminregulationsubfolder/<int:folder_id>', views.admin_regulation_folder_list, name='admin_regulation_subfolder'),
    path('adminregulationsubfolder/', views.add_folder, name='add_folder'),
    path('admin_regulation_subfolder/', views.upload_file, name='upload_file'),
    path('delete_folder/', views.delete_folder, name='delete_folder'),
    path('delete_file/', views.delete_file, name='delete_file'),
    path('library',views.library,name='library'),
    path('librarylogin/', views.librarylogin, name='librarylogin'),
    path('adminlibrary/',views.admin_library,name='adminlibrary'),
    path('adminaddusers/',views.admin_addusers,name='adminaddusers'),
    path('adminissuebook/',views.adminissuebook,name='adminissuebook'),
    path('add_users/', views.add_users, name='add_users'),
    path('adminaddbooks/',views.admin_addbooks,name='admin_addbooks'),
    path('admindeletebook/<int:book_id>/', views.delete_book, name='delete_book'),
    path('issue_book/', views.issue_book, name='issue_book'),  # Add this URL
    path('check_user/', views.check_user, name='check_user'),
    path('check_book/', views.check_book, name='check_book'),   
    path('return_book/', views.return_book, name='return_book'),
    path('check_issued_books/', views.check_issued_books, name='check_issued_books'),
    path('check_issued_return_books/', views.check_issued_return_books, name='check_issued_return_books'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)