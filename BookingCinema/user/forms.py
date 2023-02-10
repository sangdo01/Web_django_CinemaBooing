
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# class registerForm(forms.Form):
#     username = forms.CharField(max_length=20)
#     email = forms.CharField(max_length=50)
#     sdt = forms.CharField(max_length=10)
#     pass1 = forms.CharField(max_length=20)
#     pass2 = forms.CharField(max_length=20)

# class NewUserForm(UserCreationForm):
#     email = forms.EmailField(required=True)
#     class Meta:
#         model = User
#         fields = ['username', 'email', 'password1', 'password2']

#     def save(self, commit=True):
#         user = super(NewUserForm, self).save(commit=False)
#         user.email = self.cleaned_data['email'] 
#         if commit:
#             user.save()
#         return user

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']