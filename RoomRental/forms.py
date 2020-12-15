from django import forms
from .models import Room

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ('title','content')
        widgets = {
            'content' : forms.Textarea(attrs={'rows':20, 'cols':20}),
        }