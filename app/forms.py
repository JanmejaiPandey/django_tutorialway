from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    username = forms.CharField(
         widget = forms.TextInput(
             attrs={
                "class":"form-control",
                "placeholder":"Enter Your name"
             }
         )
    )
    password = forms.CharField(
         widget = forms.PasswordInput(
             attrs={
                "class":"form-control",
                "placeholder":"Enter Password"
             }
         )
        )

class SignUpForm(forms.Form):
    username = forms.CharField(
        widget = forms.TextInput(
             attrs={
                "class":"form-control",
                "placeholder":"Enter Your name"
             }
             )
    )
    email = forms.EmailField(
        widget = forms.EmailInput(
             attrs={
                "class":"form-control",
                "placeholder":"Enter Your Email"
             }
             )
    )
    password = forms.CharField(widget = forms.PasswordInput(
         attrs={
                "class":"form-control",
                "placeholder":"Enter Password"
             }
    ))
    password2 = forms.CharField(label="Confirm Password", widget = forms.PasswordInput(
         attrs={
                "class":"form-control",
                "placeholder":"Enter Password Again"
             }
    ))
    
    def clean_username(self):
        User = get_user_model()
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError("Username is taken")
        return username
    
    def clean_email(self):
        User = get_user_model()
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean(self):
        data = self.cleaned_data
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password != password2:
            raise forms.ValidationError("Password must match.")
        return data