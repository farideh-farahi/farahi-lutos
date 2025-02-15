from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    return render(request, 'base/index.html')
# ویو برای لاگین
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # به صفحه خانه هدایت می‌کند
    else:
        form = AuthenticationForm()
    return render(request, 'base/login.html', {'form': form})

# ویو برای لاگ اوت
def user_logout(request):
    logout(request)
    return redirect('home')  # به صفحه خانه هدایت می‌کند

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # به طور خودکار کاربر را وارد کنید
            return redirect('home')  # به صفحه خانه هدایت کنید
    else:
        form = SignUpForm()
    return render(request, 'base/signup.html', {'form': form})