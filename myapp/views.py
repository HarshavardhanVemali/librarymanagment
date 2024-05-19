# views.py
from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse
from .models import Folder
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import FailedLoginAttempts,UploadedImage
from datetime import timedelta
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.utils import timezone
import pytz
from .forms import ImageUploadForm,FolderForm,FileUploadForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Folder,File
from django.contrib.auth import logout
from django.contrib import messages
import requests
from bs4 import BeautifulSoup
import json
from .models import CustomUser
from .forms import BookForm
from .models import Book
from django.urls import reverse
from .models import Book
from django.views.decorators.csrf import csrf_exempt
from .models import  Book
from django.contrib.auth.models import User
from .models import AdminIssuesBooks, Book
from .forms import IssueBookForm, ReturnBookForm
from django.views.decorators.csrf import csrf_exempt
from .models import AdminIssuesBooks, Book
from django.contrib.auth.hashers import check_password


MAX_FAILED_ATTEMPTS = 3 

def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')

def faculty(request):
    return render(request, 'faculty.html')

def facultypage(request):
    return render(request, 'facultypage.html')

def contact(request):
    return render(request, 'contact.html')

def regulation(request):
    folders = Folder.objects.all()
    return render(request, 'regulation.html', {'folders': folders})
def attendance(request):
    return render(request,'attendance.html')
@login_required(login_url="/adminlogin")
def admin_regulation(request):
    parent_folders = Folder.objects.filter(parent=None)
    return render(request, 'admin_regulation.html', {'parent_folders': parent_folders})
@login_required(login_url="/adminlogin")
def admin_regulation_folder_list(request, folder_id=None):
    folder = get_object_or_404(Folder, id=folder_id)

    # Recursively get all subfolders, including child subfolders
    all_subfolders = [folder]
    def get_descendants(folder):
        subfolders = folder.subfolders.all()
        all_subfolders.extend(subfolders)
    get_descendants(folder)
    return render(request, 'admin_regulation_subfolder.html', {'folder': folder, 'subfolders': all_subfolders})
@login_required(login_url="/adminlogin/")
def add_folder(request):
    if request.method == 'POST':
        form = FolderForm(request.POST)
        if form.is_valid():
            folder = form.save(commit=False)
            folder.parent_id = request.POST.get('parent', None)  # Accessing the parent folder ID
            folder.save()
            messages.success(request, 'Folder added successfully.')  # Add success message
            return redirect('admin_regulation_subfolder', folder_id=folder.parent_id)
    else:
        form = FolderForm()
    return render(request, 'admin_regulation_subfolder.html', {'form': form})
