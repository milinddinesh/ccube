from django import forms
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User
from .models import User_info

class NewUserForms(forms.ModelForm):
    class Meta:
        model = User_info
        fields = ("email","first_name", "last_name", "phone")


# class NewUserForms(UserCreationForm):
#     first_name = forms.CharField(max_length=100)
#     last_name = forms.CharField(max_length=100)
#     phone = forms.CharField(max_length=100)
#     email = forms.CharField(max_length=100)

#     class Meta:
#         model = User_info
#         fields = ("email","first_name", "last_name", "phone")

#     def save(self, commit=True):
#         user = super(NewUserForms, self).save(commit=False)
#         user.first_name = self.cleaned_data['first_name']
#         user.last_name = self.cleaned_data['last_name']
#         user.email = self.cleaned_data['email']
#         user.phone = self.cleaned_data['phone']
#         if commit:  
#             user.save()
#         return user
    
#     def clean(self):
#         cleaned_data = super().clean()
#         # remove password fields from cleaned_data
#         cleaned_data.pop('password1', None)
#         cleaned_data.pop('password2', None)
#         return cleaned_data