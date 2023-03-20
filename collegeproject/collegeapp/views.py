from django.shortcuts import render,redirect,get_object_or_404
from .models import Department,Course
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .forms import EnquiryForm


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

# def __init__(self, *args, **kwargs):
#     instance = kwargs.get('instance')
#     initial = kwargs.get('initial')
#     if instance:
#         department_id = instance.department_id
#         initial['Course'] = instance.course
#     elif 'department' in initial:
#         try:
#             department_id = int(initial.get('department'))
#         except (ValueError, TypeError):
#             department_id = None
#     else:
#         department_id = None
#     if department_id:
#         courses = Course.objects.filter(department_id=department_id)
#         self.fields['course'].queryset = courses
#     super().__init__(*args, **kwargs)
