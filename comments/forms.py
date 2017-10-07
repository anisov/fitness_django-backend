from django import forms
from .models import CommentPost

class CommentForm(forms.ModelForm):
    name = forms.CharField(label='Имя пользователя',error_messages={'required': 'Please enter your name', 'invalid': 'Пожалуйста, введите ваше Имя корректно.'},widget=forms.TextInput(attrs={'class': 'form__input','placeholder':'Андрей'}))
    vk = forms.URLField(error_messages={'required': 'Пожалуйста, введите корректный адрес вашего vk.', 'invalid': 'Пожалуйста, введите корректный адрес вашего vk.'}, widget=forms.TextInput(attrs={'class': 'form__input','placeholder':'vk.com/example'}))
    text  = forms.CharField(label='Комментарий',error_messages={'required': 'Please enter your comment', 'invalid': 'Пожалуйста, введите ваш комментарий корректно.'}, widget=forms.Textarea(
        attrs={'class': 'form__big-text-input', 'placeholder': 'Мне понравилось'}))
    img_on_choices = [
        ('True', 'Да'),
        ('False', 'Нет')
    ]
    img_on = forms.CharField(widget=forms.RadioSelect(choices=img_on_choices,attrs={'class': 'form__input-radio','type':'radio'}))
    honeypot = forms.CharField(required=False,label="hidden",
                              widget=forms.TextInput(
                                  attrs={'class': 'hidden','type':'hidden',
                                         'placeholder': 'Скрытое поле'}))
    img = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form__img','placeholder':'Загрузить'}))

    class Meta:
        model = CommentPost
        fields = ('name', 'vk', 'text','img_on','honeypot','img')