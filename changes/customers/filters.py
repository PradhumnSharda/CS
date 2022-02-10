import django_filters
from customers.models import customer_order_model
from django_filters import DateFromToRangeFilter, DateFilter
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class OrderFilter(django_filters.FilterSet):

    date_added = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
        ),field_name='date', label="Date added")

    start_date = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
        ),field_name='date',lookup_expr=('gt'), label='Date From (>)')

    end_date = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
        ),field_name='date',lookup_expr=('lt'), label='Date To (<)')


    class Meta:
        model = customer_order_model
        fields = ['id','customer_name','company_name','mail_id','phone_number', 'payment_done', 'tyre_model', 'location','vehicle_number']
