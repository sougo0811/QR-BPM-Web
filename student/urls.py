from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_list/', views.student_list, name='student_list'),
    path('student/<int:pk>/', views.student_detail, name='student_detail'),
    path('student/<int:pk>/send_email/', views.student_send_email, name='student_send_email')
]