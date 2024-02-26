from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookForm
from book.models import Book

def index(request):
    books = Book.objects.all()

    context ={'books': books}

    return render(request, 'book/index.html', context)

def detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {'book': book}
    return render(request, 'book/detail.html', context)

def add(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('book:index')
    
    form = BookForm()

    context = {'form': form}

    return render(request, 'book/add.html', context)

def edit(request, pk):
    book = Book.objects.get(pk=pk)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()

            return redirect('book:index')
    else:
        form = BookForm(instance=book)
        

    context = {'form': form}

    return render(request, 'book/edit.html', context)

def delete(request, pk):
    book = get_object_or_404(Book, pk=pk)

    book.delete()

    return redirect('book:index')





