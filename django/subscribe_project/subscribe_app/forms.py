from django import forms
from subscribe_app.models import Customers

class NewSubscriber(forms.ModelForm):
    class Meta():
        model = Customers
        fields = '__all__'