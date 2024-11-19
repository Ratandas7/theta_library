from django.urls import path
from books.views import BookDetailView, borrow_now, return_book

urlpatterns = [
    path('<slug:book_slug>/<int:pk>/', BookDetailView.as_view(), name='book_details'),
    path('borrow_now/<slug:book_slug>/<int:id>/', borrow_now, name='borrow_now'),
    path('return/<slug:book_slug>/<int:id>', return_book, name='return_book'),
]
