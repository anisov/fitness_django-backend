from django import forms

from .models import Comment_post

class CommentForm(forms.ModelForm):
    user_name = forms.CharField(label='Имя пользователя',error_messages={'required': 'Please enter your name'},widget=forms.TextInput(attrs={'class': 'form-control','id':'comment-name','placeholder':'Имя'}))
    email = forms.EmailField(error_messages={'required': 'Please enter your name'}, widget=forms.TextInput(attrs={'class': 'form-control','id': 'comment-email','placeholder':'Ваш email'}))
    content  = forms.CharField(label='Комментарий',error_messages={'required': 'Please enter your name'}, widget=forms.Textarea(
        attrs={'class': 'form-control', 'id': 'comment-editor', 'placeholder': 'Комментарий'}))
    honeypot = forms.CharField(required=False,label="hidden",
                              widget=forms.TextInput(
                                  attrs={'class': 'hidden','type':'hidden',
                                         'placeholder': 'Скрытое поле'}))
    class Meta:
        model = Comment_post
        fields = ('user_name', 'email', 'content','honeypot')