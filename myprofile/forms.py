from django.db import models
from django import forms
from .models import Message

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['name','email','message']