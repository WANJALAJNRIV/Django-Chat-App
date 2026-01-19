from django import forms
from django.forms import ModelForm
from .models import GroupMessage, ChatGroup



class ChatMessageCreateForm(ModelForm):
    class Meta:
        model = GroupMessage
        fields = ['body']
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add Message ...'})
        }