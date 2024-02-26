from django.shortcuts import render, redirect
from .models import Author
from .forms import AuthorForm

def index(request):
    athrs = Author.objects.all()
    context = {'authors': athrs}
    return render(request, 'authors/index.html', context)

def add(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors:index')

    else:
        form = AuthorForm()
    context = {'form': form}
    return render(request, 'authors/add.html', context)

def detail(request, pk):
    author = Author.objects.get(pk=pk)

    context = {'author': author}


    return render(request, 'authors/detail.html', context)

