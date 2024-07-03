from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('student/', post_student, name='post_student'),
    path('update-student/<int:id>/', update_student, name='update_student'),
    path('delete-student/<int:id>/', delete_student, name='delete_student'),
]
