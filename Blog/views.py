
from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogForm

def new_post(request):  
    if request.method == "POST":  
        form = BlogForm(request.POST)  # فرم را با اطلاعات POST بارگذاری کنید  
        if form.is_valid():  
            form.save()  # ذخیره پست جدید  
            return redirect('home_page')  # کاربر را به صفحه خانه هدایت می‌کنیم  
    else:  
        form = BlogForm()  # برای یک درخواست GET فرم جدید ایجاد کنید  

    return render(request, 'Blog/create_new_post.html', {'form': form})  # فرم را به الگو ارسال کنید

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'Blog/blog_list.html', {'blog': blogs})

def blog(request):
    return render(request, 'Blog/post.html')





