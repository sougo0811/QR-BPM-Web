from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import StudentInfo

def index(request):
  return render(request, 'student/index.html', {})

def student_list(request):
    students = StudentInfo.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
    return render(request, 'student/student_list.html', {'students' : students})

def student_detail(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    return render(request, 'student/student_detail.html', {'student' : student})

def student_send_email(request, pk):
    student = get_object_or_404(StudentInfo, pk=pk)
    
    student.count += 1
    student.save()
    return render(request, 'student/student_send_email.html', {'student' : student})