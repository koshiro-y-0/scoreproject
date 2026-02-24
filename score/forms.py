from django.forms import ModelForm
from .models import Score
from django import forms

class ScoreForm(ModelForm):
    class Meta:
        model = Score
        fields = ['date', 'subject', 'score']
        widgets = {
            'date': forms.DateInput(attrs={
                'type': 'date',  # HTML5のカレンダーウィジェット
                'class': 'form-control'
            }),
            'subject': forms.Select(attrs={
                'class': 'form-control'
            }),
            'score': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': 0,
                'max': 100
            })
        }
