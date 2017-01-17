# -*-coding:utf-8;-*-
from __future__ import unicode_literals
from django.forms import ModelForm, TextInput, Textarea, HiddenInput, NumberInput
from index import models


class OrderForm(ModelForm):
    class Meta:
        model = models.Order
        fields = ('visitor', 'phone', 'message',)
        widgets = {
            'visitor': HiddenInput(),
            'phone': NumberInput(attrs={'class': 'form-control', 'placeholder': 'номер телефона'.capitalize()}),
            'message': Textarea(attrs={'class': 'form-control', 'placeholder': 'Сообщение'.capitalize()})
        }
