from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import reverse
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate


class SignupForm(UserCreationForm):
    """Customize UserCreationForm"""

    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        # Add placeholder to the fields
        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["password1"].widget.attrs.update({"placeholder": "Password"})
        self.fields["password2"].widget.attrs.update({"placeholder": "Repeat Password"})

    # add email field to UserCreationForm
    email = forms.EmailField(widget=forms.EmailInput(attrs={"placeholder": "Email"}))

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        url = reverse("sign_in")
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError(
                format_html(
                    'This email is already exist! <a href="{0}">sign in</a>', url
                )
            )
        return email


class SignInForm(AuthenticationForm):
    """Customize AuthenticationForm"""

    def __init__(self, *args, **kwargs):
        super(SignInForm, self).__init__(*args, **kwargs)
        # Add placeholder to the fields
        self.fields["username"].widget.attrs.update({"placeholder": "Username"})
        self.fields["password"].widget.attrs.update({"placeholder": "Password"})

    class Meta:
        fields = ("username", "password")

    def clean_password(self):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        user = authenticate(
            username=username,
            password=password,
            backend="django.contrib.auth.backends.ModelBackend",
        )
        if user is not None:
            return password
        else:
            raise forms.ValidationError("Username or password is incorrect!")
