import fileinput
from .models import Artiles
from django.forms import *

class ContactForm(forms.Form):
    subject = CharField(label = 'Ваша почта или номер телефона')
    content = CharField(label = 'Текст письма')

class ArtilesForm(ModelForm):
    class Meta:
        model = Artiles
        ContactForm = ContactForm
        fields = ['title', 'anons', 'full_text', 'date', 'image']
        
        widgets = {
            "subject": TextInput(attrs={
                'class': 'form-control'
            }),
            "content": Textarea(attrs={
                'class': 'form-control'
            }),
            "title": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Название материала',
            }),
            "anons": TextInput(attrs={
                'class': 'form-control', 
                'placeholder': 'Анонс материала',
                'style': 'float: left;'
            }),
            "text_full": Textarea(attrs={
                'class': 'form-control', 
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите дату'
            }),
            "image": FileInput(attrs={
                'type': 'file',
                'style': 'float: left;'
            })
        }