from django import forms
from .models import OmbPost

class OmbPostForm(forms.ModelForm):
    ''' コメント投稿用のフォーム '''
    class Meta:
        model = OmbPost
        fields = ['name', 'subject', 'comment']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '投稿名'}),
            'subject': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'コメントを入力'}),
        }