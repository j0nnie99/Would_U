from django import forms
from .models import Community
import datetime


class PostForm(forms.ModelForm):
    class Meta:
        model = Community
        fields = ['title','body']
        widgets = {
            'title' : forms.TextInput(
                attrs = {
                    'class' : 'form-control',
                    'required' : False,
                    'placeholder' : '글제목을 입력해주세요.',
                }
            ),
            'body' : forms.Textarea(
                attrs = {
                    'class' : 'form-control',
                    'type' : 'textarea',
                }
            ),
        }