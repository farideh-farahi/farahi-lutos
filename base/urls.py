from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from .views import register
urlpatterns = [
    path('',views.index,name='home_page'),
    path('signup/', register, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='base/login.html'), name='login'),
]

