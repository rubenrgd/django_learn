from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Listing(models.Model):
    realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
    hostname = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    manufacturer = models.CharField(max_length=200)
    env = models.CharField(max_length=100)
    made_year = models.CharField(max_length=100)
    location = models.CharField(max_length=20)
    position = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    bought_price = models.IntegerField()
    file_main = models.FileField(upload_to='files/%Y/%m/%d/', default=True)
    file_1 = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    file_2 = models.FileField(upload_to='files/%Y/%m/%d/', blank=True)
    is_published = models.BooleanField(default=True)
    list_date = models.DateTimeField(default=datetime.now, blank=True)    
    def __str__(self):
            return self.hostname