@login_required(login_url="/adminlogin/")
def upload_file(request):
    if request.method == 'POST':
        current_folder_id = request.POST.get('current_folder')
        current_folder = Folder.objects.get(id=current_folder_id)
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file_instance = form.save(commit=False)
            file_instance.folder = current_folder
            file_instance.save()
            return JsonResponse({'success': True, 'message': 'File added successfully'})
        else:
            return JsonResponse({'success': False, 'message': 'Form validation failed'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
@login_required(login_url="/adminlogin/")
def delete_folder(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            folder_id = data.get('folder_id')
            folder = Folder.objects.get(id=folder_id)
            folder.delete()
            return JsonResponse({'success': True, 'message': 'Folder deleted successfully'})
        except Folder.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'Folder does not exist'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
@login_required(login_url="/adminlogin/")
@csrf_exempt  # Temporarily disable CSRF protection for debugging (not recommended for production)
def delete_file(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            file_id = data.get('file_id')
            file = File.objects.get(id=file_id)
            file.delete()
            return JsonResponse({'success': True, 'message': 'File deleted successfully'})
        except File.DoesNotExist:
            return JsonResponse({'success': False, 'message': 'File does not exist'})
        except Exception as e:
            return JsonResponse({'success': False, 'message': str(e)})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})
@login_required(login_url="/adminlogin/")
def success(request):
    return render(request, 'admin_regulation_subfolder.html')
def download_file(request, file_path):
    with open(file_path, 'rb') as f:
        response = HttpResponse(f.read())
        content_type = "application/octet-stream"
        response['Content-Type'] = content_type
        return response

def subfolder(request, folder_id):
    folder = get_object_or_404(Folder, id=folder_id)
    all_subfolders = [folder]
    def get_descendants(folder):
        subfolders = folder.subfolders.all()
        all_subfolders.extend(subfolders)
    get_descendants(folder)
    return render(request, 'subfolder.html', {'folder': folder, 'subfolders': all_subfolders})
BLOCKED_IPS = {}
BLOCKED_IPS_PERMANENT={}
def admin_login(request):
    if request.method == 'POST':
        ip_address = request.META.get('REMOTE_ADDR')
        if is_ip_blocked(ip_address):
            block_expiry = BLOCKED_IPS[ip_address]
            asia_kolkata_timezone = pytz.timezone('Asia/Kolkata')
            block_expiry_ist = block_expiry.astimezone(asia_kolkata_timezone)
            time = block_expiry_ist.strftime('%H:%M:%S')
            return render(request, 'admin_login.html', {'blocked': True, 'error_message': f'Your IP address is blocked until {time} IST'})
        
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            if user.is_superuser or (user.is_staff and not user.is_active):
                FailedLoginAttempts.objects.filter(ip_address=ip_address).delete()
                login(request, user)
                return redirect('adminpage')
            else:
                return render(request, 'admin_login.html', {'error_message': 'You do not have permission to access the admin page.'})
        else:
            failed_attempt, created = FailedLoginAttempts.objects.get_or_create(ip_address=ip_address)
            if not created:
                failed_attempt.attempts += 1
                failed_attempt.save()
                if failed_attempt.attempts >= MAX_FAILED_ATTEMPTS:
                    block_expiry_time = timezone.now() + timedelta(minutes=30)
                    block_expiry_time_ist = block_expiry_time.astimezone(pytz.timezone('Asia/Kolkata')) 
                    time_string_ist = block_expiry_time_ist.strftime('%H:%M:%S')
                    BLOCKED_IPS[ip_address] = block_expiry_time
                    BLOCKED_IPS_PERMANENT[ip_address] = timezone.now().astimezone(pytz.timezone('Asia/Kolkata'))
                    return render(request, 'admin_login.html', {'blocked': True, 'error_message': f'Your IP address is blocked until {time_string_ist} IST'})
            return render(request, 'admin_login.html', {'error_message': 'Invalid username or password'})
    else:
        return render(request, 'admin_login.html')
def is_ip_blocked(ip_address):
    if ip_address in BLOCKED_IPS:
        if timezone.now().astimezone(pytz.timezone('Asia/Kolkata')) >= BLOCKED_IPS[ip_address]:
            del BLOCKED_IPS[ip_address]
            return False
        else:
            return True
    return False

@login_required(login_url="/adminlogin/")
def admin_page(request):
    old_images = UploadedImage.objects.all()
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            
            if not UploadedImage.objects.filter(image=new_image.image).exists():
                new_image.save()
            old_images = UploadedImage.objects.all()
    else:
        form = ImageUploadForm()
    return render(request, 'admin_page.html', {'images': old_images, 'form': form})
@login_required(login_url="/adminlogin")
def logout_view(request):
    logout(request)
    return redirect('adminlogin')
@login_required(login_url="/adminlogin")
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save()
            return JsonResponse({'image_url': instance.image.url})
    else:
        form = ImageUploadForm()
    return render(request, 'admin_page.html', {'form': form})
@login_required(login_url="/adminlogin")
def delete_image(request):
    if request.method == 'POST':
        image_id = request.POST.get('image_id')
        image = get_object_or_404(UploadedImage, id=image_id)
        image.delete()
        return JsonResponse({'message': 'Image deleted successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'})
@login_required(login_url="/adminlogin")
@csrf_exempt
def add_regulation(request):
    if request.method == 'POST':
        folder_name = request.POST.get('folder_name')
        regulation_folder = Folder.objects.create(name=folder_name)
        for i in range(1, 9):
            subfolder_name = f'SEM-{i}'
            Folder.objects.create(name=subfolder_name, parent=regulation_folder)
        return JsonResponse({'success': True})
    else:
        return render(request, 'admin_regulation.html')
@login_required(login_url="/adminlogin")
def delete_regulation(request):
    if request.method == 'POST':
        folder_id = request.POST.get('folder_id')
        try:
            folder = Folder.objects.get(id=folder_id)
            folder.delete()
            return JsonResponse({'success': True})
        except Folder.DoesNotExist:
            return JsonResponse({'error': 'Folder not found'}, status=404)
        except Exception as e:
            print(f"Error deleting folder: {e}")
            return JsonResponse({'error': 'An error occurred during deletion'}, status=500)
    else:
        return JsonResponse({'success': False})
@login_required(login_url="/adminlogin")
def delete_file(request, file_id):
    file_instance = File.objects.get(pk=file_id)
    file_instance.delete_file()
    return redirect('adminpage')
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            # Define the external login URL
            external_login_url = 'https://pay.mvgrce.edu.in/ecap/Default.aspx?ReturnUrl=%2fecap%2fStudentMaster.aspx'

            # Start a session to handle cookies and other session data
            session = requests.Session()

            # Fetch the login page to get any necessary cookies or hidden fields
            response = session.get(external_login_url)
            if response.status_code != 200:
                return JsonResponse({'status': 'failure', 'message': 'Unable to access external login page'}, status=500)

            # Parse the login page to get any necessary hidden fields
            soup = BeautifulSoup(response.content, 'html.parser')
            viewstate = soup.find('input', {'name': '__VIEWSTATE'})['value']
            eventvalidation = soup.find('input', {'name': '__EVENTVALIDATION'})['value']

            # Prepare login data for the external site
            login_data = {
                'txtId2': username,  # Ensure this is the correct username field
                'txtPwd2': password,  # Ensure this is the correct password field
                '__VIEWSTATE': viewstate,
                '__EVENTVALIDATION': eventvalidation,
            }

            # Post login data to the external site
            response = session.post(external_login_url, data=login_data)

            # Check if login was successful
            if 'StudentMaster.aspx' in response.url:
                # If successful, redirect to the external dashboard with session cookies
                return JsonResponse({'status': 'success', 'redirect_url': 'https://pay.mvgrce.edu.in/ecap/StudentMaster.aspx'})
            else:
                error_message = 'Invalid credentials or other login failure on external site.'
                return JsonResponse({'status': 'failure', 'message': error_message}, status=401)
        else:
            error_message = 'Invalid username or password.'
            return render(request, 'attendance.html', {'error_message': error_message})
    return render(request, 'attendance.html')
def verify_credentials(username, password):
    # Check if the provided username and password are valid
    user = authenticate(username=username, password=password)
    return user
def library(request,user):
    user = user
    user_data = {
        'username': user.username,
        'email':user.email,
        'first_name':user.first_name,
        'last_name':user.last_name,
        'user_type': user.user_type,
        'total_books_taken': user.total_books_taken,
        'current_books_in_hand': user.current_books_in_hand,
        'total_books_returned': user.total_books_returned,
        'department': user.department,
        'fine_amount': user.fine_amount,
    }
    issued_books = AdminIssuesBooks.objects.filter(user=user)
    issued_books_data = [
        {
            'book_name': book.book.book_name,
            'barcode': book.book.barcode,
            'issued_date': book.issued_date.strftime('%Y-%m-%d'),
            'return_date': book.return_date.strftime('%Y-%m-%d') if book.return_date else '-'
        } for book in issued_books
    ]
    books = Book.objects.all()
    return render(request, 'library.html', {'user': user_data, 'issued_books': issued_books_data,'books':books})
def librarylogin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            return render(request, 'librarylogin.html', {'error_message': 'Invalid username'})
        user = verify_credentials(username, password)
        if check_password(password, user.password):
            return library(request, user)
        else:
            return render(request, 'librarylogin.html', {'error_message': 'Invalid password'})
    else:
        return render(request, 'librarylogin.html')

def admin_library(request):
    return render(request,'adminlibrary.html')
def add_users(request):
    if request.method == 'POST':
        print("POST request received in add_users view.")
        sequencenumber = request.POST.get('sequencenumber')
        min_value = int(request.POST.get('min'))
        max_value = int(request.POST.get('max'))
        department = request.POST.get('department')
        user_type = request.POST.get('usertype')  # Get user_type from the form

        print(f"Form Data: user_type={user_type}, sequencenumber={sequencenumber}, min={min_value}, max={max_value}, department={department}")

        # Loop to create users based on the range
        for i in range(min_value, max_value + 1):
            username = f"{sequencenumber}{i:02}"
            try:
                user = CustomUser.objects.create_user(
                    username=username,
                    password='password123',  # Set a default password
                    department=department,
                    user_type=user_type
                )
                # Save the user in the database
                user.save()
                messages.success(request, f"User {username} created successfully!")
            except Exception as e:
                # Handle potential errors during user creation (e.g., username already exists)
                messages.error(request, f"Error creating user {username}: {e}")

        return redirect('add_users')  # Redirect to the same view to refresh the page
    users = CustomUser.objects.all()
    return render(request, 'adminaddusers.html', {'users': users})
def adminissuebook(request):
    return render(request,'adminissuebook.html')
def admin_addusers(request):
    return render(request,'adminaddusers.html')
def admin_addbooks(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            barcode = form.cleaned_data.get('barcode')
            # Check for existing book with the same barcode
            if Book.objects.filter(barcode=barcode).exists():
                messages.error(request, f"Book with barcode '{barcode}' already exists.")
            else:
                form.save()
                book_name = form.cleaned_data.get('book_name')
                messages.success(request, f"Book '{book_name}' added successfully!")
            return redirect('admin_addbooks')
        else:
            messages.error(request, "Error adding book. Please check the form for errors.")
    else:
        form = BookForm()

    books = Book.objects.all()
    return render(request, 'adminaddbooks.html', {'form': form, 'books': books})
def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect(reverse('admin_addbooks'))
def adminissuebook(request):
    return render(request,'adminissuebook.html')

@login_required
def check_user(request):
    username = request.GET.get('username')

    if username:
        try:
            user = CustomUser.objects.get(username=username)
            user_data = {
                'username': user.username,
                'user_type': user.user_type,
                'total_books_taken': user.total_books_taken,
                'current_books_in_hand': user.current_books_in_hand,
                'total_books_returned': user.total_books_returned,
                'department': user.department,
                'fine_amount': user.fine_amount,
            }
            return JsonResponse(user_data)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Username is required'}, status=400)

@login_required
def check_book(request):
    barcode = request.GET.get('barcode')

    if barcode:
        try:
            book = Book.objects.get(barcode=barcode)
            book_data = {
                'book_name': book.book_name,
                'author': book.author,
                'category': book.category,
                'number_of_books': book.number_of_books,
                'barcode': book.barcode,
                'published_by': book.published_by,
                'condition': book.condition,
                'location': book.location,
            }
            return JsonResponse(book_data)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
    else:
        return JsonResponse({'error': 'Barcode is required'}, status=400)
def issue_book(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        username = request.POST.get('username')

        try:
            user = CustomUser.objects.get(username=username)
            book = Book.objects.get(barcode=barcode)
            
            # Check if the book has already been issued to the user and not yet returned
            existing_issue = AdminIssuesBooks.objects.filter(user=user, book=book, return_date__isnull=True).first()
            if existing_issue:
                return JsonResponse({'error': 'Book has already been issued to this user and not yet returned.'}, status=400)

            if book.number_of_books > 0:
                book.number_of_books -= 1
                book.save()

                user.books_in_hand += 1
                user.books_taken += 1
                user.save()

                issued_book = AdminIssuesBooks.objects.create(
                    user=user,
                    book=book,
                    issued_date=timezone.now()
                )
                issued_book.save()

                return JsonResponse({'success': True, 'message': 'Book issued successfully'})
            else:
                return JsonResponse({'error': 'Book is not available.'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found.'}, status=404)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found.'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Error issuing book: {e}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
@login_required
def check_issued_books(request):
    username = request.GET.get('username')
    if username:
        try:
            user = CustomUser.objects.get(username=username)
            issued_books = AdminIssuesBooks.objects.filter(user=user, return_date__isnull=True)
            issued_books_data = [{
                'book_name': issued_book.book.book_name,
                'barcode': issued_book.book.barcode,
                'issued_date': issued_book.issued_date.strftime('%Y-%m-%d %H:%M:%S'),
                'return_date': issued_book.return_date.strftime('%Y-%m-%d %H:%M:%S') if issued_book.return_date else '-'
            } for issued_book in issued_books]
            return JsonResponse({'issued_books': issued_books_data})
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
    else:
        return JsonResponse({'error': 'Username is required'}, status=400)
def return_book(request):
    if request.method == 'POST':
        barcode = request.POST.get('barcode')
        username = request.POST.get('username')
        if not barcode or not username:
            return JsonResponse({'error': 'Barcode and username are required'}, status=400)

        try:
            user = CustomUser.objects.get(username=username)
            book = Book.objects.get(barcode=barcode)

            issued_book = AdminIssuesBooks.objects.get(user=user, book=book, return_date__isnull=True)

            issued_book.return_date = timezone.now()
            issued_book.save()

            user.books_in_hand -= 1
            user.books_returned += 1
            book.number_of_books += 1
            user.save()
            book.save()

            return JsonResponse({'success': True, 'message': 'Book returned successfully'})
        except AdminIssuesBooks.DoesNotExist:
            return JsonResponse({'error': 'Book is not currently issued to this user.'}, status=400)
        except CustomUser.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except Book.DoesNotExist:
            return JsonResponse({'error': 'Book not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': f'Error returning book: {e}'}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
def check_issued_return_books(request):
    barcode = request.GET.get('barcode')
    username = request.GET.get('username')
    if barcode and username:
        try:
            user = CustomUser.objects.get(username=username)
            book = Book.objects.get(barcode=barcode)

            # Check if the book is issued to this user and hasn't been returned
            issued_book = AdminIssuesBooks.objects.get(user=user, book=book, return_date__isnull=True)
            return JsonResponse({'issued': True})  # Book is issued to the user
        except (CustomUser.DoesNotExist, Book.DoesNotExist, AdminIssuesBooks.DoesNotExist):
            return JsonResponse({'issued': False})  # Book is not issued to the user
    else:
        return JsonResponse({'error': 'Barcode and username are required'}, status=400)