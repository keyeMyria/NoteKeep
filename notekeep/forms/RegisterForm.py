from django import forms
from django.contrib.auth.models import User
from django.db.models import Q


def user_exists(username, email):
    return User.objects.filter(Q(username=username) | Q(email=email)).count() > 0


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=100)
    email = forms.EmailField(max_length=100)
    password = forms.CharField(max_length=100)
    password2 = forms.CharField(max_length=100)

    def clean(self):
        cleaned_data = super().clean()
        self.username = cleaned_data.get("username")
        self.email = cleaned_data.get("email")
        self.password = cleaned_data.get("password")
        self.password2 = cleaned_data.get("password2")

        if len(self.username) == 0 or len(self.email) == 0 or len(self.password) == 0 or self.password != self.password2:
            raise forms.ValidationError("Some fields are wrong", code="fields")

        if user_exists(self.username, self.email):
            raise forms.ValidationError("User already exists", code="user")