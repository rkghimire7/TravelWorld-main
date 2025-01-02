from django import forms
from  travello.models import Guide



class GuideForm(forms.ModelForm):
    class Meta:
        model = Guide
        fields = [
            'civility', 'first_name', 'last_name', 'email', 'phone_number',
            'country', 'city_or_region', 'mother_tongue', 'tour_languages',
            'presentation', 'photo', 'certified_guide', 'guide_card', 'message'
        ]
        widgets = {
            'tour_languages': forms.TextInput(attrs={'placeholder': 'Enter at least one language'}),
            'presentation': forms.Textarea(attrs={'rows': 5, 'placeholder': 'Write a few lines about yourself'}),
            'message': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Optional message'}),
        }
