from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from accounts.models import UserAccount

class UserRegistrationForm(UserCreationForm):
    
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def save(self, commit = True):
        our_user = super().save(commit=False)
        if commit == True:
            our_user.save()

            UserAccount.objects.create(
                user = our_user
            )
        return our_user

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.fields['email'].required = True

        self.fields['username'].error_messages = {
            'required' : 'Please enter your username.'
        }
        self.fields['first_name'].error_messages = {
            'required' : 'Please enter your first name.'
        }
        self.fields['last_name'].error_messages = {
            'required' : 'Please enter your last name.'
        }
        self.fields['email'].error_messages = {
            'required' : 'Please enter a valid email address.',
        }
        self.fields['password1'].error_messages = {
            'required' : 'Please enter a password.',
        }
        self.fields['password2'].error_messages = {
            'required' : 'Please confirm your password.',
        }


class UserUpdateForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if 'username' in self.fields:
            self.fields['username'].widget.attrs['readonly'] = True

        if self.instance:
            try:
                user_account = self.instance.account
            except UserAccount.DoesNotExist:
                user_account = None

    def save(self, commit = True):
        our_user = super().save(commit=False)

        if commit == True:
            our_user.save()

            user_account, created = UserAccount.objects.get_or_create(user=our_user)

            user_account.save()

        return our_user