from django import forms

from .models import Response


class DailyPromptForm(forms.ModelForm):
    class Meta:
        model = Response
        exclude = ["user", "question", "created"]
