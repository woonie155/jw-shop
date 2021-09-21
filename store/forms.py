from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
  class Meta:
    model = Product
    fields = '__all__'



class CreateUserForm(UserCreationForm):
  email = forms.EmailField(required=True)
  class Meta:
    model = User
    fields = ("username", "email", "password1", "password2")
  def save(self, commit=True):
    user = super(CreateUserForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    if commit:
      user.save()
    return user
