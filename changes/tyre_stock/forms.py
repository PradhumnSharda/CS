from django import forms
from tyre_stock.models import new_stock
from bootstrap_datepicker.widgets import DatePicker

class new_stock_form(forms.ModelForm):

    class Meta:
        model = new_stock
        fields = '__all__'
        widgets = {
            'date_added': forms.DateInput(attrs={'class':'datepicker'}),
        }
