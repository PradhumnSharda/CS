from django import forms
from django.contrib.auth.models import User
from customers.models import customer_order_model
from django.core.validators import RegexValidator
from django.core.validators import validate_email


class customer_order_form(forms.ModelForm):
    
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    phone_number= forms.CharField(validators = [phoneNumberRegex])

    class Meta():
        model = customer_order_model
        fields= '__all__'
        widgets = {
         'fitment_position': forms.Textarea(attrs={
                              'style': 'height: 30px;width:300px'}),
         'tyre_number': forms.Textarea(attrs={
                              'style': 'height: 30px;width:300px'}),

        'date': forms.DateInput(attrs={'class':'datepicker'}),

       }
