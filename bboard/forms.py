from django.forms import ModelForm, CheckboxInput, RadioSelect
from django import forms
from .models import Bb



class BbForm(ModelForm):
    class Meta:
        model = Bb
        fields = ('title', 'content', 'price', 'rubric', 'fast_sell', 'favorite_fruit')
        FRUIT_CHOICES = [
            ('orange', 'Новый'),
            ('cantaloupe', 'Б/У'),
            ('mango', 'Битый'),
            ('honeydew', 'На запчасти'),
        ]
        favorite_fruit = forms.CharField(label='What is your favorite fruit?',
                                         widget=forms.RadioSelect(choices=FRUIT_CHOICES))
        widgets = {
            'fast_sell': CheckboxInput(attrs={'class': 'required checkbox form-control'}),
            'favorite_fruit' : RadioSelect(attrs={'class' : 'required checkbox form-control'},
                                           choices=FRUIT_CHOICES)
        }
