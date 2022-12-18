from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = {'title', 'text', 'annotation', 'gener', }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'post_atribute'}),
            'text': forms.Textarea(attrs={'cols': 100, 'rows': 20, 'class': 'post_atribute'}),
            'annotation': forms.Textarea(attrs={'cols': 100, 'rows': 20,'class': 'post_atribute'}),
            'gener': forms.Textarea(attrs={'cols': 20, 'rows': 1, 'class': 'post_atribute'}),
        }