from django.urls import path
from . import views
urlpatterns = [
    path('blogs/', views.blog_list, name='blog_list'),
    path('posts/', views.blog, name='posts'),
    path('posts/new/',views.new_post, name='create_new_post')
]
