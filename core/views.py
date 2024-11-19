from django.shortcuts import render
from books.models import Book, Category

def home(request, category_slug = None):
    data = Book.objects.all()
    category = None

    if category_slug is not None:
        category = Category.objects.get(slug = category_slug)
        data = Book.objects.filter(category = category)

    category = Category.objects.all()

    return render(request, 'core/index.html', {'books' : data, 'category' : category})