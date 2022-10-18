from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_index),
    path('<int:post_id>', views.blog_detail, name='blog-detail')
]