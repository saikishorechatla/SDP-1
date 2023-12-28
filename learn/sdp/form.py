from django import forms
from .models import *


class moviepicForm(forms.ModelForm):
    class Meta:
        model = moviepic
        fields = [ 'avatar']