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
            'is_parking',
            'is_pet',
            'is_smoking',
            'has_hydro',
            'has_aircondition',
            'has_water',
            'has_heat',
            'has_wifi',
            'has_tv',
            'has_laundry',
            'has_fridge',
            'has_dishwasher',
            'has_dryer',
            'has_microwave',
            'movein_date',
            )
        widgets = {
            'title' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a title'}),
            'address' : forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter a address'}),
            'latitude' : forms.TextInput(attrs={'class':'d-none form-control w-50', 'placeholder':'Enter a latitude'}),
            'longitude' : forms.TextInput(attrs={'class':'d-none form-control w-50', 'placeholder':'Enter a longitude'}),
            'description' : forms.Textarea(attrs={'class':'form-control', 'placeholder':"Describe the decor, light, what's nearby, ect...",'rows':5}),
            'price' : forms.TextInput(attrs={'class':'form-control w-50', 'placeholder':'Enter a price'}),
            'is_parking' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'is_pet' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'is_smoking' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_hydro' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_aircondition' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_water' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_heat' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_wifi' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_tv' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_laundry' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_fridge' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_dishwasher' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_dryer' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'has_microwave' : forms.CheckboxInput(attrs={'class':'d-none'}),
            'movein_date' : forms.DateTimeInput(attrs={'class':'form-control', 'placeholder':'Enter a move-in date'}),
        }

class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ('image',)
        widgets = {
            'image' : forms.ClearableFileInput(attrs={'multiple':True})
        }
    
