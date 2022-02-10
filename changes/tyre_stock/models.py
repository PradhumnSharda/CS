from django.db import models
from django.urls import reverse
import datetime
from django.utils import timezone
from django.contrib.admin.widgets import AdminDateWidget
# Create your models here.

class tyre_stockmodel(models.Model):

    tyre_name = models.CharField(max_length=50, unique=True, blank=False, error_messages ={
                    "unique":"This Tyre model already exists. Please use another name."})

    number_of_tyres = models.PositiveIntegerField(blank=False)
    reorder_number = models.PositiveIntegerField(blank=False)
    date_refreshed = models.DateField(auto_now=True)
    price = models.PositiveIntegerField(blank=False)
    commercial_vehicle_tyre = models.BooleanField(default=False)

    def __str__(self):
        return str(self.tyre_name)

    def get_absolute_url(self):
        return reverse("tyre_stock:tyre_detail", kwargs={'pk':self.pk})

class new_stock(models.Model):
    tyre_name_new = models.ForeignKey(tyre_stockmodel, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    bought_from = models.CharField(max_length=30)
    date_added = models.DateField(default=timezone.now)


    def __str__(self):
        return str(self.tyre_name_new)

    def get_absolute_url(self):
        return reverse("tyre_stock:new_stock_detail", kwargs={'pk':self.pk})
