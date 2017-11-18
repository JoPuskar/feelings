from django import forms

from . import models
from .models import Thought

class ThoughtForm(forms.ModelForm):
    class Meta:
        fields = ('condition', 'notes')
        model = models.Thought

