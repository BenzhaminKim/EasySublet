from django import forms
from .models import Room,Image

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = (
            'title',
            'address',
            'latitude',
            'longitude',
            'description',
            'price',
            'has_laundry',
            'has_fridge',
            'has_wifi',
            'movein_date',
            )
        widgets = {
            'description' : forms.Textarea(attrs={'rows':20, 'cols':20}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'multiple':True, 'required':False})
        }
    
