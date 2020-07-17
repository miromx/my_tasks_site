from django import forms
from .models import Must
import re
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class MustForm(forms.ModelForm):

    class Meta:
        model = Must
        # fields = '__all__' # вывестеи все поля
        fields = ['title']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            # 'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            # 'category': forms.Select(attrs={'class': 'form-control'}),
        }

    # def clean_title(self):
    #     """
    #     кастомный валидатор
    #     :return:
    #     """
    #     title = self.cleaned_data['title']
    #     if re.match(r'\d', title):
    #         raise ValidationError('Название не должно начинаться с цифры')
    #     return title
