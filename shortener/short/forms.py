from django.forms import ModelForm

from .models import Link


class ShortForm(ModelForm):
    class Meta:
        model = Link
        fields = ('url',)
