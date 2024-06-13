from django import forms
from .models import Task


class TodoCreateForm(forms.ModelForm):
    """Create a new task form."""

    title = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))

    class Meta:
        model = Task
        fields = ["title"]
