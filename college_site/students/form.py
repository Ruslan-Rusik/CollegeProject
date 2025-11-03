from django.forms import ModelForm
from django import forms
from .models import Student, Profile
from django.contrib.auth.models import User


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('photo', 'name', 'last_name', 'age', 'group', 'clubs')

        widgets = {
            "clubs": forms.CheckboxSelectMultiple(),
        }


class RegisterForm(ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta: 
        model = User
        fields = ['username', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Пароли не совпадают!")
        return cleaned_data 
    
class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('location', 'group', 'clubs')

        widgets = {
            "clubs": forms.CheckboxSelectMultiple(),
        }
