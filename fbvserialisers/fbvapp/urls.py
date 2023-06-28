from django.urls import path
from fbvapp.views import student_list, student_detail

urlpatterns = [
    path('students/',student_list),
    path('students/<int:pk>',student_detail),
]