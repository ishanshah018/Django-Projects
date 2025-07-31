from django.shortcuts import render
from .models import Student

def search(request):
    student = None
    roll_no = request.GET.get('roll_no')  
    if roll_no:
        try:
            student = Student.objects.get(roll_no=roll_no)
        except Student.DoesNotExist:
            student = None

    return render(request, 'student_form.html', {
        'student': student,
        'roll_no': roll_no,
    })