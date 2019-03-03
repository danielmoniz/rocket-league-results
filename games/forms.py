
from django import forms

from . import models


class GameForm(forms.ModelForm):
    # blue_score = forms.IntegerField(min_value=0)
    # orange_score = forms.IntegerField(min_value=0)
    # overtime = forms.BooleanField(required=False)
    # overtime_length = forms.IntegerField(min_value=0)

    class Meta:
        model = models.Game
        fields = ['blue_score', 'orange_score', 'overtime', 'overtime_length']
