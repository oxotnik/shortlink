from django import forms

from .models import ShortLinks


class ShortLinksForm(forms.ModelForm):
    """ Форма ввода линка """

    class Meta:
        model = ShortLinks
        fields = ("url", "date_create")
