from django.contrib import admin
from books.models import Category, Author, Book, Borrow, Review
# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['category_name']}
    list_display = ['category_name', 'slug']

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['author_name']

class BookAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug' : ['name']}
    list_display = ['name', 'slug', 'price', 'category', 'quantity', 'author', 'date']

class BorrowAdmin(admin.ModelAdmin):
    list_display = ['learner', 'book_name', 'price', 'borrowed_date', 'status', 'return_date']
    def book_name(self, obj):
        return obj.book.name
    def price(self, obj):
        return obj.book.price
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['learner_name', 'learner_email', 'review_text', 'book', 'review_date']
    def learner_name(self, obj):
        return obj.learner.user.username
    def learner_email(self, obj):
        return obj.learner.user.email
    

admin.site.register(Category, CategoryAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Borrow, BorrowAdmin)
admin.site.register(Review, ReviewAdmin)