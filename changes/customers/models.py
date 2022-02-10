from django.db import models
from django.contrib.auth.models import User
from tyre_stock.models import tyre_stockmodel
from django.urls import reverse
import datetime
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import RegexValidator
from django.core.validators import validate_email
# Create your models here.

pay = [
    ('CASH', 'CASH'),
    ('CREDIT', 'CREDIT'),
    ('KOTAK', 'KOTAK'),
    ('SBI', 'SBI'),
    ('HDFC', 'HDFC')
]

class customer_order_model(models.Model):

    customer_name = models.CharField(max_length=30, blank=False, null=False)
    company_name = models.CharField(max_length=30, blank=False, null=False)
    tyre_model = models.ForeignKey(tyre_stockmodel, on_delete=models.CASCADE)
    tyre_number = models.TextField(max_length=200, blank=False, null=False)
    quantity = models.IntegerField(blank=False, null=False)
    fitment_position = models.TextField(max_length=200, blank=True, null=True)
    mail_id = models.CharField(max_length=254, null=False, blank=False)
    phone_number= models.CharField(max_length = 16)
    date = models.DateField(default=timezone.now)
    payment_method = models.CharField(max_length=100, choices=pay)
    vehicle_number = models.CharField(max_length=10, blank=True, null=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    payment_done = models.BooleanField(default=False, blank=False, null=False)


    def __str__(self):
        return str(self.customer_name)

    def get_absolute_url(self):
        return reverse("customers:order_detail", kwargs={'pk':self.pk})

#    def save(self, *args, **kwargs):
#        if not self.pk:
#            tyre_stockmodel.objects.get(self.tyre_model_id).update(number_of_tyres = F('number_of_tyres')-('quantity'))
#        super.save(*args, **kwargs)
