from django.shortcuts import render, redirect
from .form import BookForm
from .models import Book

def index(request):
    if request.method == 'POST':
        form = BookForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            obj= form.instance
            return render(request, 'index.html',{'obj':obj})
    else:
         form = BookForm()
    img=Book.objects.all()
    return render(request, 'index.html',{'img':img, 'form': form})
     