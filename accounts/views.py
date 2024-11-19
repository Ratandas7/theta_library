from django.shortcuts import render, redirect
from django.views.generic import FormView, TemplateView
from accounts.forms import UserRegistrationForm, UserUpdateForm
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth import logout
from django.views import View
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from books.models import Borrow
from accounts.models import UserAccount
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives

# Create your views here.

def send_account_email(user, subject, template):
    message = render_to_string(template, {
        'user' : user
    })
    send_email = EmailMultiAlternatives(subject, '', to=[user.email])
    send_email.attach_alternative(message, "text/html")
    send_email.send()


class UserRegistrationView(FormView):
    form_class = UserRegistrationForm
    template_name = 'accounts/user_registration.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'

    def get_success_url(self):
        return reverse_lazy('home')
    
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    

class UserLogoutView(LogoutView):
    def get_success_url(self):
        if self.request.user.is_authenticated:
            logout(self.request)
        return reverse_lazy('home')


@method_decorator(login_required, name='dispatch')
class UserProfileUpdateView(View):
    template_name = 'accounts/user_profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form' : form})
    
    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Updated profile successfully!')
            return redirect('profile')
        return render(request, self.template_name, {'form' : form})


class ChangePasswordView(LoginRequiredMixin, PasswordChangeView):
    template_name = 'accounts/change_password.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        messages.success(self.request, 'Password has been changed successfully!')

        send_account_email(self.request.user, "Password Changed", "accounts/change_password_email.html")
        
        return super().form_valid(form)



@method_decorator(login_required, name='dispatch')
class BorrowHistoryView(TemplateView):
    template_name = 'accounts/borrow_history.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
       
        user_account = UserAccount.objects.get(user=self.request.user)
        
        context['borrows'] = Borrow.objects.filter(learner=user_account)
        return context