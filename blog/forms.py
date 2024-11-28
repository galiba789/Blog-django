from django import forms
from .models import Commennt

class CommentForms(forms.ModelForm):
    class Meta:
        model = Commennt
        fields = ['name', 'email', 'body']