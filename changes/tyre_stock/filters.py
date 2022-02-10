import django_filters
from django import forms
from tyre_stock.models import tyre_stockmodel, new_stock
from django_filters import DateFromToRangeFilter, DateFilter
from bootstrap_datepicker.widgets import DatePicker


class DateInput(forms.DateInput):
    input_type = 'date'

class TyreFilter(django_filters.FilterSet):
    class Meta:
        model = tyre_stockmodel
        fields = ['tyre_name', 'commercial_vehicle_tyre']

class New_stock_filter(django_filters.FilterSet):

    date_added = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
    ),field_name='date_added')

    start_date = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
    ),field_name='date_added',lookup_expr=('gt'), label='Date From (>)')

    end_date = django_filters.DateFilter(widget=DateInput(
        attrs={
            'class': 'datepicker'
        }
    ),field_name='date_added',lookup_expr=('lt'), label='Date To (<)')


    class Meta:
        model = new_stock
        fields = ['tyre_name_new', 'id', 'bought_from']
