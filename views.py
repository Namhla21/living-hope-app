from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import HCTRecordForm, LSERecordForm
from .utils import export_hct_records_to_excel, export_lse_records_to_excel
def create_admin():
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin123')

def home(request):
    create_admin()
    return render(request, 'home.html')


def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def hct_page(request):
    success = False

    if request.method == 'POST':
        form = HCTRecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.counselor = request.user
            record.save()
            export_hct_records_to_excel()
            form = HCTRecordForm()
            success = True
    else:
        form = HCTRecordForm()

    return render(request, 'hct.html', {'form': form, 'success': success})


@login_required
def lse_page(request):
    success = False

    if request.method == 'POST':
        form = LSERecordForm(request.POST)
        if form.is_valid():
            record = form.save(commit=False)
            record.counselor = request.user
            record.save()
            export_lse_records_to_excel()
            form = LSERecordForm()
            success = True
    else:
        form = LSERecordForm()

    return render(request, 'lse.html', {'form': form, 'success': success})