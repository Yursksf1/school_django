from django.contrib import admin
from django.urls import path
from .views import subject, students, index

urlpatterns = [
    path('', index),
    path('subject', subject),
    path('students', students),
]
