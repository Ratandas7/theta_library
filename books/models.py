from django.db import models

# Create your models here.
from django.db import models
from accounts.models import UserAccount
from books.constants import STATUS_CHOICES

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.category_name
    

class Author(models.Model):
    author_name = models.CharField(max_length=50)

    def __str__(self):
        return self.author_name


class Book(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='books/media/uploads')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now_add=True)
    quantity = models.PositiveIntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    
class Borrow(models.Model):
    learner = models.ForeignKey(UserAccount, on_delete=models.CASCADE, related_name="borrow")
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="books")
    borrowed_date = models.DateTimeField(auto_now_add=True)
    return_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='borrowed')

    def __str__(self):
        return f"{self.book.name} - {self.learner.user.username}"



class Review(models.Model):
    learner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name="reviews")
    review_text = models.TextField()
    review_date = models.DateTimeField(auto_now_add=True)
    

    def __str__(self):
        return f"Review by {self.learner.user.username} for {self.book.name}"