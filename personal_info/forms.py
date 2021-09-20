# -*- coding:utf-8 -*-
# Author: Zachary
from django import forms

# 这里是对应的views.py -> class PersonCreate(View)的Form:
from personal_info.models import Person

"""
class PersonCreateForm(forms.Form):
    name = forms.CharField(max_length=32)
    age = forms.IntegerField()
    gender = forms.BooleanField()
    id_card = forms.CharField(max_length=18)
    address = forms.CharField(max_length=255)
    temperature = forms.FloatField()

"""


# 这里是对应的views.py -> class PersonCreate(CreateView):的Form:
# 使用的是ModelForm
class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'
        # fields = ('name','age',...) 也可以这样子写

        widgets = {
            'name': forms.TextInput(attrs={'id': 'name_id', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'id': 'age_id', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'id': 'gender_id', 'class': 'form-select'}),
            'id_card': forms.TextInput(attrs={'id': 'id_card_id', 'class': 'form-control'}),
            'address': forms.TextInput(attrs={'id': 'address_id', 'class': 'form-control'}),
            'temperature': forms.NumberInput(attrs={'id': 'temperature_id', 'class': 'form-control', 'step': '0.1'}),

        }

        labels = {
            'name': '名字',

        }

class PersonUpdateForm(PersonCreateForm):
    pass
