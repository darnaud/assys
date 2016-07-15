from django.db import models
from django.utils import timezone
# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	make = models.CharField(max_length=200)
	description = models.TextField(default="")
	publish_date = models.DateField(default = timezone.now)
	price = models.DecimalField(default=0.00,decimal_places=2, max_digits=8)
	stock = models.IntegerField(default=0)