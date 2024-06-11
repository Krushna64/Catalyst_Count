from django.urls import path
from .views import *

urlpatterns = [
    path('upload_file/', upload_file, name='upload_file'),
    path('query_builder/', query_builder, name='query_builder'),
    path('users/', users, name='users'),
    path('users/<int:pk>/', users, name='users'),
]