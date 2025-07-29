from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Student

def home(request):
    students = Student.objects.all()
    return render(request, 'home.html', {'students': students})

def welcome(request):
    return render(request, 'welcome.html')

def search(request):
    query = request.GET.get('name')
    if query:
        students = Student.objects.filter(name__icontains=query)
        if not students:
            return render(request, 'home.html', {'nodata': True})
        return render(request, 'home.html', {'students': students})
    #return render(request, 'home.html', {'nodata': True})

def stu_information(request, id):
    student = get_object_or_404(Student, id=id)
    return render(request, 'inform.html', {'student': student})