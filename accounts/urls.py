from django.urls import path
from accounts.views import UserRegistrationView, UserLoginView, UserLogoutView, UserProfileUpdateView, ChangePasswordView, BorrowHistoryView

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', UserProfileUpdateView.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('account/borrow_history/', BorrowHistoryView.as_view(), name='borrow_history'),
]
