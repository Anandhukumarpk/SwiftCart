from django import forms

from .models import Contactus



class ContactForm(forms.ModelForm):
    class Meta:  # Capitalized Meta
        model = Contactus  # Specify the model
        fields = ['Name', 'Email', 'Message']  # Specify the fields









   





       