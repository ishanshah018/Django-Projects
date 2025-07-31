from django.shortcuts import render
from .models import Book

def search(request):
    query=request.GET.get('query')
    books=[]
    
    if query:
        books=Book.objects.filter(b_name=query) | Book.objects.filter(a_name=query)
        
    return render(request,'book_form.html',{
        'books':books,
        'query':query
    })