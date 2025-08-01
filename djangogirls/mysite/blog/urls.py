from django.urls import path
from .views import *

urlpatterns = [
    path('',blog_list_view, name='list'),
    path('create-blog', blog_post_view, name='create-blog'),
    path('edit/<int:pk>/', post_edit_view, name='post_edit'),
]