# from django import forms
# from django.forms import fields
from django.forms.models import ModelForm
from .models import Material, Chapter
# from django.forms import models


class MaterialForm(ModelForm):
    class Meta:
        model = Material
        exclude = ['chapter']
        # fields = '__all__'


class ChapterForm(ModelForm):
    class Meta:
        model = Chapter
        # fields = '__all__'
        exclude = ['subject']
