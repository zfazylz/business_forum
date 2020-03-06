from .models import FeedBack
from django import forms


class FeedBackForm(forms.ModelForm):
    class Meta:
        model = FeedBack
        fields = ('name', 'email', 'message')
