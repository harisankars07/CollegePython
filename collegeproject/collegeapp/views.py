from django.shortcuts import render,redirect
from .models import Department,Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import EnquiryForm
from django.contrib import messages


def home(request):
    departments = Department.objects.all()
    return render(request, 'index.html',{'departments': departments})

def logins(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/new_page')
        else:
            pass
    return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if not all([username, password, confirm_password]):
            messages.info(request, "Please fill all required fields.")
            return render(request, 'register.html')

        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, "USERNAME TAKEN")
                return redirect('register')

        else:
            messages.info(request, "PASSWORD NOT MATCH")
            return redirect('register')
        return redirect('/logins')

    return render(request, 'register.html')

def new_page(request):

    return render(request, 'new_page.html')


def form(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            # form.save()
            return redirect('/confirm')

    else:
        form = EnquiryForm()
    return render(request, 'form.html', {'form': form})

def confirm(request):

    return render(request, 'confirm.html')

def get_courses(request):
    department_id = request.GET.get('department_id')
    courses = Course.objects.filter(department_id=department_id)
    return render(request, 'get_course.html', {'courses': courses})

