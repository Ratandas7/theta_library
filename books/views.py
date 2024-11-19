from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import DetailView
from books.models import Book, Borrow
from django.contrib import messages
from books.forms import ReviewForm
from django.contrib.auth.decorators import login_required
from accounts.models import UserAccount
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def send_book_email(user, book_name, book_price, subject, template):
    message = render_to_string(template, {
        'user': user,
        'book_name' : book_name,
        'book_price' : book_price,
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_details.html'
    slug_field = 'slug'
    slug_url_kwarg = 'book_slug'

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        review_form = ReviewForm(data = self.request.POST)
        if review_form.is_valid():
            new_review = review_form.save(commit=False)
            new_review.book = self.object
            new_review.learner = request.user.account
            new_review.save()
            messages.success(self.request, "Your Feedback Added Successfully!")
            return redirect('book_details', book_slug=self.object.slug, pk=self.object.pk)
        else:
            return self.get(request, *args, **kwargs)
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        book = self.object
        reviews = book.reviews.all()

        user_review = book.reviews.filter(learner=self.request.user.account).first() if self.request.user.is_authenticated else None
        has_borrowed = Borrow.objects.filter(learner=self.request.user.account, book=book).exists() if self.request.user.is_authenticated else False
        review_form = ReviewForm() if not user_review and has_borrowed else None

        context['reviews'] = reviews
        context['review_form'] = review_form
        context['has_borrowed'] = has_borrowed
        # context['user_review'] = user_review
        return context
    

@login_required
def borrow_now(request, book_slug, id):
    book = get_object_or_404(Book, slug=book_slug, pk=id)

    if request.method == 'POST':
        user_account = UserAccount.objects.get(user=request.user)

        if book.quantity > 0:
            
            if user_account.balance >= book.price:
                Borrow.objects.create(learner=user_account, book=book)
                user_account.balance -= book.price
                user_account.save()

                book.quantity -= 1
                book.save()

                messages.success(request, f"You have successfully borrowed ({book.name}). Your remaining balance is {user_account.balance:.2f}.")

                send_book_email(request.user, book.name, f"{book.price:.2f}", "Book Borrowed Message", "books/borrow_book_email.html")

                return redirect('borrow_history')
            
            else:
                messages.error(request, "Insufficient balance to borrow this book.")
                return redirect('book_details', book_slug=book.slug, pk=id)
            
        else:
            messages.error(request, f"Sorry, {book.name} is out of stock.")
            return redirect('book_details', book_slug=book.slug, pk=id)

    return redirect('home')



@login_required
def return_book(request, book_slug, id):
    book = get_object_or_404(Book, slug=book_slug, pk=id)
    user_account = get_object_or_404(UserAccount, user=request.user)

    borrow = Borrow.objects.filter(learner=user_account, book=book, status='borrowed').first()

    if borrow:
        borrow.status = 'returned'
        borrow.return_date = timezone.now()
        borrow.save()

        user_account.balance += book.price
        user_account.save()

        messages.success(request, f'({book.name}) Book returned successfully! ${book.price} has been added to your account balance.')

        send_book_email(request.user, book.name, f"{book.price:.2f}", "Book Returned Message", "books/return_book_email.html")

    else:
        messages.error(request, "No active borrow record found for this book.")

    return redirect('borrow_history')







 