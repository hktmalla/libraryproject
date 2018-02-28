from django import forms
from .models import *


class AdminLoginForm(forms.Form):
    user_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_name', 'roll_number', 'address', 'phone_number', 'batch']

        def __init__(self, *args, **kwargs):
            super.__init__(*args, **kwargs)
            for field in iter(self.fields):
                self.fields[field].widget.attrs.update(
                    {'class': 'form-control'}
                )
